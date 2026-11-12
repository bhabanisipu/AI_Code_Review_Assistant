from pydantic import BaseModel,Field
from typing import List

class CodeReview(BaseModel):
    bugs: List[str] = Field(
        description="List of bugs and errors identified in the code"
    )
    security_issues: List[str] = Field(
        description="List of potential security vulnerabilities"
    )
    performance_issues: List[str] = Field(
        description="List of performance-related issues"
    )
    improvement_suggestions: List[str] = Field(
        description="Suggestions to improve code quality"
    )
    corrected_code: str = Field(
        description="Corrected source code in the original programming language"
    )