import streamlit as st
import utils
import tempfile

st.title("AI Integrated Job Search and Skill & Competencies Match (based on URL) ")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
st.divider()

st.set_page_config(page_title="RAG", page_icon="🧠", layout="wide")


col_input , col_rag = st.columns([1,5])
with col_input:
    target_url = st.text_input("URL",placeholder="https://en.wikipedia.org/wiki/Large_language_model")
    st.divider()
    prompt = st.text_input("Prompt", placeholder="What is the LLM?",
                           key="url_prompt")
    st.divider()
    sumbit_btn = st.button(label="Submit",key="url_btn")

    print(target_url)
    print(prompt)
    if sumbit_btn:
        with col_rag:
            with st.spinner("Processing..."):
                st.success("Response: Answering with RAG...")
                response = utils.rag_with_url(target_url,prompt)
                st.markdown(response)
                st.divider()
            