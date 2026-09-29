from crewai import Agent
from config.llm import build_llm
from tools.web_search import build_web_search_tool
from utils.formatting import require_sources_instruction

def create_scholarship_agent() -> Agent:
    return Agent(
        role="Scholarship Agent",
        goal=(
            "Find current scholarships, tuition waivers and funding attached to the researched programs, and compare "
            "verified scholarship requirements with the student profile. " + require_sources_instruction()
        ),
        backstory=(
            "You are a funding researcher for international students. You distinguish university scholarships, "
            "government funding and automatic tuition awards, and report separate scholarship deadlines when applicable."
        ),
        llm=build_llm(),
        tools=[build_web_search_tool()],
        verbose=True,
        allow_delegation=False,
    )
