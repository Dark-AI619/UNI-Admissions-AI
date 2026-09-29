from crewai import Task

def create_requirements_task(agent, context) -> Task:
    return Task(description="Extract a program-by-program checklist: grades/GPA, prior-study prerequisites, language tests, standardized tests, age/nationality rules, documents, deadline, fees and scholarship criteria. Never invent missing values; preserve source URLs.", expected_output="A requirement matrix with URLs and UNKNOWN for unverified fields.", agent=agent, context=context)
