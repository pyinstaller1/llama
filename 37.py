%%writefile app.py
import streamlit as st
from langchain_openai import ChatOpenAI
import os

st.title("건강보험 AI 동호회 챗봇")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message[0]).write(chat_message[1])

question = st.chat_input("질문을 입력하세요.")
if question:
    st.chat_message("user").write(question)

    key = os.getenv('OPENAI_KEY')
    llm = ChatOpenAI(openai_api_key=key)

    answer = llm.invoke(question)
    answer = answer.content
    st.chat_message("assistant").write(answer)

    st.session_state["messages"].append(["user", question])
    st.session_state["messages"].append(["assistant", answer])
