
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



# 🔥 키워드 추출 함수
def extract_keywords(question):
    keywords = [
        token.form for token in kiwi.tokenize(question)
        if token.tag in ['NNG', 'NNP', 'VV', 'SL']  # 명사, 고유명사, 외래어, 동사
    ]
    filtered_keywords = [word for word in keywords if word not in stopwords]
    return filtered_keywords




from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity_with_keywords(question, vector_db, text_chunks, question_vector):
    # 🔥 키워드 추출 및 불필요한 키워드 필터링
    stopwords = ['하다', '있다', '되다', '가', '이', '를', '은', '는', '다', '요', '죠', '하']  # 🔥 '하' 추가
    keywords = extract_keywords(question)
    keywords = [kw for kw in keywords if kw not in stopwords and len(kw) > 1]  # 🔥 1글자 키워드 제거
    print(f"질문 키워드: {keywords}")
    
    stored_vectors = np.array([vector_db.index.reconstruct(i) for i in range(vector_db.index.ntotal)])
    
    all_similarities_with_bonus = []
    for i, vector in enumerate(stored_vectors):
        similarity = cosine_similarity(np.array(question_vector).reshape(1, -1), vector.reshape(1, -1))[0][0]
        
        # 🔥 청크 내 공백 제거 및 키워드 매칭
        clean_chunk = text_chunks[i].page_content.replace('\n', '').replace('\r', '').replace(' ', '')
        
        # 🔥 키워드 보너스 강화 (보너스의 크기를 더 높게 조정)
        keyword_bonus = sum([(clean_chunk.count(keyword) + 2) * 200 for keyword in keywords if keyword in clean_chunk])  # 🔥 보너스 강화
        
        # 🔥 유사도와 키워드 가중치 조정
        weighted_similarity = 0.2 * similarity + 0.8 * keyword_bonus  # 🔥 코사인 유사도 비중을 0.2로 증가
        
        all_similarities_with_bonus.append((i, weighted_similarity))
        
        # 🔥 청크의 키워드 매칭 정보 출력
        print(f"청크 {i+1}: 유사도 점수={similarity:.4f}, 키워드 보너스={keyword_bonus}, 총 점수={weighted_similarity:.4f}")
    
    # 🔥 유사도에 따라 정렬
    sorted_similarities = sorted(all_similarities_with_bonus, key=lambda x: x[1], reverse=True)
    return sorted_similarities






























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











import re

def clean_answer(answer):
    """
    Answer 부분의 불필요한 [Your Website], [Your Blog] 같은 부분을 제거하고
    중복된 공백을 정리하는 함수.
    """
    # 🔥 Answer: 이후의 텍스트만 추출
    if "Answer:" in answer:
        answer = answer.split("Answer:", 1)[1].strip()

    # 🔥 정규 표현식으로 [Your Website] 같은 불필요한 부분 제거
    answer = re.sub(r'\[.*?\]', '', answer)  # 🔥 대괄호 [ ] 안의 모든 내용 제거

    # 🔥 불필요한 줄바꿈과 공백 정리
    answer = re.sub(r'\s+', ' ', answer)  # 🔥 여러 개의 공백, 줄바꿈을 하나로 통합
    return answer.strip()


def update_chain_with_top_chunks(top_chunks, text_chunks):
    """retriever와 chain을 업데이트하고 새로운 chain으로 교체"""
    # 🔥 update_retriever_with_top_chunks 함수로 retriever 생성
    retriever = update_retriever_with_top_chunks(top_chunks, vector_db, text_chunks)
    
    # 🔥 새로운 chain 생성
    chain, _ = get_chain(retriever)  # 🔥 새로운 chain 생성 (1번만 호출)
    st.session_state["chain"] = chain  # 🔥 새로운 체인을 세션에 반영
    
    print(f"🔄 새로운 chain이 생성되었습니다.")
    return chain



