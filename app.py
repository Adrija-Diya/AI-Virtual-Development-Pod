import streamlit as st
import google.generativeai as genai
from agents import requirement_agent, code_agent, testing_agent
from rag import retrieve_context

# Configure API
genai.configure(api_key="AIzaSyAfJ53SslReHw6AJf667KhWsAOsgrwxsb0")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Powered Virtual Development Pod")
st.write("Multi-Agent AI Development Assistant with RAG")

user_input = st.text_input("Enter your development task:")

if st.button("Generate"):
    if user_input:

        st.subheader("Step 1:Retrieved Knowledge(RAG)")
        context = retrieve_context(user_input)
        st.write(context)

        st.subheader("Step 2: Requirement Analysis Agent")
        requirements = requirement_agent(user_input + "\n\nContext:\n" + context, model)
        st.write(requirements)

        st.subheader("Step 3: Code Generation Agent")
        code = code_agent(requirements, model)
        st.write(code)

        st.subheader("Step 4: Code Testing Agent")
        review = testing_agent(code, model)
        st.write(review)

    else:
        st.write("Please enter a task.")