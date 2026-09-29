from crewai import Task

def create_scholarship_task(agent, student_profile: str, context) -> Task:
    return Task(description=f"""Check funding relevant to this student and researched programs:
{student_profile}
Give scholarship name/provider, coverage, criteria, deadline, apparent eligibility, missing information and official URL. Never infer funding without evidence.""", expected_output="A sourced scholarship/funding assessment.", agent=agent, context=context)
