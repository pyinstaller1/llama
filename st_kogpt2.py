from langchain.chains import LLMChain, ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast, pipeline
import streamlit as st
import os
from datetime import datetime
from langchain_hamsu import *

def get_time():
    now = datetime.now()
    return f"[{now.hour}시{now.minute}분{now.second}초]"

st.set_page_config(page_title="챗봇", page_icon=":robot_face:")
st.title(":red[NHIS]&nbsp;koGPT2 _챗봇_ :robot_face:")

# 모델 및 토크나이저 초기화
if "model" not in st.session_state or "tokenizer" not in st.session_state:
    model_name = os.path.join(os.path.dirname(__file__), "models--skt--kogpt2-base-v2", "snapshots", "d0c0df48bf2b2c9350dd855021a5b216f560c0c7")
    st.session_state["tokenizer"] = GPT2TokenizerFast.from_pretrained(model_name)
    st.session_state["model"] = GPT2LMHeadModel.from_pretrained(model_name)
    st.session_state["tokenizer"].pad_token = st.session_state["tokenizer"].eos_token
    print("모델 및 토크나이저가 성공적으로 초기화되었습니다.")

# hf_pipeline 초기화
if "hf_pipeline" not in st.session_state:
    st.session_state["hf_pipeline"] = pipeline(
        "text-generation",
        model=st.session_state["model"],
        tokenizer=st.session_state["tokenizer"],
        device=0 if torch.cuda.is_available() else -1,
        max_length=512,
        max_new_tokens=100,
        truncation=True,
        clean_up_tokenization_spaces=True
    )
    print("hf_pipeline이 성공적으로 초기화되었습니다.")

# HuggingFacePipeline을 사용하여 hf_chain 초기화
# HuggingFacePipeline을 사용하여 hf_chain 초기화
if "hf_chain" not in st.session_state:
    try:
        hf_pipeline = HuggingFacePipeline(pipeline=st.session_state["hf_pipeline"])
        
        # PromptTemplate 수정 부분
        prompt = PromptTemplate(
            input_variables=["input_text"],
            template="질문에 대해 간단하고 명확한 답변을 생성하세요. 질문: {input_text}"
        )
        
        st.session_state["hf_chain"] = LLMChain(prompt=prompt, llm=hf_pipeline)
        print("hf_chain이 성공적으로 초기화되었습니다.")
    except Exception as e:
        print("hf_chain 초기화 중 오류 발생:", e)



# ConversationalRetrievalChain을 사용하여 chain 생성
if "chain" not in st.session_state:
    try:
        st.session_state["chain"] = get_chain(st.session_state["hf_chain"])
        print("chain이 성공적으로 초기화되었습니다.")
    except Exception as e:
        print("체인 초기화 중 오류 발생:", e)

MAX_INPUT_LENGTH = 512

# 입력 텍스트 길이 제한을 위한 함수
def truncate_input(text, tokenizer, max_length=512):
    tokens = tokenizer.encode(text, truncation=True, max_length=max_length)
    return tokenizer.decode(tokens)

# 사이드바 파일 업로드 및 벡터 DB 생성
with st.sidebar:
    uploaded_files = st.file_uploader("PDF 자료를 여기에 첨부하세요.", type=['pdf'], accept_multiple_files=True)
    process = st.button("첨부된 파일 등록")
    if process:
        if len(uploaded_files) == 0:
            st.error("파일을 첨부하세요.")
        else:
            message_info = st.info("파일을 벡터 DB에 저장하고 있습니다.")
            
            # PDF 파일에서 텍스트 추출 및 청크 생성
            pdf_text = " ".join([doc.page_content for doc in get_pdf(uploaded_files)])
            text_chunks = get_text_chunks(pdf_text, st.session_state["tokenizer"])
            st.session_state["text_chunks"] = [{"content": chunk, "index": i + 1} for i, chunk in enumerate(text_chunks)]
            
            try:
                # 벡터 DB 생성 및 타입 확인
                embedding = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
                vector_db = FAISS.from_texts([chunk["content"] for chunk in st.session_state["text_chunks"]], embedding)
                print("vector_db의 타입:", type(vector_db))  # FAISS 객체가 생성되었는지 확인
                
                # 체인 생성
                chain_candidate = get_chain(vector_db)
                if chain_candidate is not None:
                    st.session_state["chain"] = chain_candidate
                    print("체인이 성공적으로 초기화되었습니다.")
                else:
                    st.error("체인을 초기화하지 못했습니다.")
            
            except Exception as e:
                print("체인 초기화 중 오류 발생:", e)
                st.error(f"체인 초기화 중 오류 발생: {e}")
            
            finally:
                message_info.empty()


# 질문 입력 및 답변 생성
question = st.chat_input("질문을 입력하세요.")
if question:
    print("질문 시작", get_time())
    print(f"질문 내용: {question} {get_time()}")
    st.chat_message("user").write(f"{question} {get_time()}")

    if "chain" in st.session_state:
        truncated_question = truncate_input(question, st.session_state["tokenizer"], MAX_INPUT_LENGTH)
        inputs = {"question": truncated_question, "chat_history": []}

        try:
            print("retriever 호출 시작")
            retriever = st.session_state["chain"].retriever
            query_result = retriever.get_relevant_documents(truncated_question)
            print(f"검색된 청크 수: {len(query_result)}")

            for i, doc in enumerate(query_result):
                original_chunk = next((chunk for chunk in st.session_state["text_chunks"] if chunk["content"] == doc.page_content), None)
                original_index = original_chunk["index"] if original_chunk else "알 수 없음"
                short_chunk = doc.page_content.replace("\n", " ").replace("\r", " ")[:35]
                print(f"청크 {original_index}, 내용 (35자 이내): {short_chunk}...")

            print("응답 생성 시작")
            result = st.session_state["chain"](inputs)
            answer = result.get("answer", "답변을 생성할 수 없습니다.")
            print("응답 생성 완료")

            if "Helpful Answer:" in answer:
                answer = answer.split("Helpful Answer:")[-1].strip()
            st.chat_message("assistant").write(f"{answer} {get_time()}")

        except Exception as e:
            import traceback
            print("질문 처리 중 오류 발생:", e)
            traceback.print_exc()
            st.error(f"오류 발생: {e}")
    else:
        st.error("체인이 설정되지 않았습니다.")

    print("답변 완료", get_time())
