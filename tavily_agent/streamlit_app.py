from agent import app
import streamlit as st
from typing import Dict


"""
    Runs the full RAG agent pipeline using LangGraph, and displays the final output 
    including the question, LLM-generated answer, and retrieved sources.

    Args:
        question (str): The natural-language question from the user.
"""

st.set_page_config(page_title="Tavily RAG Agent", layout="centered")

st.title("📚 Tavily-Powered RAG Agent")
st.markdown("Ask a question and the agent will retrieve web content and answer it using an LLM.")

question = st.text_input("🔍 Enter your question:", placeholder="What are the implications of quantum computing on cybersecurity?")

if st.button("🚀 Run Agent") and question:
    with st.spinner("Running the agent..."):
        result: Dict = app.invoke({"question": question})

    st.subheader("🧠 Question:")
    st.write(result["question"])

    st.subheader("🤖 LLM Answer:")
    st.write(result['llm_answer'])

    st.subheader("🔗 Retrieved Sources:")
    sources = result["tavily_results"]
    if sources:
        for i, source in enumerate(sources, 1):
            title = source.get("title", f"Source {i}")
            url = source.get("url", "#")
            st.markdown(f"{i}. [{title}]({url})")
    else:
        st.write("No sources found.")
