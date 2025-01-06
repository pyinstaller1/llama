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
    
    list_sentence = re.findall(r'[^.?!\n]+[.?!\n]?', sentence)

    list_sentence = [item for item in list_sentence if item.strip()]
    print(list_sentence)

    translator = Translator(to_lang="ko", from_lang="en")
    
    nlp = spacy.load("en_core_web_sm")
    tokenizer = Tokenizer()

    word_total = []
    list_translated = []
    
    for idx, item in enumerate(list_sentence):

        if len(item) >= 500:
            yield "1문장에 500자 이내 까지만 번역 가능합니다.<br><br>"
            yield item
            return
        
        list_translated.append(translator.translate(item))
        print(list_translated)



        str_translated = "<span style='color: darkblue; font-size:20px;'>" + list_sentence[idx] + "</span><br><u>" + list_translated[idx] + "</u><br>"
        print(str_translated)
        yield str_translated




























        
        doc = nlp(item)

        tokens = tokenizer.tokenize(item)

        word_list = []

        for token in doc:
            if not token.is_stop:
                if token.lemma_ not in [ '.', ',']:
                    word_list.append(token.lemma_)


        word_list = [word for word in word_list if word not in ['', '.', '!', '?', '\n']]

        """
        for token in tokens:
            word_list.append(token.surface)
        """

        stop_words = ['works']
        word_list = [word for word in word_list if word not in stop_words]


        count_word_list = 0
        str_word = ""
        for idx_word, word in enumerate(word_list):
            html = requests.get("https://www.wordreference.com/enko/" + word)
            soup = BeautifulSoup(html.text, "html.parser")

            span = soup.find("span", {"class": "pronWR tooltip pronWidget"})
            # pron = " [" + span.text.split("/")[1].replace("ˈ", "").replace("ˌ", "")+ "] "
            pron = " "
            tr = soup.find_all("tr", {"class": "even"})

            list_temp = []
            for tr_meaning in tr[:5*3]:   # 3가지 의미
                if tr_meaning.find("td", {"class": "ToWrd"}):
                    if tr_meaning.find("td", {"class": "ToWrd"}).contents[0]:
                        if str(tr_meaning.find("td", {"class": "ToWrd"}).contents[0])[0] != "<":
                            list_temp.append(tr_meaning.find("td", {"class": "ToWrd"}).contents[0].split(",")[0].split(",")[0].strip())

            list_temp = list(dict.fromkeys(list_temp))
            list_temp = [item for item in list_temp if len(item) <= 7]
            meaning = ", ".join(list_temp[:1])

            word_total.append(word)



            
            str_word_total = str(word_total).replace("[", "[ ").replace("]", " ]").replace("'", "").replace(", ", "&nbsp;&nbsp;")

            str_word = word + pron + meaning

            if idx_word < len(word_list)-1:
                str_word += "&nbsp;&nbsp;&nbsp;"
            yield str_word
            
        yield "<br><br>"
        # time.sleep(1)



    yield str_word_total

    # return
        











def get_response(request):
    # 실시간으로 데이터를 스트리밍하려면 StreamingHttpResponse 사용
    response = StreamingHttpResponse(get_words(request))
    response['Content-Type'] = 'text/html; charset=utf-8'

    
    return response

