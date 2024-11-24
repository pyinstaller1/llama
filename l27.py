
from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st
import os
from datetime import datetime
from langchain_llama3787 import *

# !pip install pyngrok streamlit pypdf faiss-gpu -U langchain-community



def get_time():
    now = datetime.now()
    return f"     [{now.hour}시{now.minute}분{now.second}초]"

def get_time_web():
    now = datetime.now()
    return f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[{now.hour}시{now.minute}분{now.second}초]"




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



@st.cache_resource  # Streamlit의 cache를 사용하여 한 번만 모델을 로드
def load_tokenizer():
    print("토크나이저 로드 시작"+get_time())
    model_name = "verygood7/llama3-ko-8b"
    subfolder = "snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    print("토크나이저 로드 완료"+get_time())
    return tokenizer
"""


"""
if 'tokenizer' not in st.session_state:
    # st.session_state['tokenizer'] = load_tokenizer()
    st.session_state['tokenizer'], st.session_state['model'] = load_model()
    print("토크나이저 로드 완료"+get_time())    
"""





"""

from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime


def get_time():
    now = datetime.now()
    return f"     [{now.hour}시{now.minute}분{now.second}초]"





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
    print("모델 로드 시작")
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
text_content = " ".join(doc.page_content for doc in pdf_text)  # Document 객체 리스트 -> 문자열 변환


# text_chunks = get_text_chunks(text_content, st.session_state['tokenizer'])
text_chunks = get_text_chunks(text_content, tokenizer)

vector_db = get_vector_db(text_chunks)



"""
for doc_id, doc in vector_db.docstore._dict.items():
    chunk_id = doc.metadata.get("chunk_id", "N/A")
    content = doc.page_content.replace('\n', ' ').replace('\r', ' ')
    split_content = '\n'.join([content[i:i+70] for i in range(0, len(content),70)])
    print(f"청크 {int(chunk_id)+1}:\n{split_content}\n")
"""


for doc_id, doc in vector_db.docstore._dict.items():
    chunk_id = doc.metadata.get("chunk_id", "N/A")
    content = doc.page_content[:38].replace('\n', ' ').replace('\r', ' ')
    print(f"청크 {int(chunk_id) + 1}: {content} ...")




from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)






# 질문 벡터 확인
question = "장기려가 뭐했냐?" # "건강보험이 뭐냐?"
question_vector = embedding_model.embed_query(question)
print(f"질문 벡터: {question_vector}")

# 청크 벡터 확인 (예: 첫 번째 청크)
stored_vectors = vector_db.index.reconstruct_n(0, 1)
# print(f"저장된 첫 번째 청크 벡터: {stored_vectors}")


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


question_vector_2d = np.array(question_vector).reshape(1, -1)   # 질문 벡터 (1D 배열을 2D로 변환)
stored_vectors = np.array(stored_vectors)  # 저장된 기존의 FAISS 벡터DB  (2D 배열)
similarities = cosine_similarity(question_vector_2d, stored_vectors) # 코사인 유사도 계산

print("유사도 점수:", similarities)




template_input="Use the following context to answer the question:\n\nContext: {context}\n\nAnswer:"

if "chain" not in st.session_state:
  st.session_state["chain"] = None
st.session_state["chain"], retriever, hf_pipeline = get_chain(vector_db, model, tokenizer, template_input)
chain = st.session_state["chain"]









# 질문에 대해 검색된 문서 가져오기
docs = retriever.get_relevant_documents(question)

stored_vectors = vector_db.index.reconstruct_n(0, vector_db.index.ntotal)

# 청크 4의 벡터와 질문 벡터 간 유사도 점수 계산
chunk_4_vector = stored_vectors[3]  # 청크 4는 0부터 시작하는 인덱스 기준 3
similarity_with_chunk_4 = cosine_similarity(
    np.array(question_vector).reshape(1, -1),
    np.array(chunk_4_vector).reshape(1, -1)
)[0][0]

print(f"청크 4와 질문 간 유사도 점수: {similarity_with_chunk_4:.4f}")


"""
if docs:
    # 저장된 모든 벡터 가져오기 (중복 방지)
    stored_vectors = vector_db.index.reconstruct_n(0, vector_db.index.ntotal)  # 2D 배열

    # 검색된 문서 순서대로 유사도 점수 계산
    for rank, doc in enumerate(docs, start=1):
        chunk_id = int(doc.metadata.get("chunk_id", -1))  # 청크 ID 가져오기
        content = doc.page_content[:38].replace("\n", " ").replace("\r", " ")  # 청크 내용 요약
        
        # 코사인 유사도 계산
        similarity_score = cosine_similarity(
            np.array(question_vector).reshape(1, -1),
            np.array(stored_vectors[chunk_id]).reshape(1, -1)
        )[0][0]

        # 순위와 유사도 점수 출력
        print(f"{rank}위 청크 {chunk_id + 1}: {content}, 유사도 점수: {similarity_score:.4f}")

    # 검색된 청크 번호 확인
    chunk_ids = [int(doc.metadata["chunk_id"]) + 1 for doc in docs if "chunk_id" in doc.metadata]
    print(f"선택된 청크 번호: {chunk_ids}")
"""

if docs:
    # 검색된 문서의 ID와 내용을 출력
    print("\n[검색된 청크들]")
    for doc in docs:
        print(f"청크 ID: {int(doc.metadata.get('chunk_id')) + 1}, 내용: {doc.page_content[:50]}...")  # ID에 +1 적용

    # 모든 저장된 벡터 가져오기
    stored_vectors = vector_db.index.reconstruct_n(0, vector_db.index.ntotal)

    # 모든 청크의 유사도 계산
    all_similarities = [
        (i + 1, cosine_similarity(np.array(question_vector).reshape(1, -1), stored_vectors[i].reshape(1, -1))[0][0])  # ID +1 적용
        for i in range(len(stored_vectors))
    ]

    # 유사도 순으로 정렬하여 출력
    sorted_similarities = sorted(all_similarities, key=lambda x: x[1], reverse=True)
    print("\n[유사도 순 정렬된 청크]")
    for rank, (chunk_id, similarity) in enumerate(sorted_similarities[:10], start=1):  # 상위 10개만
        print(f"{rank}위 청크 {chunk_id}: 유사도 점수 {similarity:.4f}")  # ID에 이미 +1 적용됨










# 체인이 요구하는 입력 키 확인
print(f"체인이 요구하는 입력 키: {chain.input_keys}")

chain_result = chain.run({"query": question})

answer = chain_result.split("Answer:", 1)[1].strip()
print(f"LangChain 답변: {answer} " + get_time())


# Hugging Face 파이프라인 직접 호출
hf_pipeline_result = hf_pipeline(question, max_length=512, num_return_sequences=1)
print(f"Hugging Face 파이프라인 답변: {hf_pipeline_result[0]['generated_text']} {get_time()}")

print("답변 완료"+get_time())


















"""

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

"""           
