from crewai import Agent
from config.llm import build_llm
from utils.formatting import require_sources_instruction

def create_research_agent() -> Agent:
    return Agent(
        role="University Research Agent",
        goal=(
            "Find current degree programs and official admissions information that match the student profile. "
            + require_sources_instruction()
        ),
        backstory=(
            "You are a meticulous international admissions researcher. You focus on current official sources, "
            "program pages and admissions offices. You never fabricate thresholds, deadlines, tuition or eligibility rules."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
