


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import streamlit as st
from datetime import datetime
from kiwipiepy import Kiwi
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS

from langchain_llama3 import *

# !pip install pyngrok streamlit pypdf faiss-gpu kiwipiepy -U langchain-community

# combo_chunk = "질문:"
combo_chunk = "380"


def get_time():
    now = datetime.now()
    return f"     [{now.hour}시{now.minute}분{now.second}초]"

def get_time_web():
    now = datetime.now()
    return f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[{now.hour}시{now.minute}분{now.second}초]"





kiwi = Kiwi()
stopwords = ['하다', '있다', '되다', '가', '이', '를', '은', '는', '다', '요', '죠']

def extract_keywords(question):
    keywords = [
        token.form for token in kiwi.tokenize(question)
        if token.tag in ['NNG', 'NNP', 'VV', 'SL']  # 명사, 고유명사, 외래어, 동사
    ]
    filtered_keywords = [word for word in keywords if word not in stopwords]
    return filtered_keywords

def calculate_similarity_with_keywords(question, vector_db, text_chunks):
    # 🔥 키워드 추출 및 불필요한 키워드 필터링
    stopwords = ['하다', '있다', '되다', '가', '이', '를', '은', '는', '다', '요', '죠', '하']  # 🔥 '하' 추가
    keywords = extract_keywords(question)
    keywords = [kw for kw in keywords if kw not in stopwords and len(kw) > 1]  # 🔥 1글자 키워드 제거
    print(f"질문 키워드: {keywords}")
    
    stored_vectors = np.array([vector_db.index.reconstruct(i) for i in range(vector_db.index.ntotal)])

    embedding_model = HuggingFaceEmbeddings(
      model_name="jhgan/ko-sroberta-multitask",
      model_kwargs={'device': 'cpu'},
      encode_kwargs={'normalize_embeddings': True}
    )

    question_vector = embedding_model.embed_query(question)
    
    all_similarities_with_bonus = []
    for i, vector in enumerate(stored_vectors):
        similarity = cosine_similarity(np.array(question_vector).reshape(1, -1), vector.reshape(1, -1))[0][0]
        
        # 🔥 청크 내 공백 제거 및 키워드 매칭
        clean_chunk = text_chunks[i].page_content.replace('\n', '').replace('\r', '').replace(' ', '')
        
        # 🔥 키워드 보너스 강화
        keyword_bonus = sum([(clean_chunk.count(keyword) + 2) * 1000 for keyword in keywords if keyword in clean_chunk])  # 🔥 보너스 강화
        weighted_similarity = similarity + keyword_bonus
        all_similarities_with_bonus.append((i, weighted_similarity))
        
        # 🔥 청크의 키워드 매칭 정보 출력
        print(f"청크 {i+1}: 유사도 점수={similarity:.4f}, 키워드 보너스={keyword_bonus}, 총 점수={weighted_similarity:.4f}")
    
    # 🔥 유사도에 따라 정렬
    sorted_similarities = sorted(all_similarities_with_bonus, key=lambda x: x[1], reverse=True)
    return sorted_similarities






def clean_answer(answer):
    # 🔥 "Answer:" 이후 텍스트만 추출
    answer = answer.split("Answer:", 1)[-1].strip() if "Answer:" in answer else answer


    # 🔥 'Note:', 'Context:', 'Key word:' 뒤의 모든 내용 제거
    patterns_to_remove = ['Note:', 'Context:', 'Key word:', 'Translation:', 'Explanation:']
    for pattern in patterns_to_remove:
        if pattern in answer:
            answer = answer.split(pattern, 1)[0].strip()

    return answer




def get_chain(vector_db):
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

    # combo_chunk = "질문:"   ### 380 pdf 에서 1위 점수차가 2배 이상이면 1개, 아니면 2개
    if combo_chunk == "질문:":
      retriever = vector_db.as_retriever(search_kwargs={"k": 1})
    if combo_chunk == "380":
      retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    prompt_template = PromptTemplate(
        template="Answer should be Korean. Avoid repeat of similar sentences. Use the following context to answer the question.:\n\nContext: {context}\n\n Answer:"
        )

    combine_documents_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)
    chain = RetrievalQA(retriever=retriever, combine_documents_chain=combine_documents_chain)

    print("get_chain 함수 완료" + get_time())
    return chain


