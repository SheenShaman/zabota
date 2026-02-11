import logging

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters
)

from app.constants import TELEGRAM_TOKEN
from app.logger import setup_logging
from app.services.handlers import (
    start_handler,
    help_handler,
    new_query_handler,
    message_handler,
    unknown_command_handler,
)

setup_logging()
logger = logging.getLogger(__name__)


def main():
    """
    Создаем бота и подключаем кнопки
    """
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    logger.info("Bot startup")

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("new_query", new_query_handler))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command_handler))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
