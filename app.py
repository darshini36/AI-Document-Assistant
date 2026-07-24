import streamlit as st
from rag import ask_question

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Document Assistant")

question = st.text_input("Ask a question about your PDF")

if st.button("Ask"):

    if question:

        answer = ask_question(question)

        st.subheader("Answer")

        st.write(answer)