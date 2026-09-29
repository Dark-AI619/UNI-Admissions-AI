from crewai import Task

def create_eligibility_task(agent, student_profile: str, context) -> Task:
    return Task(description=f"""Evaluate this applicant against every verified requirement:
{student_profile}
For each criterion use exactly: Eligible, Likely Eligible, Missing Requirement, Not Eligible, or Unknown. Explain briefly. Missing applicant data is never a pass and this is not an admission guarantee.""", expected_output="Requirement-by-requirement eligibility assessment for each program.", agent=agent, context=context)
