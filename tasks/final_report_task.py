from crewai import Task

def create_final_report_task(agent, student_profile: str, context) -> Task:
    return Task(description=f"""Create a final admissions decision-support report for:
{student_profile}
Use sections: Admissions Overview; Recommended Programs; Programs With Blocking Requirements; Scholarship Opportunities; Missing Applicant Information; Next Actions; Verification Note. For each program show eligibility, met/missing requirements, funding, deadline and official sources. Do not add unsupported facts. Explain conflicts. State that screening is not an admission guarantee.""", expected_output="A clear Markdown admissions report with official sources and next actions.", agent=agent, context=context)
