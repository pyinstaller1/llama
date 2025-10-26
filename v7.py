import subprocess
from datetime import datetime

# 실행할 명령어와 인자들
exe_path = r"D:\model\llama.cpp\build\bin\Release\llama-run.exe"
model_path = r"D:\model\llama-3-Korean-Bllossom-8B-Q4_K_M.gguf"
# prompt = r'<s>[INST] What is health insurance? Please answer within Korean 100 words. [/INST]'
prompt = r"<s>[INST] Here is the error data for the last 6 months:\nMonth 1: A=8, B=4, C=6\nMonth 2: A=9, B=5, C=7\nMonth 3: A=10, B=4, C=6\nMonth 4: A=11, B=6, C=7\nMonth 5: A=10, B=5, C=8\nMonth 6: A=12, B=6, C=8\nBased on this data:\n1. Identify any trends or patterns for A, B, and C.\n2. Predict the number of errors for each of them for next month.\n3. Provide a brief reasoning for your predictions (considering trends, small fluctuations, or growth rates).\n4. Do not simply repeat the last month's values; try to estimate a realistic next-month number based on the pattern. Finally, indicate which of A, B, or C is most likely to have the highest number of errors next month. Answer in Korean. [/INST]"



'''
D:\model\llama.cpp\build\bin\Release\llama-run.exe D:\model\llama-3-Korean-Bllossom-8B-Q4_K_M.gguf "<s>[INST] Here is the error data for the last 6 months:\nMonth 1: A=8, B=4, C=6\nMonth 2: A=9, B=5, C=7\nMonth 3: A=10, B=4, C=6\nMonth 4: A=11, B=6, C=7\nMonth 5: A=10, B=5, C=8\nMonth 6: A=12, B=6, C=8\nBased on this data:\n1. Identify any trends or patterns for A, B, and C.\n2. Predict the number of errors for each of them for next month.\n3. Provide a brief reasoning for your predictions (considering trends, small fluctuations, or growth rates).\n4. Do not simply repeat the last month's values; try to estimate a realistic next-month number based on the pattern. Finally, indicate which of A, B, or C is most likely to have the highest number of errors next month. Answer in Korean. [/INST]"

'''


print(datetime.now())

time_start = datetime.now()

# subprocess 실행
'''
process = subprocess.run(
    [exe_path, model_path, prompt],
    capture_output=True,      # 결과를 변수에 저장
    text=True,                # 문자열로 변환 (UTF-8)
    encoding='utf-8'
)
'''



process = subprocess.run(
    f'cmd /c chcp 65001 & "{exe_path}" "{model_path}" "{prompt}"',
    capture_output=True,
    text=True,
    encoding='utf-8',
    shell=True  # cmd 명령어 실행용
)


# 출력 저장

print('프로세스 완료')




answer = process.stdout   # ✅ 여기 변수에 답변이 저장됨
answer = answer.replace('[INST]', '').replace('[INST]', '').replace('[/INST]', '').replace('<ans>', '').replace('</ans>', '').replace('<s>', '').replace('</s>', '').replace('[0m', '')





print(datetime.now())

time_end = datetime.now()


error_output = process.stderr  # 에러가 있으면 여기에 저장됨

print(datetime.now())


# 출력 확인
print("=== MODEL OUTPUT ===")
print(answer)

print('답변 완료')
print(datetime.now())


if error_output:
    print("=== ERROR ===")
    print(error_output)

print(datetime.now())



elapsed = time_end - time_start
print(elapsed)
print(elapsed.total_seconds())

# 총 초를 분/초로 분해
total_seconds = int(elapsed.total_seconds())
minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"=== 전체 소요 시간: {minutes}분 {seconds}초 ===")
