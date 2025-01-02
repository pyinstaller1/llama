from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
import re
from janome.tokenizer import Tokenizer
import time
import urllib3
from translate import Translator
import spacy



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 기본 페이지로 연결되는 뷰
def index(request):
    return render(request, 'index_english.html')





def get_words(request):
    sentence = request.GET.get('sentence', '')

    sentence = "it works well really in paris."

    translator = Translator(to_lang="ko", from_lang="en")
    translated = translator.translate(sentence).replace(".", ".<br>")

    print(sentence)
    print(translated)







    


    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    print(doc)
    print(7)

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(sentence)

    word_list = []

    list_lemmas = []
    for token in doc:
        if not token.is_stop:
            if token.lemma_ not in [ '.', ',']:
                word_list.append(token.lemma_)

    print(word_list)

    str_word = str(word_list)

    print(str_word)
    





    print(88888)




    for token in tokens:
        word_list.append(token.surface)
        
    word_list = [word for word in word_list if word not in stop_words]
 
    count_word_list = 0

    for word in word_list:
        html = requests.get("https://www.wordreference.com/enko/" + word)
        soup = BeautifulSoup(html.text, "html.parser")

        span = soup.find("span", {"class": "pronWR tooltip pronWidget"})
        pron = " [" + span.text.split("/")[1].replace("ˈ", "").replace("ˌ", "")+ "] "
        # pron = ": "


        tr = soup.find_all("tr", {"class": "even"})

        list_temp = []
        for tr_meaning in tr[:5*3]:   # 3가지 의미
            if tr_meaning.find("td", {"class": "ToWrd"}):
                if tr_meaning.find("td", {"class": "ToWrd"}).contents[0]:
                    if str(tr_meaning.find("td", {"class": "ToWrd"}).contents[0])[0] != "<":
                        list_temp.append(tr_meaning.find("td", {"class": "ToWrd"}).contents[0].split(",")[0].split(",")[0].strip())

        list_temp = list(dict.fromkeys(list_temp))
        list_temp = [item for item in list_temp if len(item) <= 7]
        meaning = ", ".join(list_temp[:2])
        print (word + pron + meaning + "<br>")





    

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
                if re.match(r'[\u4e00-\u9fff]', word[0]) and re.match(r'[\u4e00-\u9fff]', list_kanji[i][0]) and re.sub(r'[^\u4e00-\u9fff]', '', word) != re.sub(r'[^\u4e00-\u9fff]', '', list_kanji[i]) and '·' not in list_kanji[i]:
                    continue

            if re.match(r'[ア-ン]', word[0]):   # 카타카나 word와 다른 카타카나 단어 제거
                if re.match(r'[ア-ン]', word[0]) and re.match(r'[カ-ン]', list_hiragana[i][0]) and re.sub(r'[^ア-ン]', '', word) != re.sub(r'[^ア-ン]', '', list_hiragana[i]):
                    continue

            if len(list_hiragana[0]) <= 8 and len(list_hiragana[i]) > 8: # 긴 설명의 단어 제거
                continue

            if re.match(r'[ア-ン]', word[0]) and re.match(r'[あ-ん]', list_hiragana[i][0]) and word != list_hiragana[i]:   # 가타카나 word 와 다른 가타카나 제거
                continue


            
            str_word += list_hiragana[i] + " [" + list_kanji[i] + "] " + list_meaning[i] + "&nbsp;&nbsp;&nbsp;" + kanji_meaning + "<br>"



        # word_list 의 중복 의미 들 중 1번째 단어 위치에만, word_list 단어 원본 표시 => str_word_list
        count_str_word_list = 0
        for i in range(len(str_word.split("<br>"))):
            if count_str_word_list == 0:         # 1단어의 1번째 종류이면, word_list의 단어 표시 
                str_word_list += word + "<br>"
                count_str_word_list = 1
            else:
                str_word_list += "<br>"         # 1단어의 1번째 종류가 아니면, <br> 만 추가 해서 str_word와 줄을 맞춤

        str_word += "<br>"



        if count_word_list == 0: # 1회성 데이터
            if len(word_list) == 1:
                yield (translated + "<br>" + str(word_list)).replace("'", "").replace("[", "[ ").replace("]", " ]") + "!border!" + str_word + "!border_title!" + str_word_list + "!border_title!"
            else:
                yield (translated + "<br>" + str(word_list)).replace("'", "").replace("[", "[ ").replace("]", " ]") + "!border!"
                count_word_list = 1


        yield str_word + "!border_title!" + str_word_list + "!border_title!" # 실시간 데이터
        time.sleep(0.8)







def get_response(request):
    # 실시간으로 데이터를 스트리밍하려면 StreamingHttpResponse 사용
    response = StreamingHttpResponse(get_words(request))
    response['Content-Type'] = 'text/html; charset=utf-8'

    
    return response

