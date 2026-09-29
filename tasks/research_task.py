from crewai import Task

def create_research_task(agent, student_profile: str, live_evidence: str) -> Task:
    return Task(
        description=f"""Analyze this applicant against the supplied live admissions evidence.

APPLICANT PROFILE
{student_profile}

LIVE WEB SEARCH EVIDENCE
{live_evidence}

In one concise pass:
1. Select up to 5 relevant university/program matches.
2. Extract only the key verified requirements: academic threshold, language requirement, major prerequisite, deadline, tuition/funding if present.
3. Compare the applicant to those requirements and label each program exactly as: Eligible, Likely Eligible, Missing Requirement, Not Eligible, or Unknown.
4. Note scholarship/funding evidence when present.
5. Preserve the source URL for each program.
6. Mark unsupported facts UNKNOWN.

Keep the output compact for the final reviewer.""",
        expected_output=(
            "A compact structured shortlist of up to 5 programs with verified requirements, "
            "eligibility status, scholarship notes, deadlines and source URLs."
        ),
        agent=agent,
    )
