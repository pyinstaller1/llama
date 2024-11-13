
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st
import os
from datetime import datetime
from langchain_llama3 import *


def get_time():
    now = datetime.now()
    return f"     [{now.hour}시{now.minute}분{now.second}초]"

def get_time_web():
    now = datetime.now()
    return f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[{now.hour}시{now.minute}분{now.second}초]"

@st.cache_resource  # Streamlit의 cache를 사용하여 한 번만 모델을 로드
def load_model():
    print("모델 로드 시작"+get_time())
    model_name = "verygood7/llama3-ko-8b"
    subfolder = "snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    print("토크나이저 로드 완료"+get_time())
    model = AutoModelForCausalLM.from_pretrained(model_name, subfolder=subfolder)
    return tokenizer, model



@st.cache_resource  # Streamlit의 cache를 사용하여 한 번만 모델을 로드
def load_tokenizer():
    print("모델 로드 시작"+get_time())
    model_name = "verygood7/llama3-ko-8b"
    subfolder = "snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    print("토크나이저 로드 완료"+get_time())
    return tokenizer







st.set_page_config(page_title="라마3", page_icon="🦙")
st.title(":red[NHIS]&nbsp;라마3 🦙 _챗봇_")


if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message[0]).write(chat_message[1])

# if 'tokenizer' not in st.session_state or 'model' not in st.session_state:
#    st.session_state['tokenizer'], st.session_state['model'] = load_model()
#    print("모델 로드 완료"+get_time())

if 'tokenizer' not in st.session_state:
    st.session_state['tokenizer'] = load_tokenizer()
    print("토크나이저 로드 완료"+get_time())    


print("시작"+get_time())






with st.sidebar:
    uploaded_files = st.file_uploader("PDF 자료를 여기에 첨부하세요.", type=['pdf'], accept_multiple_files=True)
    process = st.button("첨부된 파일 등록")
    if process:
        if len(uploaded_files) == 0:
            st.error("파일을 첨부하세요.")
        else:
            message_info = st.info("파일을 벡터 DB에 저장하고 있습니다.")

            # 각 업로드된 파일 처리
            pdf_text = ""
            for file in uploaded_files:
                pdf_text += " ".join([doc.page_content for doc in get_pdf(file)])

            text_chunks = get_text_chunks(pdf_text, st.session_state['tokenizer'])

            vector_db = get_vector_db(text_chunks)   # 벡터 DB에 저장

            print("청크 수:", vector_db.index.ntotal)  # 인덱스에 저장된 벡터의 개수 출력
            for i, (doc_id, document) in enumerate(vector_db.docstore._dict.items()):
                print(f"청크 {i}: {document.page_content[:35]}".replace("\n", " ").replace("\r", " "))

            print(777)
            if "chain" not in st.session_state:
                st.session_state["chain"] = None
            st.session_state["chain"] = get_chain(vector_db)
            print(888)



            message_info.empty()   # 저장이 완료되면 안내 메세지 삭제

            


            









question = st.chat_input("질문을 입력하세요.")
if question:
    st.chat_message("user").write(question + get_time_web())



    if  len(uploaded_files) != 0:                # 첨부파일이 있으면, RAG
        st.chat_message("user").write(question)

        with st.spinner("RAG 답변 생성 중..."):

            # 5.py에서 이 부분에 RAG 챗봇을 만듭니다.

            answer ="RAG 챗봇은 5.py 에서 만듭니다."
            st.chat_message("assistant").write(answer) 


    if  len(uploaded_files) == 0:            # 첨부 파일이 없으면, 챗GPT 3.5
        st.chat_message("user").write(question)
        print(777)

        with st.spinner("라마3 모델이 답변 생성 중..."):
            print(77777777777)

            answer ="라마3 모델이 답변합니다."
            st.chat_message("assistant").write(answer)
            
            # key = os.getenv('OPENAI_KEY')
            # llm = ChatOpenAI(openai_api_key = key)   # 챗GPT에게 질문 (PDF가 없어서 RAG 아님)
            # answer = llm.invoke(question)                # 챗GPT에게 답변을 받아옴 (RAG 아님)
            # answer = answer.content
            # st.chat_message("assistant").write(answer)   # 챗GPT의 답변 출력



    """
    # tokenizer의 __call__ 메서드를 사용해 입력과 attention_mask를 함께 가져옴
    inputs = st.session_state['tokenizer'](question, return_tensors="pt")
    print("질문 엔코딩 완료" + get_time())

    # 모델에 입력값과 attention_mask를 전달하여 출력 생성
    outputs = st.session_state['model'].generate(
        inputs["input_ids"], 
        max_length=300,
        pad_token_id=st.session_state['tokenizer'].pad_token_id,
        attention_mask=inputs["attention_mask"],
        temperature=0.7,        # 생성의 다양성을 약간 추가
        top_p=0.9,              # 선택 범위를 넓혀 보다 풍부한 답변 생성
        repetition_penalty=1.2  # 반복을 억제하여 답변이 다양해짐
    )
    print("답변 벡터 생성 output 완료" + get_time())

    answer = st.session_state['tokenizer'].decode(outputs[0], skip_special_tokens=True)
                                                
    st.chat_message("assistant").write(answer+get_time_web())
    """
















    st.session_state["messages"].append(["user", question+get_time_web()])
    st.session_state["messages"].append(["assistant", answer+get_time_web()])
    print("답변 완료"+get_time())






