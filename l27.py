
from transformers import AutoTokenizer, AutoModelForCausalLM
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
    for i, vector in enumerate(stored_vectors):
        # 디버깅: 현재 계산 중인 벡터 확인
        print(f"벡터 {i + 1} 크기: {vector.shape}")
        
        # 코사인 유사도 계산
        similarity = cosine_similarity(
            np.array(question_vector).reshape(1, -1),
            vector.reshape(1, -1)
        )[0][0]
        
        # 키워드 보너스 계산
        keyword_bonus = sum([0.5 for keyword in keywords if keyword in text_chunks[i]])
        
        # 총 유사도 계산
        all_similarities_with_bonus.append(
            (i + 1, similarity + keyword_bonus)
        )

    # 유사도 순으로 정렬
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





from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

template_input="Use the following context to answer the question:\n\nContext: {context}\n\nAnswer:"
# template_input="답변은 질문과 관련된 정보를 중심으로 작성하며, 질문 속 키워드({keywords})를 강조하여 명확하고 구체적으로 설명하세요."



if "chain" not in st.session_state:
  st.session_state["chain"] = None
st.session_state["chain"], retriever, hf_pipeline = get_chain(vector_db, model, tokenizer, template_input)
chain = st.session_state["chain"]













# 질문 벡터 확인
question = "장기려가 뭐했냐?"  # 예시 질문
question_vector = embedding_model.embed_query(question)
print(f"질문 벡터: {question_vector}")





from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# retriever에서 검색된 문서와 관련된 유사도 계산
docs = retriever.get_relevant_documents(question)  # 질문과 관련된 문서들

if docs:
    question_vector = embedding_model.embed_query(question)   # 질문 벡터
    stored_vectors = vector_db.index.reconstruct_n(0, vector_db.index.ntotal)   # 벡터DB의 PDF 파일 벡터

        
    # 유사도 계산 (Cosine Similarity)
    similarities = [
        (doc.metadata['chunk_id'], cosine_similarity(np.array(question_vector).reshape(1, -1), np.array(stored_vectors[doc.metadata['chunk_id']]).reshape(1, -1))[0][0])
        for doc in docs
    ]

    # sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    sorted_similarities = calculate_similarity_with_keywords(question, vector_db, text_chunks, question_vector)


    for rank, (chunk_id, similarity) in enumerate(sorted_similarities, start=1):
        print(f"{rank}위 청크 {chunk_id}: 유사도 점수 {similarity:.4f}")


else:
    print("검색된 문서가 없습니다.")




chain_result = chain.run({"query": question})
answer = chain_result.split("Answer:", 1)[1].strip()
print(f"LangChain 답변: {answer} " + get_time())









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
