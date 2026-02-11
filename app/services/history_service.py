from collections import defaultdict

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "Ты Telegram-бот. "
        "Отвечай кратко и по существу."
    )
}


class History:
    """
    История контекста пользователя
    """
    def __init__(self) -> None:
        self._user_context = defaultdict(list)

    def clear(self, user_id: int) -> None:
        self._user_context[user_id] = [SYSTEM_PROMPT]

    def add(self, user_id: int, role: str, content: str) -> None:
        self._user_context[user_id].append(
            {"role": role, "content": content}
        )

    def get(self, user_id: int) -> list[dict[str, str]]:
        return self._user_context[user_id]