def get_top_context_from_chunks(top_chunk_ids, text_chunks, top_score, second_score):
    """1위 청크의 전체 내용을 포함하고, 나머지 청크는 요약하여 반환"""
    from kiwipiepy import Kiwi
    kiwi = Kiwi()

    context_parts = []

    # 🔥 1위 청크의 내용 추가
    top_chunk_id = top_chunk_ids[0]  # 1위 청크
    top_chunk_text = text_chunks[top_chunk_id].page_content
    context_parts.append(f"가장 중요한 참고 문서:\n{top_chunk_text}\n")

    # 🔥 1위와 2위의 점수 차이가 클 경우, 1위만 자세히 참조
    if top_score > second_score * 2:  # 1위 점수가 2위의 2배 이상이면
        print(f"⚠️ 1위 청크의 점수가 2위보다 2배 높음. 1위 청크만 참조합니다.")
        return "\n".join(context_parts)  # 🔥 1위 청크만 반환

    # 🔥 나머지 2~4위 청크의 요약 추가
    for chunk_id in top_chunk_ids[1:]:
        chunk_text = text_chunks[chunk_id].page_content
        sentences = chunk_text.split('.')

        # 🔥 키워드 필터링으로 중요한 문장만 추출
        relevant_sentences = [sentence for sentence in sentences if len(sentence) > 10]  # 간단한 필터
        context_parts.append(f"참고 문서 요약 (청크 {chunk_id + 1}):\n" + " ".join(relevant_sentences[:2]) + "\n")

    return "\n".join(context_parts)




def update_retriever_with_top_chunks(top_chunk_ids, vector_db, text_chunks):
    """선택된 청크로 새로운 vector_db 및 retriever 생성"""
    from langchain.vectorstores import FAISS
    from langchain.schema import Document

    # 🔥 선택된 청크의 내용을 추출
    selected_documents = [text_chunks[i] for i in top_chunk_ids]  # 🔥 상위 청크만 선택
    chunk_documents = [
        Document(page_content=doc.page_content, metadata={"chunk_id": idx}) 
        for idx, doc in enumerate(selected_documents)
    ]

    # 🔥 새로운 vector_db 생성 (상위 청크로만 생성)
    embeddings = load_embeddings()
    new_vector_db = FAISS.from_documents(chunk_documents, embeddings)  # 🔥 새로운 vector_db 생성
    
    # 🔥 retriever를 new_vector_db로 직접 사용
    retriever = new_vector_db  # 🔥 new_vector_db는 이미 retriever로 사용 가능

    print(f"🔄 새로운 retriever가 {len(top_chunk_ids)}개의 청크로 업데이트 되었습니다.")
    return retriever  # 🔥 retriever만 반환












# 🔥 청크 유사도 계산
sorted_similarities = calculate_similarity_with_keywords(question, vector_db, text_chunks, question_vector)

# 🔥 상위 4개 청크 선택
top_chunks = [chunk_id for chunk_id, _ in sorted_similarities[:4]]
top_scores = [score for _, score in sorted_similarities[:4]]  # 🔥 각 청크의 유사도 점수 추출

# 🔥 새로운 retriever와 chain 생성
update_chain_with_top_chunks(top_chunks, text_chunks)

# 🔥 상위 청크의 컨텍스트 생성 (중요한 문장만 추출)
keywords = extract_keywords(question)
context = get_top_context_from_chunks(top_chunks, text_chunks, top_scores[0], top_scores[1])  # 🔥 점수 추가

# 🔥 LLM에 질문을 명확히 전달하기 위한 프롬프트 생성
prompt = f"""
아래의 문서를 바탕으로 사용자의 질문에 대한 명확하고 구체적인 답변을 작성하십시오.

{context}

질문: {question}

답변: 
"""

# 🔥 chain.run으로 최종 답변 생성
chain_result = st.session_state["chain"].run({"query": prompt})

# 🔥 결과가 문자열일 경우 바로 사용, 그렇지 않으면 딕셔너리로 접근
if isinstance(chain_result, str):
    answer = chain_result.strip()
else:
    answer = chain_result.get('result', '답변을 가져오지 못했습니다.').strip()

# 🔥 불필요한 텍스트 제거
cleaned_answer = clean_answer(answer)

print(f"LangChain 답변: {cleaned_answer} " + get_time())
print("답변 완료" + get_time())



