# Telegram GPT Bot

Telegram-бот на Python с интеграцией OpenAI API.
Бот сохраняет контекст диалога и генерирует ответы с использованием ChatGPT.

### Возможности

- Ответ на команды /start, /help, /new_query
- Генерация ответов через OpenAI API
- Сохранение истории диалога для каждого пользователя

Сброс контекста:

- по команде /start
- по команде /new_query
- по кнопке «Новый запрос»

### Описание модулей

- main.py — точка входа, регистрация handlers и запуск бота
- handlers.py — обработчики команд и сообщений
- history_service.py — хранение истории диалога
- openai_service.py — взаимодействие с OpenAI API
- constants.py — конфигурация (токены)
- logger.py — настройка логирования

### Установка

- git clone https://github.com/SheenShaman/zabota.git
- cd zabota
- python -m venv .venv
- source .venv/bin/activate
- pip install poetry
- poetry install

### Настройка переменных окружения

Создать файл .env в корне проекта:
`TELEGRAM_TOKEN=your_telegram_token`
`OPENAI_API_KEY=your_openai_api_key`

### Запуск

`python main.py`
