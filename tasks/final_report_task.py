from crewai import Task

def create_final_report_task(agent, student_profile: str, context) -> Task:
    return Task(
        description=f"""Review the analyst's output for this applicant:
{student_profile}

Return a concise final report containing:
- Best-fit programs
- Eligibility / missing requirements
- Scholarship or funding notes
- Verified deadlines
- Official source URLs
- 3 to 5 next actions

Do not repeat long evidence snippets and do not add unsupported facts.
If evidence is weak or conflicting, state that clearly.
State that this is decision support, not an admission guarantee.""",
        expected_output="A concise Markdown admissions report with sources and next actions.",
        agent=agent,
        context=context,
    )
