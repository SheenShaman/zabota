import logging

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

from app.history_service import History
from app.client_openai import ClientOpenAI

logger = logging.getLogger(__name__)

history_service = History()
openai_service = ClientOpenAI()

keyboard = ReplyKeyboardMarkup(
    [[KeyboardButton("Новый запрос")]],
    resize_keyboard=True
)


async def start_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    history_service.clear(user_id=update.effective_user.id)
    await update.message.reply_text(
        "Привет!\n"
        "Я бот GPT, какой у тебя запрос?",
        reply_markup=keyboard
    )


async def new_query_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    history_service.clear(user_id=update.effective_user.id)
    await update.message.reply_text(
        "Контекст сброшен\n"
        "Какой у тебя запрос?"
    )


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - начало работы с ботом\n"
        "/help - список доступных команд\n"
        "/new_query - сбросить контекст и сделать новый запрос\n"
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_text = update.message.text
    if user_text == "Новый запрос":
        await new_query_handler(update, context)
        return

    history_service.add(user_id, "user", user_text)
    try:
        user_context = history_service.get(user_id)
        assistant_reply = await openai_service.get_response(user_context)
        history_service.add(user_id, "assistant", assistant_reply)
        await update.message.reply_text(assistant_reply)

    except Exception as e:
        logging.error(f"Ошибка OpenAI: {e}")
        await update.message.reply_text(
            "Произошла ошибка при обращении к ChatGPT."
        )