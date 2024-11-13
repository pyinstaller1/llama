from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import UnstructuredPowerPointLoader
from datetime import datetime, timedelta
import streamlit as st

from langchain.schema import Document



def get_pdf(file):
    pdf_text = []

    loader = PyPDFLoader(file.name)
    texts = loader.load_and_split()
    pdf_text.extend(texts)

    return pdf_text





def token_len(text, tokenizer):
    tokens = tokenizer.encode(text)
    return len(tokens)


def get_text_chunks(text, tokenizer):  # PDF 데이터를 900단어 단위의 청크로 분리
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=100,
        length_function=lambda txt: token_len(txt, tokenizer)
    )
    chunks = text_splitter.split_text(text)
    return chunks





"""
def get_vector_db(text_chunks):      # 청크 문장 => 벡터 DB 저장
    embeddings = HuggingFaceEmbeddings(
        model_name="jhgan/ko-sroberta-multitask",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    vector_db = FAISS.from_documents(text_chunks, embeddings)
    return vector_db   # 벡터 DB를 리턴
"""





@st.cache_resource  # 한 번만 로드하여 캐싱
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="jhgan/ko-sroberta-multitask",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )

def get_vector_db(text_chunks):
    # 청크를 Document 객체로 변환
    chunk_documents = [Document(page_content=text) for text in text_chunks]
    embeddings = load_embeddings()
    vector_db = FAISS.from_documents(chunk_documents, embeddings)
    return vector_db







from langchain.memory import ConversationBufferMemory

def get_chain(vector_db):
    print("get_chain 함수 시작")

    # Streamlit 세션에서 모델과 토크나이저 가져오기
    model = st.session_state["model"]
    tokenizer = st.session_state["tokenizer"]

    # 람다 파이프라인을 통해 LLM을 래핑 (직접 호출로 연결)
    def model_pipeline(input_text):
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(inputs["input_ids"], max_length=300, pad_token_id=tokenizer.pad_token_id)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 커스텀 래핑된 LLaMA 모델로 ConversationalRetrievalChain 생성
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    chain = ConversationalRetrievalChain.from_llm(
        llm=model_pipeline,
        retriever=retriever,
        memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="answer"),
        get_chat_history=lambda h: h,
        return_source_documents=True,
        verbose=True
    )
    
    print("ConversationalRetrievalChain 생성 성공")
    return chain































