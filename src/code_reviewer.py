from src.llm_config import get_llm
from src.schemas import CodeReview

from langchain_core.prompts import ChatPromptTemplate

llm = get_llm()

structured_llm = llm.with_structured_output(CodeReview)

prompt = ChatPromptTemplate.from_template("""
You are an expert software engineer and professional code reviewer.

Your task is to review the submitted source code.

Programming Language: {language}

Source Code:
{code}

Follow these instructions carefully:

1. Analyze the code using the specified programming language.
2. Identify bugs, runtime errors and logical errors.
3. Explain why each issue occurs.
4. Identify potential security vulnerabilities.
5. Identify performance issues.
6. Suggest code quality improvements.
7. Provide corrected code.

IMPORTANT RULES:
- Never change the original programming language.
- Do not convert the code into Python or any other language.
- The corrected code must use {language}.
- Preserve the original functionality.
- If no issue is found, clearly mention that.
- Do not invent errors that are not supported by the code.

""")

code_review_chain = prompt | structured_llm

def review_code(language: str, code: str) -> CodeReview:
    """
    Analyze source code and return a structured code review.
    """

    if not language or not language.strip():
        raise ValueError("Programming language is required.")

    if not code or not code.strip():
        raise ValueError("Source code is required.")

    try:
        result = code_review_chain.invoke({
            "language": language,
            "code": code
        })

        return result

    except Exception as e:
        raise RuntimeError(
            f"Code review failed: {str(e)}"
        ) from e

