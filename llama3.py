from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime

def get_time():
    return str("   [" + datetime.now().strftime("%H:%M:%S") + "]")

# 모델과 토크나이저 로드
print("시작"+get_time())
model_name = "/content/llama/snapshots/10acb1aa4f341f2d3c899d78c520b0822a909b95"
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("토크나이저 완료"+get_time())
model = AutoModelForCausalLM.from_pretrained(model_name)
print("모델 완료"+get_time())

# 질문 입력
question = "프랑스의 수도는?"

# 입력 텍스트를 토큰화하고 모델에 입력
inputs = tokenizer.encode(question, return_tensors="pt")
print("엔코딩 input 완료"+get_time())

outputs = model.generate(inputs, max_length=50)
print("생성 output 완료"+get_time())

# 답변 출력
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("디코딩 answer 완료"+get_time())
print(answer)





















