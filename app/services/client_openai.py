from openai import AsyncOpenAI

from app.constants import AI_MODEL_ID, OPENROUTER_API_KEY, OPENROUTER_URL


class ClientOpenAI:
    """
    Клиент для обращения к OpenAI
    """

    def __init__(self) -> None:
        self.client = AsyncOpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url = OPENROUTER_URL,
        )

    async def get_response(self, user_context: list[dict[str, str]]) -> str:
        response = await self.client.chat.completions.create(
            model=AI_MODEL_ID,
            messages=user_context,
            max_tokens=150,
            temperature=0.5,
        )
        return response.choices[0].message.content
