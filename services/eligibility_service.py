import re
from typing import Optional

def _number(value: str) -> Optional[float]:
    match = re.search(r"\d+(?:\.\d+)?", value or "")
    return float(match.group()) if match else None

def percentage_meets(student_value: str, required_value: str) -> Optional[bool]:
    student = _number(student_value)
    required = _number(required_value)
    if student is None or required is None:
        return None
    return student >= required

def score_meets(student_value: str, required_value: str) -> Optional[bool]:
    return percentage_meets(student_value, required_value)

def deterministic_check(label: str, student_value: str, required_value: str) -> dict:
    result = score_meets(student_value, required_value)
    if result is True:
        status = "Eligible"
    elif result is False:
        status = "Not Eligible"
    else:
        status = "Unknown"
    return {
        "requirement": label,
        "student_value": student_value or "Unknown",
        "required_value": required_value or "Unknown",
        "status": status,
    }
