



import torch
import transformers
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



st.set_page_config(page_title="라마3", page_icon="🦙")


# pip install streamlit kiwipiepy -U langchain-community transformers torch scikit-learn pypdf faiss-cpu
# !pip install pyngrok streamlit pypdf faiss-cpu kiwipiepy -U langchain-community
# !ngrok authtoken 2pfBXJdvp34yPDeEAVXCrvFS2aD_5guh96guiVvtwcnmEsPo9

# from pyngrok import ngrok
# public_url = ngrok.connect(8501)  # 포트를 정수로 지정
# print(f"Public URL: {public_url}")

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


    if combo_chunk == "380":
      # 🔥 중복된 문장 제거
      sentences = answer.split('.')  # '.' 기준으로 문장을 나눔
      unique_sentences = []
      
      for sentence in sentences:
        sentence = sentence.strip()  # 공백 제거
        if sentence and sentence not in unique_sentences:
          unique_sentences.append(sentence)
      answer = '. '.join(unique_sentences)  # 중복 제거된 문장 합치기

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
def get_text_chunks_qa(text, chunk_size=380, overlap=100):
    print("qa")


    if isinstance(text, list):
      text = " ".join([doc.page_content for doc in text])
    print(text)
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
    
    print(7777777)
    print(chunks)
    
    chunk_documents = [
      Document(page_content=chunk, metadata={"chunk_id": idx})
      for idx, chunk in enumerate(chunks)
      ]
    
    chunks = chunk_documents
    return chunks



def get_text_chunks(text, chunk_size=380, overlap=100):
    print("no qa")

    # text가 Document 객체들의 리스트라면, 각 Document의 page_content를 하나의 문자열로 결합
    if isinstance(text, list):
        text = " ".join([doc.page_content for doc in text])
    
    chunks = []
    start = 0

    print(8888888)
    print(text)

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
    # model_path = "C:\\model\\llama3"
    
    print("토크나이저 로드 시작 " + get_time())
    tokenizer = AutoTokenizer.from_pretrained(model_name, subfolder=subfolder)
    print("토크나이저 로드 완료 " + get_time())

    # GPU가 사용 가능한지 확인
    if torch.cuda.is_available():
        device = torch.device("cuda")
        torch_dtype = torch.float16  # GPU에서는 FP16으로 VRAM 절약
        print("GPU가 감지되었습니다. GPU 환경에서 실행합니다.")
    else:
        device = torch.device("cpu")
        torch_dtype = torch.float32  # CPU에서는 FP32 사용
        print("GPU를 사용할 수 없습니다. CPU 환경에서 실행합니다.")
    

    print("모델 로드 시작 " + get_time())
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        subfolder=subfolder,
        # model_path,
        torch_dtype=torch_dtype
    ).to(device)
    
    print("모델 로드 완료 " + get_time())
    return tokenizer, model



if 'tokenizer' not in st.session_state:
    st.session_state['tokenizer'], st.session_state['model'] = load_model()
    print("토크나이저, 모델 로드 완료"+get_time())    


if "pipeline" not in st.session_state:
    print("라마3 모델 로드 시작   " + get_time())
    st.session_state["pipeline"] = transformers.pipeline(
        "text-generation",
        model=st.session_state["model"],
        tokenizer = st.session_state["tokenizer"],
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
    )
    st.session_state["pipeline"].model.eval()
    print("라마3 모델 로드 완료   " + get_time())





st.title(":red[NHIS]&nbsp;라마3 🦙 _챗봇_")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
  for chat_message in st.session_state["messages"]:
    st.chat_message(chat_message[0]).write(chat_message[1])



print("시작"+get_time())







with st.sidebar:
    uploaded_files = st.file_uploader("PDF 자료를 여기에 첨부하세요.", type=['pdf'], accept_multiple_files=True)
    process = st.button("첨부된 파일 등록")

    combo_chunk = st.sidebar.selectbox("청크 구분", ["380", "질문:"], index=0)  # 기본값 "380"

    if process:
        if len(uploaded_files) == 0:
            st.error("파일을 첨부하세요.")
        else:
            message_info = st.info("파일을 벡터 DB에 저장하고 있습니다.")

            pdf_text = get_pdf(uploaded_files)

            # combo_chunk = "질문:"   ###
            if combo_chunk == "질문:":
                text_chunks = get_text_chunks_qa(pdf_text, chunk_size=380, overlap=100)
            if combo_chunk == "380":
                text_chunks = get_text_chunks(pdf_text, chunk_size=380, overlap=100)
            
            print(8888888)
            print(text_chunks)

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



            message_info.empty()   # 저장이 완료되면 안내 메세지 삭제

            


            









question = st.chat_input("질문을 입력하세요.")
if question:
    if  len(uploaded_files) != 0:                # 첨부파일이 있으면, RAG
        st.chat_message("user").write(question + get_time_web())
        question_time = question + get_time_web()

        with st.spinner("RAG 답변 생성 중..."):
            print(7)
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

            print(f"LangChain 답변: {answer} " + get_time())
            st.chat_message("assistant").write(answer + get_time_web()) 


    if  len(uploaded_files) == 0:            # 첨부 파일이 없으면, 라마3 LLM이 답변
        st.chat_message("user").write(question + get_time_web())
        question_time = question + get_time_web()

        with st.spinner("라마3 모델이 답변 생성 중..."):
            answer = ask(question)
            st.chat_message("assistant").write(answer + get_time_web())

















    st.session_state["messages"].append(["user", question_time])
    st.session_state["messages"].append(["assistant", answer+get_time_web()])
    print("답변 완료"+get_time())



