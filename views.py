from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
import re
from janome.tokenizer import Tokenizer
import time
import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 기본 페이지로 연결되는 뷰
def index(request):
    return render(request, 'index.html')  # index.html 템플릿을 렌더링





def get_words(request):
    sentence = request.GET.get('sentence', '')

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(sentence)

    word_list = []
    suffixes = ['れ', 'られ', 'れる', 'られる', 'せる', 'させる', 'た', 'だ']
    stop_words = ['が', 'に', 'の', 'し', 'て', 'など']

    hiragana_pattern = re.compile(r'[ぁ-ん]$')

    for token in tokens:
        surface = token.surface

        # 'れ'나 'られ'와 같은 접미사가 붙은 동사를 처리
        if surface in suffixes and len(word_list) > 0:
            if hiragana_pattern.search(word_list[-1]):
                word_list[-1] = word_list[-1] + surface  # 앞 단어와 합치기
            else:
                word_list.append(surface)
        else:
            word_list.append(surface)
        
    word_list = [word for word in word_list if word not in stop_words]
    print(word_list)

    count_word_list = 0

    for word in word_list:

        str_word = ""

        html = requests.get(f"https://dic.daum.net/search.do?dic=jp&q={word}")
        soup = BeautifulSoup(html.text, "html.parser")

        list_hiragana = [div.find("a", class_=["txt_cleansch", "txt_searchword"]).text for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]
        list_meaning = [re.sub("\\(.*?\\)\\s*", "", div.find("span", class_="txt_search").text)[:10] for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]
        list_kanji = [div.find("span", class_="sub_txt").text.replace("\n", "").replace("\t", "").replace(" ", "").replace("口", "") if div.find("span", class_="sub_txt") else "" for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]



        # 중복 제거
        unique_hiragana = []
        unique_meaning = []
        unique_kanji = []

        for idx, h in enumerate(list_hiragana):
            if h not in unique_hiragana:
                unique_hiragana.append(h)
                unique_meaning.append(list_meaning[idx])
                unique_kanji.append(list_kanji[idx])

        list_hiragana = unique_hiragana[:3]
        list_meaning = unique_meaning[:3]
        list_kanji = unique_kanji[:3]

        for i in range(len(list_hiragana)):
            if list_kanji[i]:   # word의 한자와 다른 한자 단어 제거
                if re.match(r'[\u4e00-\u9fff]', word[0]) and re.match(r'[\u4e00-\u9fff]', list_kanji[i][0]) and re.sub(r'[^\u4e00-\u9fff]', '', word) != re.sub(r'[^\u4e00-\u9fff]', '', list_kanji[i]):
                    continue

            if re.match(r'[カ-ン]', word[0]):   # 카타카나 word와 다른 카타카나 단어 제거
                if re.match(r'[カ-ン]', word[0]) and re.match(r'[カ-ン]', list_hiragana[i][0]) and re.sub(r'[^カ-ン]', '', word) != re.sub(r'[^カ-ン]', '', list_hiragana[i]):
                    continue

            
            str_word += list_hiragana[i] + " [" + list_kanji[i] + "] " + list_meaning[i] + "<br>"
        str_word += "<br>"


        if count_word_list == 0:
            yield str(word_list).replace("'", "") + "word_list"
            count_word_list = 1

        yield str_word







def get_response(request):
    # 실시간으로 데이터를 스트리밍하려면 StreamingHttpResponse 사용
    response = StreamingHttpResponse(get_words(request))
    response['Content-Type'] = 'text/html; charset=utf-8'

    
    return response

