from crewai import Task

def create_recommendation_task(agent, student_profile: str, context) -> Task:
    return Task(description=f"""Using only researched programs and eligibility evidence, identify strong matches for:
{student_profile}
Explain field/degree fit, feasibility, country, budget, language and scholarship fit. Clearly disclose unmet hard requirements.""", expected_output="A concise evidence-based program shortlist.", agent=agent, context=context)
