from crewai import Task

def create_research_task(agent, student_profile: str, live_evidence: str) -> Task:
    return Task(
        description=f"""Research current university programs matching this applicant:

APPLICANT PROFILE
{student_profile}

LIVE WEB SEARCH EVIDENCE
{live_evidence}

Use the live evidence above as your factual source base.
Capture university, exact program, country, official URL, deadline, academic/language requirements, tuition and prerequisites.
Prefer official university/government pages visible in the evidence.
If a fact is not supported by the evidence, mark it UNKNOWN rather than guessing.""",
        expected_output="A sourced shortlist of relevant programs with current admissions facts and official URLs.",
        agent=agent,
    )
