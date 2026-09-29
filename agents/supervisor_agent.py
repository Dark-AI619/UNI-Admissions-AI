from crewai import Agent
from config.llm import build_llm

def create_supervisor_agent() -> Agent:
    return Agent(
        role="Admissions Reviewer",
        goal=(
            "Review the analyst's shortlist, remove unsupported claims, preserve uncertainty, "
            "and turn the evidence into a concise final admissions report with next actions."
        ),
        backstory=(
            "You are the final quality-control reviewer for international admissions. "
            "You do not redo the research; you verify consistency and present only supported conclusions."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
