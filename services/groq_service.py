from groq import Groq
from config.settings import get_settings

def get_groq_client() -> Groq:
    settings = get_settings()
    return Groq(api_key=settings.groq_api_key)

def groq_chat(messages: list[dict], model: str = "openai/gpt-oss-120b") -> str:
    client = get_groq_client()
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2,
    )
    return response.choices[0].message.content or ""
