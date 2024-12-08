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
    chunks = text_splitter.split_documents(text)
    return chunks







# @st.cache_resource  # 한 번만 로드하여 캐싱
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="jhgan/ko-sroberta-multitask",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )



def get_vector_db(text_chunks):

    text_chunks = [chunk.page_content for chunk in text_chunks]

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

def get_chain8(vector_db):
    print("get_chain 함수 시작" + get_time())

    hf_pipeline = pipeline(
        "text-generation",
        model=st.session_state["model"],
        tokenizer=st.session_state["tokenizer"],
        device=0,
        framework="pt",
        return_text=True
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    retriever = vector_db.as_retriever()   # as_retriever(search_kwargs={"k": 5})   청크5개


    prompt_template = PromptTemplate(
        template="Use the following context to answer the question:\n\nContext: {context}\n\n Answer:"
        )




    



    combine_documents_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)
    chain = RetrievalQA(retriever=retriever, combine_documents_chain=combine_documents_chain)

    print("get_chain 함수 완료" + get_time())
    return chain, retriever

















def ask(x, context='', is_input_full=False):
    print(x)
    print(get_time())

    PROMPT = '''You are a helpful AI assistant. Please answer the user's questions kindly. 당신은 유능한 AI 어시스턴트 입니다. 사용자의 질문에 대해 친절하게 답변해주세요.'''
    instruction = x

    messages = [
        {"role": "system", "content": f"{PROMPT}"},
        {"role": "user", "content": f"{instruction}"}
        ]

    prompt = st.session_state["pipeline"].tokenizer.apply_chat_template(
            messages, 
            tokenize=False, 
            add_generation_prompt=True
    )

    print(prompt)

    print("질문 데이터 생성 완료   " + get_time())


    terminators = [
        st.session_state["pipeline"].tokenizer.eos_token_id,
        st.session_state["pipeline"].tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]


    print("답변 생성 시작   " + get_time())
    outputs = st.session_state["pipeline"](
        prompt,
        max_new_tokens=2048,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9
    )

    print(outputs[0]["generated_text"][len(prompt):])
    print("답변 생성 완료   " + get_time())
    return outputs[0]["generated_text"][len(prompt):]













