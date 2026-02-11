import logging
from collections import defaultdict

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

user_histories = defaultdict(list)

keyboard = ReplyKeyboardMarkup(
    [[KeyboardButton("Новый запрос")]],
    resize_keyboard=True
)


def clear_user_history(user_id: int):
    user_histories[user_id] = []
    logger.info(f"clear_user_history: {user_id}")


def add_history_query(user_id: int, role: str, role_content: str):
    user_histories[user_id].append(
        {"role": role, "content": role_content}
    )
    logger.info(f"add_user_history: {user_id}")


async def start_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    clear_user_history(update.effective_user.id)
    await update.message.reply_text(
        "Привет!\n"
        "Я бот GPT, какой у тебя запрос?",
        reply_markup=keyboard
    )


async def new_query_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    clear_user_history(update.effective_user.id)
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
    else:
        add_history_query(user_id, "user", user_text)
