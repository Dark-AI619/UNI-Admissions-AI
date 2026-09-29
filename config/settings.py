import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    groq_api_key: str
    groq_model: str = "groq/openai/gpt-oss-120b"

def get_settings() -> Settings:
    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        try:
            import streamlit as st
            api_key = str(st.secrets.get("GROQ_API_KEY", "")).strip()
        except Exception:
            api_key = ""
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is missing. Add it to Streamlit Secrets before running the app."
        )
    return Settings(groq_api_key=api_key)
