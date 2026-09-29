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

The agents research current admissions information, extract requirements, compare them with the applicant profile, find relevant scholarships/programs and produce a final sourced report.

## Architecture

- `streamlit_app.py` — Streamlit UI
- `agents/` — one file per agent
- `tasks/` — one file per CrewAI task
- `crew/` — orchestration
- `models/` — Pydantic data models
- `services/` — Groq configuration and deterministic eligibility helpers
- `utils/` — formatting helpers

## Deploy on Streamlit Community Cloud

1. Open Streamlit Community Cloud.
2. Create a new app from this GitHub repository.
3. Select branch `main`.
4. Entrypoint: `streamlit_app.py`.
5. In **Advanced settings → Secrets**, add:

```toml
GROQ_API_KEY = "your-real-groq-api-key"
```

6. Deploy.

Do not commit a real `.streamlit/secrets.toml` file.

## Model

Default Groq model:

```
openai/gpt-oss-120b
```

## Reliability rule

The agents are explicitly instructed not to invent admission requirements. Unknown or unverified requirements must be reported as unknown. Final recommendations should preserve source URLs and distinguish verified requirements from interpretation.
