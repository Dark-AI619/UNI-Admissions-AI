import os
from crewai import LLM
from config.settings import get_settings

def build_llm() -> LLM:
    settings = get_settings()
    os.environ["GROQ_API_KEY"] = settings.groq_api_key
    return LLM(
        model=settings.groq_model,
        api_key=settings.groq_api_key,
        temperature=0.2,
    )
