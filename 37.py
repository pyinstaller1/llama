
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st
import os

st.title("건강보험 AI 동호회 챗봇")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message[0]).write(chat_message[1])


print(7)

@st.cache_resource  # Streamlit의 cache를 사용하여 한 번만 모델을 로드
def load_model():
    model_name = "verygood7/llama3-ko-8b"
    subfolder = "snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    model = AutoModelForCausalLM.from_pretrained(model_name, subfolder=subfolder)
    return tokenizer, model


if 'tokenizer' not in st.session_state or 'model' not in st.session_state:
    st.session_state['tokenizer'], st.session_state['model'] = load_model()

question = st.chat_input("질문을 입력하세요.")
if question:
    st.chat_message("user").write(question)

    # inputs = st.session_state['tokenizer'].encode(question, return_tensors="pt")
    inputs = tokenizer.encode(question, return_tensors="pt")

    # key = os.getenv('OPENAI_KEY')
    # llm = ChatOpenAI(openai_api_key=key)
    # answer = llm.invoke(question)
    # answer = answer.content
    answer = "답변: " + question

    st.chat_message("assistant").write(answer)

    st.session_state["messages"].append(["user", question])
    st.session_state["messages"].append(["assistant", answer])

