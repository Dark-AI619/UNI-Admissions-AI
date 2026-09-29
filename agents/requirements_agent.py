from crewai import Agent
from config.llm import build_llm
from utils.formatting import require_sources_instruction

def create_requirements_agent() -> Agent:
    return Agent(
        role="Requirements Extraction Agent",
        goal=(
            "Convert researched admissions information into a structured list of academic, language, document, "
            "age, prerequisite, deadline, tuition and scholarship requirements. "
            + require_sources_instruction()
        ),
        backstory=(
            "You specialize in translating complicated admissions pages into precise applicant requirements. "
            "You separate mandatory requirements from preferences and never infer missing rules."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
