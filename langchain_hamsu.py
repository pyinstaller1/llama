from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFacePipeline
from langchain.chains.combine_documents import map_reduce
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.document_loaders import PyPDFLoader
import streamlit as st
from datetime import datetime, timedelta
import requests
import xml.etree.ElementTree as ET


# 필요한 데이터 불러오기
def get_pdf(uploaded_files):
    pdf_text = []
    for file in uploaded_files:
        loader = PyPDFLoader(file.name)
        texts = loader.load_and_split()
        pdf_text.extend(texts)
    return pdf_text

def get_text_chunks(text, tokenizer, max_length=800):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    text_chunks = text_splitter.split_text(text)
    truncated_chunks = []
    for i, chunk in enumerate(text_chunks):
        tokens = tokenizer.encode(chunk)
        if len(tokens) > max_length:
            tokens = tokens[:max_length]
        truncated_chunk = tokenizer.decode(tokens)
        truncated_chunks.append(truncated_chunk)
    return truncated_chunks

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_vector_db(text_chunks):
    # HuggingFace 임베딩을 사용하여 텍스트를 FAISS로 변환
    embedding = HuggingFaceEmbeddings(model_name='monologg/kobert')
    vector_db = FAISS.from_texts(text_chunks, embedding)
    return vector_db


def create_document_chain(hf_pipeline):
    document_prompt = PromptTemplate(input_variables=["page_content"], template="{page_content}")
    combine_docs_chain = map_reduce(
        llm_chain=LLMChain(
            prompt=PromptTemplate(
                input_variables=["context", "question"],
                template=("Use the following pieces of context to answer the question at the end. "
                          "If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\n"
                          "{context}\n\nQuestion: {question}\nHelpful Answer:")
            ),
            llm=hf_pipeline
        ),
        document_prompt=document_prompt,
        document_variable_name="context"
    )
    return combine_docs_chain






from langchain_community.llms import HuggingFacePipeline
from langchain.chains import ConversationalRetrievalChain

def get_chain(vector_db):
    print("get_chain 함수 시작")
    print("vector_db의 타입 (get_chain 내부):", type(vector_db))  # FAISS 객체인지 확인

    # 파이프라인 생성
    hf_pipeline = HuggingFacePipeline(pipeline=st.session_state["hf_pipeline"])
    print("hf_pipeline 생성 성공")

    # FAISS 객체에서 retriever 생성
    retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    print("retriever 생성 성공")

    # ConversationalRetrievalChain 생성
    try:
        chain = ConversationalRetrievalChain.from_llm(llm=hf_pipeline, retriever=retriever)
        print("ConversationalRetrievalChain 생성 성공")
    except Exception as e:
        print("체인 초기화 중 오류 발생:", e)
        raise e

    print("get_chain 함수 종료")
    return chain








def temperature():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {
        'serviceKey': 'YOUR_API_KEY',
        'pageNo': '1',
        'numOfRows': '1000',
        'dataType': 'XML',
        'base_date': datetime.now().strftime('%Y%m%d'),
        'base_time': (datetime.now().replace(minute=0, second=0, microsecond=0) - timedelta(hours=1)).strftime('%H%M'),
        'nx': '77',
        'ny': '122'
    }
    response = requests.get(url, params=params)
    root = ET.fromstring(response.content)
    temperature_item = root.find(".//item[category='T1H']")
    temperature = temperature_item.find('obsrValue').text
    return f"현재 온도는 {temperature}도입니다."
