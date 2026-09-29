from crewai import Agent
from config.llm import build_llm

def create_recommendation_agent() -> Agent:
    return Agent(
        role="Program Recommendation Agent",
        goal=(
            "Recommend programs from the researched candidate set based on the student's requested field, "
            "degree level, country preferences, budget and stated constraints. Explain fit without inventing requirements."
        ),
        backstory=(
            "You are a university program-matching specialist. You optimize for relevance and feasibility, "
            "not prestige alone, and explain why each suggestion fits the student's stated goals."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
