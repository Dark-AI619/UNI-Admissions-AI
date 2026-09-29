# UNI Admissions AI

A modular multi-agent university admissions assistant built with Streamlit, CrewAI and Groq.

## What it does

The system uses six specialist agents:

1. University Research Agent
2. Requirements Extraction Agent
3. Eligibility Agent
4. Program Recommendation Agent
5. Scholarship Agent
6. Admissions Supervisor Agent

The Research and Scholarship agents use live web search. The other agents reason only over researched evidence.

## Architecture

- `streamlit_app.py` — Streamlit UI
- `agents/` — one file per agent
- `tasks/` — one file per CrewAI task
- `crew/` — orchestration
- `models/` — Pydantic data models
- `services/` — Groq and deterministic eligibility helpers
- `tools/` — reusable web research tools
- `utils/` — formatting helpers

## Deploy on Streamlit Community Cloud

1. Open Streamlit Community Cloud.
2. Create a new app from this GitHub repository.
3. Select branch `main`.
4. Entrypoint: `streamlit_app.py`.
5. Use **Python 3.12** in Advanced settings.
6. In **Advanced settings → Secrets**, add:

```toml
GROQ_API_KEY = "your-real-groq-api-key"
SERPER_API_KEY = "your-serper-api-key"
```

7. Deploy.

The repository also includes `runtime.txt` pinned to Python 3.12 to avoid CrewAI/ChromaDB/Pydantic incompatibilities seen under Python 3.14.

Do not commit real secrets.

## Model

Default Groq model:

```
openai/gpt-oss-120b
```

## Reliability rule

The agents are instructed not to invent admission requirements. Unknown or unverified requirements must be reported as UNKNOWN. Final recommendations preserve source URLs and distinguish verified facts from interpretation.
