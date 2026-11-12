import streamlit as st 
from src.code_reviewer import review_code

st.set_page_config(
    page_title="Ai Code Review Assistant",
    page_icon="🤖",
    layout='centered'
)

st.title("🤖 AI Code Review Assistant")

st.write("Analyze Your Source Code using Ai.")

language = st.selectbox(
    "Select Programming Language",
    [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "TypeScript"
    ]
)

code = st.text_area(
    "Enter Your Source code",
    height = 350,
    placeholder="Please Write Your Source code here..."
)

if st.button("Review Code"):
    if not code.strip():
        st.warning("please enter some source code.")
    else:
        with st.spinner("Analyzing Your Code..."):
            try:
                result = review_code(
                    language=language,
                    code=code
                )
                st.success("Code review Completed")

                st.subheader("Bugs and Errors")
                if result.bugs:
                    for bug in result.bugs:
                        st.error(bug)
                else:
                    st.write("No bugs identified. ")

                st.subheader("Security Issues")
                if result.security_issues:
                    for issue in result.security_issues:
                        st.warning(issue)
                else:
                    st.write("No security issues identified. ")

                st.subheader("Performance Issues")
                if result.performance_issues:
                    for issue in result.performance_issues:
                        st.info(issue)
                else:
                    st.write("No performance issue identified. ")

                st.subheader("Improvement Suggestion")
                if result.improvement_suggestions:
                    for sugg in result.improvement_suggestions:
                        st.write(f" - {sugg}")
                else:
                    st.write("No additional suggestions. ")

                st.subheader("Corrected Code")
                if result.corrected_code:
                    st.code(
                        result.corrected_code,
                        language=language.lower()
                    )
                else:
                    st.write("The Code is Corrected.")
            except Exception as e:
                st.error(
                    f"Unable to review the code: {str(e)}"
                )
