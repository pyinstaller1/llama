
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import streamlit as st
import os
from datetime import datetime
from langchain_llama3 import *

# !pip install pyngrok streamlit pypdf faiss-gpu kiwipiepy -U langchain-community



def get_time():
    now = datetime.now()
    return f"     [{now.hour}시{now.minute}분{now.second}초]"

def get_time_web():
    now = datetime.now()
    return f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[{now.hour}시{now.minute}분{now.second}초]"








from kiwipiepy import Kiwi

kiwi = Kiwi()
stopwords = ['하다', '있다', '되다', '가', '이', '를', '은', '는', '다', '요', '죠']

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 질문에 대한 키워드 추출
def extract_keywords(question):
    keywords = [
        token.form
        for token in kiwi.tokenize(question)
        if token.tag in ['NNG', 'NNP', 'VV', 'NP', 'MAG']   # 명사, 동사, 대명사, 부사
    ]
    filtered_keywords = [word for word in keywords if word not in stopwords]  # 불용어 제거
    return filtered_keywords





from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 키워드 및 유사도 계산 함수
def calculate_similarity_with_keywords(question, vector_db, text_chunks, question_vector):
    # 키워드 추출
    keywords = extract_keywords(question)

    # 모든 벡터 가져오기
    stored_vectors = np.array([
        vector_db.index.reconstruct(i) for i in range(vector_db.index.ntotal)
    ])
    
    # 디버깅: 벡터 모양 확인
    print(f"질문 벡터 크기: {np.array(question_vector).shape}")
    print(f"저장된 벡터 크기: {stored_vectors.shape}")

    # 유사도 계산
    all_similarities_with_bonus = []
    for i, vector in enumerate(stored_vectors):  # 🔥 enumerate 사용
        # 디버깅: 현재 계산 중인 벡터 확인
        print(f"벡터 {i} 크기: {vector.shape}")
        
        # 코사인 유사도 계산
        similarity = cosine_similarity(
            np.array(question_vector).reshape(1, -1),
            vector.reshape(1, -1)
        )[0][0]
        
        # 키워드 보너스 계산
        keyword_bonus = sum([0.5 for keyword in keywords if keyword in text_chunks[i]])
        
        # 🔥 i 그대로 사용
        all_similarities_with_bonus.append(
            (i, similarity + keyword_bonus)  # i는 0부터 시작, 나중에 출력할 때 +1 적용
        )

    # 유사도 순으로 정렬
    sorted_similarities = sorted(all_similarities_with_bonus, key=lambda x: x[1], reverse=True)
    return sorted_similarities


# 🔥 유사도 계산 후 출력 부분
sorted_similarities = calculate_similarity_with_keywords(question, vector_db, text_chunks, question_vector)

# 🔥 청크 ID를 1부터 9로 표시하기 위해 i + 1을 추가합니다.
for rank, (chunk_id, similarity) in enumerate(sorted_similarities, start=1):
    print(f"{rank}위 청크 {chunk_id + 1}: 유사도 점수 {similarity:.4f}")  # 🔥 chunk_id + 1

# 🔥 상위 4개 청크를 선택합니다. (1~9로 표시되도록 변경)
top_chunks = [chunk_id + 1 for chunk_id, _ in sorted_similarities[:4]]  # 🔥 chunk_id + 1
print(f"💎 선택된 청크 ID: {top_chunks}")

# 🔥 chunk_id와 UUID 매핑을 표시할 때 1부터 시작하는 인덱스로 표시합니다.
chunk_id_to_uuid = {i + 1: doc_id for i, doc_id in enumerate(vector_db.docstore._dict.keys())}
print(f"📘 chunk_id_to_uuid 매핑: {chunk_id_to_uuid}")



























"""
@st.cache_resource  # Streamlit의 cache를 사용하여 한 번만 모델을 로드
def load_tokenizer():
    print("토크나이저 로드 시작"+get_time())
    model_name = "verygood7/llama3-ko-8b"
    subfolder = "snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    print("토크나이저 로드 완료"+get_time())
    return tokenizer
"""



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
    print("토크나이저 로드 완료"+get_time())    






