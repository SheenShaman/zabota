from openai import OpenAI

from app.constants import OPENAI_API_KEY


class ClientOpenAI:
    """
    Клиент для обращения к OpenAI
    """

    def __init__(self) -> None:
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_response(self, user_context: list[dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=user_context,
            max_tokens=100,
            temperature=0.5,
        )
        return response.choices[0].message.content
