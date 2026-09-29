from crewai import Agent
from config.llm import build_llm

def create_eligibility_agent() -> Agent:
    return Agent(
        role="Eligibility Agent",
        goal=(
            "Compare the student's supplied profile against verified admission requirements. "
            "Use one of: Eligible, Likely Eligible, Missing Requirement, Not Eligible, or Unknown. "
            "Never treat missing applicant data as a pass."
        ),
        backstory=(
            "You are an evidence-first eligibility analyst. You compare each criterion independently, "
            "state what is satisfied or missing, and avoid overclaiming."
        ),
        llm=build_llm(),
        verbose=True,
        allow_delegation=False,
    )