"""


def get_time():
    now = datetime.now()
    return f"     [{now.hour}시{now.minute}분{now.second}초]"



from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime






if "tokenizer" in globals():
    del globals()["tokenizer"]
if "model" in globals():
    del globals()["model"]

# 또는 __builtins__에서 삭제
if hasattr(__builtins__, "tokenizer"):
    del __builtins__.tokenizer
if hasattr(__builtins__, "model"):
    del __builtins__.model

print("기존 모델과 토크나이저 삭제 완료")

if "get_chain" in globals():
    del globals()["get_chain"]
print("기존 get_chain 함수 삭제 완료")











# 모델 로드 및 전역 변수 정의
if "tokenizer" not in globals() or "model" not in globals():
    print("모델 로드 시작" + get_time())
    model_name = "verygood7/llama3-ko-8b"
    subfolder = "snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"

    # 토크나이저 및 모델 로드
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    model = AutoModelForCausalLM.from_pretrained(model_name, subfolder=subfolder)

    # 최상위 전역 변수로 등록
    __builtins__.tokenizer = tokenizer
    __builtins__.model = model

    print("모델 로드 완료" + get_time())
else:
    print("이미 로드된 모델 사용")

"""





"""

print("모델 로드 시작")
model = st.session_state["model"]
print("토크나이저 로드 시작")
tokenizer = st.session_state["tokenizer"]
print("모델과 토크나이저를 성공적으로 가져왔습니다." + get_time())
"""
















from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

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

    retriever = vector_db.as_retriever()   # as_retriever(search_kwargs={"k": 5})   청크5개

    prompt_template = PromptTemplate(
        template="Use the following context to answer the question:\n\nContext: {context}\n\n Answer:"
        )

    combine_documents_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)
    chain = RetrievalQA(retriever=retriever, combine_documents_chain=combine_documents_chain)

    print("get_chain 함수 완료" + get_time())
    return chain, retriever












from io import BytesIO

# Streamlit의 UploadedFile과 동일한 구조를 모방한 클래스
class UploadedFile:
    def __init__(self, name, content):
        self.name = name  # 파일 이름
        self.content = content  # 파일 내용 (바이너리 데이터)

    def read(self):
        """Streamlit의 UploadedFile처럼 바이너리 데이터를 반환"""
        return self.content

uploaded_files = [
    UploadedFile(
        name="건강보험자료.pdf",
        content=open("./건강보험자료.pdf", "rb").read()
    )
]
















pdf_text = get_pdf(uploaded_files)
# text_content = " ".join(doc.page_content for doc in pdf_text)  # Document 객체 리스트 -> 문자열 변환



from langchain.schema import Document  # Document 클래스 추가

text_content = [Document(page_content=doc.page_content, metadata={"source": "pdf", "page_number": idx}) 
                for idx, doc in enumerate(pdf_text)]



text_chunks = get_text_chunks(text_content, st.session_state['tokenizer'])
# text_chunks = get_text_chunks(text_content, tokenizer)
vector_db = get_vector_db(text_chunks)

for doc_id, doc in vector_db.docstore._dict.items():
    chunk_id = doc.metadata.get("chunk_id", "N/A")
    content = doc.page_content[:38].replace('\n', ' ').replace('\r', ' ')
    print(f"청크 {int(chunk_id) + 1}: {content} ...")






from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

template_input="Use the following context to answer the question:\n\nContext: {context}\n\nAnswer:"
# template_input="답변은 질문과 관련된 정보를 중심으로 작성하며, 질문 속 키워드({keywords})를 강조하여 명확하고 구체적으로 설명하세요."


# st.session_state["model"] = model
# st.session_state["tokenizer"] = tokenizer

if "chain" not in st.session_state:
  st.session_state["chain"] = None
st.session_state["chain"], retriever = get_chain(vector_db)
chain = st.session_state["chain"]










from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)



# 🔥 질문을 정의합니다.
question = "장기려가 뭐했냐?"  # 예시 질문

