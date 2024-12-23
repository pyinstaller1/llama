
from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup

import time
import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)





def index(request):
    return render(request, 'index.html')





def generate_streaming_html(request):
    sentence = request.GET.get('sentence', '')
    words = sentence.split()

    # 각 단어에 대한 정의를 실시간으로 클라이언트로 전송
    for word in words:
        definition = get_definition_from_api(word)  # 단어에 대한 정의 가져오기
        yield f"<p><strong>{word}</strong>: {definition}</p>"
        
        time.sleep(1)  # 실시간 응답을 위해 약간의 시간 지연 (필요 시 조정)

def get_definition_from_api(word):
    try:
        # 실제 크롤링할 웹사이트 URL
        url = f'https://www.weblio.jp/content/{word}'
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            soup = soup.find("div", class_="kiji")
            
            if soup:
                meaning = "   ".join([a.text.split("【")[0].split("〔")[0][:8] for a in soup.find_all("h2", class_="midashigo")])
                return meaning
            else:
                return "Definition not found"
        else:
            return "Failed to retrieve data"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def crawl_words(request):
    # 실시간으로 데이터를 스트리밍하려면 StreamingHttpResponse 사용
    response = StreamingHttpResponse(generate_streaming_html(request))
    response['Content-Type'] = 'text/html; charset=utf-8'
    return response


