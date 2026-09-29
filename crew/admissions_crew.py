import time
from crewai import Crew, Process
from agents.research_agent import create_research_agent
from agents.supervisor_agent import create_supervisor_agent
from tasks.research_task import create_research_task
from tasks.final_report_task import create_final_report_task
from models.student_profile import StudentProfile
from services.web_search_service import build_admissions_research

def build_admissions_crew(profile: StudentProfile) -> Crew:
    profile_text = profile.to_prompt()
    live_evidence = build_admissions_research(profile_text)

    analyst = create_research_agent()
    reviewer = create_supervisor_agent()

    analysis_task = create_research_task(
        analyst,
        profile_text,
        live_evidence,
    )

    final_task = create_final_report_task(
        reviewer,
        profile_text,
        [analysis_task],
    )

    return Crew(
        agents=[analyst, reviewer],
        tasks=[analysis_task, final_task],
        process=Process.sequential,
        verbose=True,
    )

def run_admissions_crew(profile: StudentProfile) -> str:
    last_error = None

    for attempt in range(3):
        try:
            result = build_admissions_crew(profile).kickoff()
            return getattr(result, "raw", None) or str(result)
        except Exception as exc:
            last_error = exc
            message = str(exc).lower()

            if "rate limit" not in message and "rate_limit" not in message and "429" not in message:
                raise

            if attempt < 2:
                time.sleep(5 * (attempt + 1))

    raise last_error
