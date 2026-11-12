import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGSMITH_PROJECT")

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY key not found in .env file. ")

    llm = ChatGroq(
        model='qwen/qwen3.8-27b',
        temperature=0.2,
        max_tokens=2000,
        api_key=api_key
    )
    return llm