# 🔥 질문 벡터를 생성합니다.
question_vector = embedding_model.embed_query(question)  # 🔥 질문 벡터 생성

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# 🔥 retriever에서 검색된 문서와 관련된 유사도 계산
docs = retriever.get_relevant_documents(question)  # 질문과 관련된 문서들

if docs:
    # 🔥 1️⃣ 질문 벡터 생성 (중복 제거)
    stored_vectors = vector_db.index.reconstruct_n(0, vector_db.index.ntotal)   # 벡터DB의 PDF 파일 벡터

    # 🔥 2️⃣ 유사도 계산 (Cosine Similarity)
    similarities = [
        (doc.metadata.get('chunk_id'), cosine_similarity(
            np.array(question_vector).reshape(1, -1), 
            np.array(stored_vectors[doc.metadata.get('chunk_id', 0)]).reshape(1, -1)
        )[0][0]) 
        for doc in docs if doc.metadata.get('chunk_id') is not None
    ]

    # 🔥 3️⃣ 청크와 유사도 정렬

    question = "장기려가 뭐했냐?"
    sorted_similarities = calculate_similarity_with_keywords(question, vector_db, text_chunks, question_vector)

    for rank, (chunk_id, similarity) in enumerate(sorted_similarities, start=1):
        print(f"{rank}위 청크 {chunk_id + 1}: 유사도 점수 {similarity:.4f}")  # 🔥 chunk_id + 1로 1부터 시작

    # 🔥 4️⃣ 상위 4개 청크 선택
    top_chunks = [chunk_id for chunk_id, similarity in sorted_similarities[:4] if chunk_id < len(stored_vectors)]  # 상위 4개 청크 선택
    print(f"💎 선택된 청크 ID: {[chunk_id + 1 for chunk_id in top_chunks]}")  # 🔥 1부터 시작

    # 📚 5️⃣ vector_db에 저장된 모든 키 확인
    print(f"📚 vector_db에 저장된 키: {list(vector_db.docstore._dict.keys())}")

    # 📘 6️⃣ chunk_id와 UUID 키의 매핑 테이블 생성
    chunk_id_to_uuid = {}

    for key, doc in vector_db.docstore._dict.items():
        if 'chunk_id' in doc.metadata:
            chunk_id = int(doc.metadata['chunk_id'])  # 🔥 chunk_id가 문자열일 수 있으므로 int로 변환
            chunk_id_to_uuid[chunk_id] = key  # chunk_id -> UUID 매핑
        else:
            print(f"⚠️ 'chunk_id'가 문서에 없습니다. key: {key}, metadata: {doc.metadata}")

    print(f"📘 chunk_id_to_uuid 매핑: {chunk_id_to_uuid}")

    # 🔥 7️⃣ retriever의 문서 목록을 우리가 선택한 청크로 교체
    try:
        docs = []
        for chunk_id in top_chunks:
            if chunk_id in chunk_id_to_uuid:
                # 🔥 매핑된 UUID로 docstore에서 문서 가져오기
                uuid_key = chunk_id_to_uuid[chunk_id]
                docs.append(vector_db.docstore._dict[uuid_key])
            else:
                print(f"❌ KeyError: chunk_id '{chunk_id + 1}'에 해당하는 키가 vector_db에 없습니다.")
    except KeyError as e:
        print(f"❌ KeyError: {e}. 🔍 다시 확인해야 합니다.")
        print(f"🔍 가능한 키 목록: {list(vector_db.docstore._dict.keys())}")
else:
    print("⚠️ 검색된 문서가 없습니다.")

# 🔥 chain.run으로 최종 답변 생성
chain_result = st.session_state["chain"].run({
    "query": question
})

if 'result' in chain_result and "Answer:" in chain_result['result']:
    answer = chain_result['result'].split("Answer:", 1)[1].strip()
else:
    answer = chain_result.get('result', '답변을 가져오지 못했습니다.').strip()

print(f"LangChain 답변: {answer} " + get_time())
print("답변 완료" + get_time())








