from crewai import Agent
from config.llm import build_llm
from utils.formatting import require_sources_instruction

def create_scholarship_agent() -> Agent:
    return Agent(
        role="Scholarship Agent",
        goal=(
            "Analyze supplied live search evidence for scholarships, tuition waivers and funding attached to researched programs. "
            + require_sources_instruction()
        ),
        backstory=(
            "You are a funding researcher for international students. You only use the supplied evidence and prior task context, "
            "distinguish funding types, and never invent coverage, deadlines or criteria."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
