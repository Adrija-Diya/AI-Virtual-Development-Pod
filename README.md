# AI-powered virtual development pod

An AI-powered virtual development assistant that simulates a collaborative software development team using multiple AI agents and Retrieval-Augmented Generation (RAG).
The system analyzes user development tasks, retrieves relevant technical knowledge, generates implementation requirements, produces code, and reviews the generated code for improvements.
The application is built with Streamlit and uses Google Gemini LLM along with RAG-based knowledge retrieval using FAISS and Sentence Transformers.
This project demonstrates how multi-agent AI systems can automate different stages of the software development lifecycle, including requirement analysis, code generation, and testing.

Key Features:

Multi-agent AI architecture
Retrieval-Augmented Generation (RAG)
Automated requirement analysis
AI-powered code generation
Code review and testing agent
Interactive user interface
Real-time AI responses

System Architecture:

The system works as a Virtual AI Development Team:

User Input
   ↓
RAG Knowledge Retrieval
   ↓
Requirement Analysis Agent
   ↓
Code Generation Agent
   ↓
Code Testing Agent
   ↓
Streamlit Interface

AI Agents:

1. Requirement Analysis Agent
Analyzes the user's development request and extracts the functional and technical requirements needed for implementation.

2. Code Generation Agent
Generates relevant code based on the analyzed requirements using the LLM.

3. Testing Agent
Reviews the generated code to identify potential bugs, security risks, and possible improvements.
Retrieval-Augmented Generation (RAG)
The project integrates a RAG pipeline to enhance LLM responses with contextual knowledge.

Process:

User query is converted into embeddings.
Embeddings are compared with a knowledge base using FAISS vector search.
Relevant context is retrieved.
The retrieved knowledge is provided to the AI agents for better responses.

Tech Stack:

Programming Language:
Python

AI / Machine Learning:
Google Gemini LLM (Gemini 2.5 Flash)
Sentence Transformers (all-MiniLM-L6-v2)

Vector Database:
FAISS (Facebook AI Similarity Search)

Frameworks:
Streamlit (User Interface)

Libraries:
google-generativeai
sentence-transformers
faiss-cpu
numpy

Development Environment:
Visual Studio Code

Version Control:
Git
GitHub

Platforms Used:
Google AI Studio / Gemini API
GitHub (Repository hosting)
Streamlit Local Server
Python Virtual Environment (venv)

Example Use Cases:

Generate a Flask login API

Create REST APIs in Python

Generate Python utility functions

Review and improve generated code

Installation:

Clone the repository:

git clone https://github.com/yourusername/AI-Virtual-Development-Pod.git

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py
Future Improvements

Integration with GitHub Copilot-like code assistance

Database-driven RAG knowledge base

CI/CD integration for automated testing

Deployment on cloud platforms

Author
Adrija Singh
