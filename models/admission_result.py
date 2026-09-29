from pydantic import BaseModel, Field
from typing import Literal

EligibilityStatus = Literal["Eligible", "Likely Eligible", "Missing Requirement", "Not Eligible", "Unknown"]

class RequirementCheck(BaseModel):
    requirement: str
    applicant_value: str = "Unknown"
    status: EligibilityStatus = "Unknown"
    explanation: str = ""

class ProgramAssessment(BaseModel):
    university: str
    program: str
    country: str
    eligibility: EligibilityStatus
    checks: list[RequirementCheck] = Field(default_factory=list)
    scholarship_notes: str = ""
    deadline: str = "Unknown"
    source_urls: list[str] = Field(default_factory=list)
