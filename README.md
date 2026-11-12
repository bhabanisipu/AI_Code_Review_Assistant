# 🤖 AI Code Review Assistant

An AI-powered code review application built using **Python, LangChain, Groq API, Qwen3.8-27B, Pydantic, Streamlit, and LangSmith**.

## 📌 Project Overview

AI Code Review Assistant automatically analyzes source code and identifies potential bugs, security vulnerabilities, and performance issues. It also provides improvement suggestions and generates corrected code using Generative AI.

## 🚀 Features

- 🐞 Bug and error detection
- 🔐 Security vulnerability analysis
- ⚡ Performance issue identification
- 💡 Code improvement suggestions
- ✅ Corrected code generation
- 📊 Structured output using Pydantic
- 📈 LLM monitoring using LangSmith
- 💻 Multiple programming language selection

## 🛠️ Technologies Used

- Python
- LangChain
- Groq API
- Qwen3.8-27B
- Pydantic
- Streamlit
- LangSmith

## 🏗️ Project Workflow

1. User selects a programming language.
2. User submits source code.
3. LangChain prepares the prompt.
4. Qwen3.8-27B analyzes the code through Groq API.
5. Pydantic validates the structured response.
6. Streamlit displays the code review results.
7. LangSmith monitors LLM executions.

## 📂 Project Structure

```text
AI_Code_Review_Assistant/
│
├── notebooks/
├── src/
│   ├── llm_config.py
│   ├── schemas.py
│   └── code_reviewer.py
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
cd AI_Code_Review_Assistant

python -m venv code
code\Scripts\activate

pip install -r requirements.txt
```

## ▶️ Run Application

```bash
streamlit run app.py
```

## 📈 Monitoring

Integrated **LangSmith** to monitor LLM executions, inspect prompts and responses, track latency, and debug errors.

## 🔮 Future Enhancements

- Automated unit-test generation
- Secure code execution and validation
- GitHub integration
- Code quality reports

## 👨‍💻 Author

**Bhabani Sankar Sahoo**

B.Tech – Computer Science and Engineering (AI/ML)

**Interests:** Generative AI | Machine Learning | Deep Learning | NLP | LangChain
