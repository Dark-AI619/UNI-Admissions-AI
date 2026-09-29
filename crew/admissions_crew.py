import time
from crewai import Crew, Process
from agents.research_agent import create_research_agent
from agents.requirements_agent import create_requirements_agent
from agents.eligibility_agent import create_eligibility_agent
from agents.recommendation_agent import create_recommendation_agent
from agents.scholarship_agent import create_scholarship_agent
from agents.supervisor_agent import create_supervisor_agent
from tasks.research_task import create_research_task
from tasks.requirements_task import create_requirements_task
from tasks.eligibility_task import create_eligibility_task
from tasks.recommendation_task import create_recommendation_task
from tasks.scholarship_task import create_scholarship_task
from tasks.final_report_task import create_final_report_task
from models.student_profile import StudentProfile
from services.web_search_service import build_admissions_research

def build_admissions_crew(profile: StudentProfile) -> Crew:
    p = profile.to_prompt()
    live_evidence = build_admissions_research(p)

    a1 = create_research_agent()
    a2 = create_requirements_agent()
    a3 = create_eligibility_agent()
    a4 = create_recommendation_agent()
    a5 = create_scholarship_agent()
    a6 = create_supervisor_agent()

    t1 = create_research_task(a1, p, live_evidence)
    t2 = create_requirements_task(a2, [t1])
    t3 = create_eligibility_task(a3, p, [t2])
    t4 = create_recommendation_task(a4, p, [t1, t2, t3])
    t5 = create_scholarship_task(a5, p, [t1, t2, t3])
    t6 = create_final_report_task(a6, p, [t1, t2, t3, t4, t5])

    return Crew(
        agents=[a1, a2, a3, a4, a5, a6],
        tasks=[t1, t2, t3, t4, t5, t6],
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
            text = str(exc).lower()
            if "rate limit" not in text and "rate_limit" not in text and "429" not in text:
                raise
            if attempt < 2:
                time.sleep(6 * (attempt + 1))
    raise last_error