# 텍스트를 청크로 분리
def get_text_chunks_question(text, chunk_size=380, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        if "질문:" in text[start:]:
            question_start = text.find("질문:", start)
            answer_end = text.find("질문:", question_start + 1)  # 다음 '질문:' 위치 찾기

            # 답변의 끝이 있다면, '질문: ~ 답변:' 구간을 하나의 청크로 저장
            if question_start != -1 and answer_end != -1:
                chunk = text[question_start:answer_end].strip()
                chunks.append(chunk)
                start = answer_end  # 다음 질문으로 넘어가도록
            else:
                # 마지막 질문/답변이 끝까지 포함되도록 처리
                chunk = text[question_start:].strip()
                chunks.append(chunk)
                break
        else:
            break
    
    chunk_documents = [
      Document(page_content=chunk, metadata={"chunk_id": idx})
      for idx, chunk in enumerate(chunks)
      ]
    
    chunks = chunk_documents
    return chunks



def get_text_chunks(text, chunk_size=380, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        # 현재 청크의 끝 인덱스 계산
        end = start + chunk_size
        
        # 청크 저장 (현재 범위의 텍스트)
        chunk = text[start:end].strip()
        chunks.append(chunk)

        # 다음 청크의 시작 위치로 이동 (오버랩 적용)
        start = end - overlap

    # LangChain Document 형식으로 변환
    chunk_documents = [
        Document(page_content=chunk, metadata={"chunk_id": idx})
        for idx, chunk in enumerate(chunks)
    ]

    return chunk_documents



def get_new_chain(top_chunk_ids, text_chunks):
    new_vector_db = get_new_vectcor_db(top_chunk_ids, st.session_state["vector_db"], st.session_state["text_chunks"])    
    st.session_state["chain"] = get_chain(new_vector_db)  # 🔥 새로운 chain 생성
    print(f"🔄 새로운 chain이 생성되었습니다.")
    return st.session_state["chain"]

def get_new_vectcor_db(top_chunk_ids, vector_db, text_chunks):

    selected_documents = [text_chunks[i] for i in top_chunk_ids]  # 🔥 상위 청크만 선택
    chunk_documents = [
        Document(page_content=doc.page_content, metadata={"chunk_id": idx}) 
        for idx, doc in enumerate(selected_documents)
    ]

    embeddings = load_embeddings()
    new_vector_db = FAISS.from_documents(chunk_documents, embeddings)  # 🔥 새로운 vector_db 생성
    
    print(f"🔄 새로운 vector_db가 {len(top_chunk_ids)}개의 청크로 생성 되었습니다.")
    return new_vector_db











@st.cache_resource  # Streamlit의 cache를 사용하여 한 번만 모델을 로드
def load_model():
    model_name = "verygood7/llama3-ko-8b"
    subfolder = "snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"
    print("토크나이저 로드 시작"+get_time())
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    print("토크나이저 로드 완료"+get_time())
    model = AutoModelForCausalLM.from_pretrained(model_name, subfolder=subfolder)
    print("모델 로드 완료"+get_time())
    return tokenizer, model


if 'tokenizer' not in st.session_state:
    # st.session_state['tokenizer'] = load_tokenizer()
    st.session_state['tokenizer'], st.session_state['model'] = load_model()
    print("토크나이저, 모델 로드 완료"+get_time())    










# 텍스트 파일 읽기
with open('건강보험자료.txt', 'r', encoding='utf-8') as f:
    pdf_text = f.read()

# combo_chunk = "질문:"   ###
if combo_chunk == "질문:":
  text_chunks = get_text_chunks_question(pdf_text, chunk_size=380, overlap=100)
if combo_chunk == "380":
  text_chunks = get_text_chunks(pdf_text, chunk_size=380, overlap=100)

vector_db = get_vector_db(text_chunks)

for doc_id, doc in vector_db.docstore._dict.items():
    chunk_id = doc.metadata.get("chunk_id", "N/A")
    content = doc.page_content[:38].replace('\n', ' ').replace('\r', ' ')
    print(f"청크 {int(chunk_id) + 1}: {content} ...")

if "chain" not in st.session_state:
  st.session_state["chain"] = None
st.session_state["chain"] = get_chain(vector_db)

if "vector_db" not in st.session_state:
  st.session_state["vector_db"] = None
st.session_state["vector_db"] = vector_db
if "text_chunks" not in st.session_state:
  st.session_state["text_chunks"] = None
st.session_state["text_chunks"] = text_chunks









question = "장기려가 뭐했냐?"  # 예시 질문
# question = "직장가입자 건강보험증 발송은 어디로 하나요?"

sorted_similarities = calculate_similarity_with_keywords(question, st.session_state["vector_db"], st.session_state["text_chunks"])   # 질문과 벡터DB 청크의 유사도 계산

top_scores = [score for _, score in sorted_similarities[:2]]
if len(top_scores) >= 2:
  if top_scores[0] >= 2 * top_scores[1]:
    top_chunk_ids = [chunk_id+1 for chunk_id, _ in sorted_similarities[:1]]   # 상위 1개 청크 선택
  else:
    top_chunk_ids = [chunk_id+1 for chunk_id, _ in sorted_similarities[:2]]   # 상위 2개 청크 선택
else:
  top_chunk_ids = [chunk_id+1 for chunk_id, _ in sorted_similarities[:1]]   # 상위 1개 청크 선택

print(top_chunk_ids)
get_new_chain(top_chunk_ids, st.session_state["text_chunks"])
chain_result = st.session_state["chain"].run({"query": question})

answer = clean_answer(chain_result.strip())

print(f"LangChain 답변: {answer} " + get_time())
print("답변 완료" + get_time())




