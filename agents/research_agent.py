from crewai import Agent
from config.llm import build_llm
from utils.formatting import require_sources_instruction

def create_research_agent() -> Agent:
    return Agent(
        role="University Research Agent",
        goal=(
            "Analyze supplied live search evidence to identify relevant degree programs and admissions information. "
            + require_sources_instruction()
        ),
        backstory=(
            "You are a meticulous international admissions researcher. You work only from the live search evidence "
            "supplied in the task plus the applicant profile. You never fabricate thresholds, deadlines, tuition or eligibility rules."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
