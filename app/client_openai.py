from openai import OpenAI

from app.constants import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def openai_query(user_context: list[dict[str, str]]) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=user_context,
        temperature=0.7
    )
    assistant_reply = response.choices[0].message.content
    return assistant_reply