from crewai import Task

def create_research_task(agent, student_profile: str) -> Task:
    return Task(description=f"""Research current university programs matching this applicant:
{student_profile}
Capture university, exact program, country, official URL, deadline, academic/language requirements, tuition and prerequisites. Prefer official sources. Mark unverified facts UNKNOWN.""", expected_output="A sourced shortlist of relevant programs with current admissions facts and official URLs.", agent=agent)
