import streamlit as st
from crew.admissions_crew import run_admissions_crew
from models.student_profile import StudentProfile

st.set_page_config(page_title="UNI Admissions AI", page_icon="🎓", layout="wide")

st.title("🎓 UNI Admissions AI")
st.caption("Live admissions research with a compact analyst + reviewer pipeline.")

with st.form("student_profile_form"):
    col1, col2 = st.columns(2)

    with col1:
        current_education = st.selectbox(
            "Current education level",
            ["High School", "Diploma", "Bachelor's", "Master's", "Other"],
        )
        grades = st.text_input(
            "Grades / percentage / GPA",
            placeholder="e.g. 86% or 3.4/4.0",
        )
        desired_degree = st.selectbox(
            "Desired degree",
            ["Bachelor's", "Master's", "PhD", "Diploma", "Language Program"],
        )
        fields = st.text_area(
            "Preferred fields",
            placeholder="e.g. Artificial Intelligence, Computer Science, Automation Engineering",
        )
        preferred_countries = st.text_area(
            "Preferred countries",
            placeholder="e.g. China, Turkey, Germany",
        )

    with col2:
        budget = st.text_input(
            "Annual budget",
            placeholder="e.g. USD 5,000/year",
        )
        scholarship_required = st.checkbox(
            "Scholarship required",
            value=True,
        )
        english = st.text_input(
            "English qualification",
            placeholder="e.g. IELTS 7.0 / TOEFL 95 / None",
        )
        other_languages = st.text_input(
            "Other language qualifications",
            placeholder="e.g. HSK 4, German B1",
        )
        extras = st.text_area(
            "Other qualifications / constraints",
            placeholder="SAT, CSCA, extracurriculars, age, preferred intake, etc.",
        )

    submitted = st.form_submit_button(
        "Run admissions analysis",
        type="primary",
    )

if submitted:
    if not fields.strip() or not preferred_countries.strip():
        st.error("Please enter at least one preferred field and one preferred country.")
        st.stop()

    profile = StudentProfile(
        current_education=current_education,
        grades=grades,
        desired_degree=desired_degree,
        preferred_fields=[x.strip() for x in fields.split(",") if x.strip()],
        preferred_countries=[x.strip() for x in preferred_countries.split(",") if x.strip()],
        budget=budget,
        scholarship_required=scholarship_required,
        english_qualification=english,
        other_language_qualifications=other_languages,
        additional_information=extras,
    )

    with st.spinner("Researching current admissions information and reviewing your profile..."):
        try:
            result = run_admissions_crew(profile)
        except Exception as exc:
            st.exception(exc)
            st.stop()

    st.success("Analysis complete")
    st.markdown(result)
