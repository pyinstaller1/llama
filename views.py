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

        str_word = ""    # 히라가나 [한자] 한글뜻
        str_word_list = ""   # 각 word의 1번째 줄에만 word 원본

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



        # 한자의 한글 뜻 kanji_meaning

        kanji_meaning = ""
        if not list_kanji:   # 카타카나 word는 list_kanji = []
            pass
            
        elif list_kanji[0] == "":   # 숫자 word는 list_kanji = ['', '']
            pass
        
        elif ('一' <= list_kanji[0][0] <= '龥') or ('㐀' <= list_kanji[0][0] <= '䶵'):
            html = requests.get("https://dic.daum.net/search.do?dic=hanja&q=" + list_kanji[0])
            soup = BeautifulSoup(html.text, "html.parser")
            div = soup.find("div", class_="card_word")
            span = div.find_all("span", class_="txt_emph1")
            list_span = []

            for data in span:
                list_span.append(data.text)

            a = div.find_all("a", class_="sub_read")
            list_a = []
            for data in a:
                list_a.append(data.text.split(",")[0])

            for i in range(min(len(list_span), len(list_a))):
                kanji_meaning = kanji_meaning + list_span[i] + " " + list_a[i] + "&nbsp;&nbsp;&nbsp;"
            kanji_meaning += "end"
            kanji_meaning = kanji_meaning.strip().replace("&nbsp;&nbsp;&nbsp;end", "")
            


        # str_word: 히라가나 [한자] 한글뜻   kanji_meaning
        for i in range(len(list_hiragana)):
            if list_kanji[i]:   # 한자 word의 한자와 다른 한자 단어 제거
                if re.match(r'[\u4e00-\u9fff]', word[0]) and re.match(r'[\u4e00-\u9fff]', list_kanji[i][0]) and re.sub(r'[^\u4e00-\u9fff]', '', word) != re.sub(r'[^\u4e00-\u9fff]', '', list_kanji[i]):
                    continue

            if re.match(r'[カ-ン]', word[0]):   # 카타카나 word와 다른 카타카나 단어 제거
                if re.match(r'[カ-ン]', word[0]) and re.match(r'[カ-ン]', list_hiragana[i][0]) and re.sub(r'[^カ-ン]', '', word) != re.sub(r'[^カ-ン]', '', list_hiragana[i]):
                    continue

            
            str_word += list_hiragana[i] + " [" + list_kanji[i] + "] " + list_meaning[i] + "&nbsp;&nbsp;&nbsp;" + kanji_meaning + "<br>"


        print(88888888888)
        print(str_word)
        # word_list 의 중복 의미 들 중 1번째 단어 위치에만, word_list 단어 원본 표시 => str_word_list
        count_str_word_list = 0
        for i in range(len(str_word.split("<br>"))):
            if count_str_word_list == 0:         # 1단어의 1번째 종류이면, word_list의 단어 표시 
                str_word_list += word + "<br>"
                count_str_word_list = 1
            else:
                str_word_list += "<br>"         # 1단어의 1번째 종류가 아니면, <br> 만 추가 해서 str_word와 줄을 맞춤


        str_word += "<br>"
        str_word_list += "<br>"




        if count_word_list == 0: # 1회성 데이터
            yield str(word_list).replace("'", "") + "!border!"
            count_word_list = 1

        print(str_word + "!border_title!" + str_word_list)
        print(777)

        yield str_word + "!border_title!" + str_word_list + "!border_title!" # 실시간 데이터







def get_response(request):
    # 실시간으로 데이터를 스트리밍하려면 StreamingHttpResponse 사용
    response = StreamingHttpResponse(get_words(request))
    response['Content-Type'] = 'text/html; charset=utf-8'

    
    return response

