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
from transformers import pipeline


def get_time():
    now = datetime.now()
    return f"     [{now.hour}시{now.minute}분{now.second}초]"



"""
def get_pdf(file):
    pdf_text = []

    loader = PyPDFLoader(file.name)
    texts = loader.load_and_split()
    pdf_text.extend(texts)

    return pdf_text
"""

def get_pdf(uploaded_files):   # PDF 파일들에서 데이터 가져오기
    pdf_text = []

    for file in uploaded_files:
        loader = PyPDFLoader(file.name)
        texts = loader.load_and_split()
        pdf_text.extend(texts)

    return pdf_text   # PDF 파일들에서 꺼낸 텍스트 데이터를 1개의 [리스트] 에 저장해서 리턴






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







@st.cache_resource  # 한 번만 로드하여 캐싱
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="jhgan/ko-sroberta-multitask",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )


def get_vector_db(text_chunks):
    # 청크를 Document 객체로 변환 (chunk_id 추가)
    chunk_documents = [
        Document(page_content=text, metadata={"chunk_id": idx}) 
        for idx, text in enumerate(text_chunks)
    ]
    embeddings = load_embeddings()
    vector_db = FAISS.from_documents(chunk_documents, embeddings)
    return vector_db





from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

def get_chain(vector_db, model, tokenizer, template_input):
    print("get_chain 함수 시작" + get_time())

    hf_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=0,
        framework="pt",
        return_text=True
    )
    print("Hugging Face pipeline 생성 성공")

    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    print(f"LangChain에서 사용하는 모델 ID: {llm.pipeline.model.config._name_or_path}")

    # retriever = vector_db.as_retriever(search_kwargs={"k": 5})  # 반환할 청크 수를 5개로 설정
    retriever = vector_db.as_retriever()
    print("Retriever 생성 성공")

    prompt_template = PromptTemplate(
        template = template_input
        # template="Use the following context to answer the question:\n\nContext: {context}\n\nAnswer:"
    )

    combine_documents_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)

    chain = RetrievalQA(retriever=retriever, combine_documents_chain=combine_documents_chain)

    print("get_chain 함수 완료" + get_time())
    return chain, retriever, hf_pipeline


























