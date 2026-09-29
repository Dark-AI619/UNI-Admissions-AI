from crewai import Agent
from config.llm import build_llm
from utils.formatting import require_sources_instruction

def create_research_agent() -> Agent:
    return Agent(
        role="Admissions Analyst",
        goal=(
            "Analyze the supplied live search evidence and applicant profile in one pass. "
            "Identify relevant programs, extract the key verified admission requirements, "
            "estimate fit, and note scholarship information when present. "
            + require_sources_instruction()
        ),
        backstory=(
            "You are an evidence-first international admissions analyst. "
            "You combine research, requirements extraction, program matching and preliminary "
            "eligibility screening without inventing facts."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
