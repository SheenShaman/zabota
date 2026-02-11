from collections import defaultdict


class History:
    """
    История контекста пользователя
    """
    def __init__(self) -> None:
        self._user_context: dict[int, list[dict[str, str]]] = defaultdict(list)

    def clear(self, user_id: int) -> None:
        self._user_context[user_id] = []

    def add(self, user_id: int, role: str, content: str) -> None:
        self._user_context[user_id].append(
            {"role": role, "content": content}
        )

    def get(self, user_id: int) -> list[dict[str, str]]:
        return self._user_context[user_id]
