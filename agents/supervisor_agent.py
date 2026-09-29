from crewai import Agent
from config.llm import build_llm

def create_supervisor_agent() -> Agent:
    return Agent(
        role="Admissions Supervisor Agent",
        goal="Reconcile research, requirements, eligibility, program fit and scholarship findings into a sourced final report. Flag contradictions and preserve uncertainty.",
        backstory="You are the senior reviewer of an international admissions team. You reject unsupported claims, prefer official evidence and present a clear action plan.",
        llm=build_llm(), verbose=True, allow_delegation=False,
    )
