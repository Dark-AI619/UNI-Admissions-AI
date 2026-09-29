from pydantic import BaseModel, Field

class StudentProfile(BaseModel):
    current_education: str
    grades: str = ""
    desired_degree: str
    preferred_fields: list[str] = Field(default_factory=list)
    preferred_countries: list[str] = Field(default_factory=list)
    budget: str = ""
    scholarship_required: bool = True
    english_qualification: str = ""
    other_language_qualifications: str = ""
    additional_information: str = ""

    def to_prompt(self) -> str:
        return (
            f"Current education: {self.current_education}\n"
            f"Grades: {self.grades or 'Not provided'}\n"
            f"Desired degree: {self.desired_degree}\n"
            f"Preferred fields: {', '.join(self.preferred_fields) or 'Not provided'}\n"
            f"Preferred countries: {', '.join(self.preferred_countries) or 'Not provided'}\n"
            f"Annual budget: {self.budget or 'Not provided'}\n"
            f"Scholarship required: {'Yes' if self.scholarship_required else 'No'}\n"
            f"English qualification: {self.english_qualification or 'Not provided'}\n"
            f"Other language qualifications: {self.other_language_qualifications or 'Not provided'}\n"
            f"Additional information: {self.additional_information or 'None'}"
        )
