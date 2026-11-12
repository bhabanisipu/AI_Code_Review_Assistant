from src.code_reviewer import review_code

code = """
def divide(a, b):
    return a / b

print(divide(10, 0))
"""

result = review_code("Python", code)

print(result)