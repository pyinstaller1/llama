from django.shortcuts import render
from django.http import StreamingHttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
import re
from janome.tokenizer import Tokenizer
import time
import urllib3
from translate import Translator
import json
import os



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 기본 페이지로 연결되는 뷰
def index(request):
    return render(request, 'index.html')  # index.html 템플릿을 렌더링




def hiragana(request):
    # sentence = request.GET.get('sentence', '')
    return render(request, 'hiragana.html')


def index_js(request):
    return render(request, 'js.html')  # index.html 템플릿을 렌더링


def get_words_js(request):
    sentence = request.GET.get('sentence', '')
    state = "hjk"

    with open(os.path.join(os.path.dirname(__file__), 'static\\japan.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)
    korean_to_hiragana = data.get("korean_to_hiragana", {})

    list_lyrics = []
    for sentence_small in sentence.split("."):
        list_lyrics.append(sentence_small)





    if len(list_lyrics) == 1:
        if re.search(r'[一-龯]', list_lyrics[0]):
            state = "h"
    if len(list_lyrics) == 1:
        if not re.search(r'[一-龯]', list_lyrics[0]):
            state = "j"
            
    if len(list_lyrics) >= 2:
        if re.search(r'[一-龯]', list_lyrics[0]):
            state = "h"
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]):
                state = "hj"
            # if not re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]):
            #    state = "hk"
                
    if len(list_lyrics) >= 2:
        if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[0]) and not re.search(r'[一-龯]', list_lyrics[0]):
            state = "j"
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]):
                state = "j"
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and re.search(r'[一-龯]', list_lyrics[1]):
                state = "h"
            if not re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]):
                state = "jk"
                
            
    if len(list_lyrics) >= 3:
        if not re.search(r'[一-龯]', list_lyrics[0]) and not re.search(r'[一-龯]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[2]):
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[0]) and re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]):
                state = "j"
            else:
                state = "jk"


    if len(list_lyrics) >= 3:
        if re.search(r'[一-龯]', list_lyrics[0]) and re.search(r'[一-龯]', list_lyrics[3]):
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]):
                state = "hjk"
                print("hjk")
            else:
                state = "hkk"
                print("hkk")
    print("state: " + state)
    list_lyrics = [item for item in list_lyrics if item != '']


    # h hj hk j jk hjk hkk

    if state in ['h', 'j']:
        list_lyrics = [item for item in list_lyrics for _ in range(2)]
        print(list_lyrics)
        state = "hj"




    # translated = re.sub(r'\|+', '|', translated)
    # translated = translated.replace("|", ".")
        
    if state in ["hj"]:
        print("hj")
        translator = Translator(to_lang="ko", from_lang="ja")
        translated = translator.translate(re.sub(r'[.?!]', "|", sentence))
        print(7)
        print(re.sub(r'[.?!]', "|", sentence.replace("(", "").replace(")", "")))
        print(sentence)
        print(translated)

        return










def translate_batch(lines, src_lang='ja', dest_lang='en'):
    translator = Translator()
    # 여러 문장을 한 번에 번역 (리스트로 전달)
    translations = translator.translate(lines, src=src_lang, dest=dest_lang)
    return [translation.text for translation in translations]

# 번역할 일본어 문장들
lines = [
    "諦めを手にしないで",  # Don't give up
    "都會かくれた ポ-カ- poker face",  # The city hides the poker face
    "海に捨ててしまおう",  # Let's throw it into the sea
    "あの微笑みを忘れないで"  # Don't forget that smile
]
























        list_translated = [translated.split("<br>")[i] for i in range(len(translated.split("<br>"))) if i % 2 == 0]

        list_korea = []
        korea = []
        for i in range(len(translated.split("|"))):
            print(8)
            if (i+3)%3 == 1:
                print(list_lyrics[i])
                list_korea.append(translated.split("|")[i])
        print(list_korea)
        korea = ' | '.join(list_korea)
        print(korea)





        
        for i in range(len(list_lyrics)):
            if (i+3)%3 == 1:
                print(list_lyrics[i])
                translated = translator.translate(re.sub(r'[.?!]', '|', sentence))
                list_korea = translated.split("|")
                print(list_korea)


    if state in ["hjk", "hkk"]:
        for i in range(len(list_lyrics)):
            print((i+1)%3)
            if (i+1)%3 == 2:
                print(list_lyrics[i])
                hiragana_sentence = ""
                for char in list_lyrics[i]:
                    hiragana_sentence += korean_to_hiragana.get(char, char)
                print(hiragana_sentence)
                list_lyrics[i] = hiragana_sentence
                print(777)
                





    
    print(list_lyrics)
    


            




    return






def get_words(request):
    sentence = request.GET.get('sentence', '')
    sentence_temp = ""
    
    word_list = []
    suffixes = ['れ', 'られ', 'れる', 'られる', 'せる', 'させる', 'た', 'だ']
    stop_words = ['が', 'に', 'へ', 'の', 'し', 'て', 'など', 'を', 'お', 'は', 'と', 'も', 'だ', 'か', 'から', 'まで', 'なる', 'で', 'なっ', 'い', 'ます', 'です', 'ました','いる', 'です', 'する',  'でした', '。', '「', '」', '.', ',', '、', '？', '！', '・', ' ']


    if re.compile(r"[가-힣]").search(sentence):

        translated_temp = ""
        translated = ""

        translator = Translator(to_lang="ja", from_lang="ko")
        translated = translator.translate(re.sub(r'[.?!]', '|', sentence))
        translated = re.sub(r'\|+', '|', translated)
        translated = translated.replace("|", ".")
        
        sentence_temp = sentence
        sentence = translated    # 일-한 번역 => 한-일 번역
        translated = sentence_temp

        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(sentence)


        
    else:
        translator = Translator(to_lang="ko", from_lang="ja")
        translated = translator.translate(sentence).replace(".", ".<br>")

        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(sentence)


    hiragana_pattern = re.compile(r'[ぁ-ん]$')

    for token in tokens:
        surface = token.surface

        # 'れ'나 'られ'와 같은 접미사가 붙은 동사를 처리
        if surface in suffixes and len(word_list) > 0:
            if hiragana_pattern.search(word_list[-1]):
                word_list[-1] = word_list[-1] + surface  # 앞 단어와 합치기
            else:
                if surface not in ["."]:
                    word_list.append(surface)
        else:
            word_list.append(surface)
        
    word_list = [word for word in word_list if word not in stop_words]
    word_list = [word for word in word_list if word not in ["？."]]

            
    word_list = [
        word[:-3] + 'る' if word.endswith('られた') else
        word[:-3] + 'す' if word.endswith('された') else
        word[:-3] + 'す' if word.endswith('される') else
        word[:-3] + 'る' if word.endswith('られる') else
        word
        for word in word_list
        ]


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



        if sentence_temp != "":
            translated = sentence

        

        if count_word_list == 0: # 1회성 데이터
            if len(word_list) == 1:
                yield (translated + "<br>+[" + str(word_list)).replace("'", "").replace("[", "[ ").replace("]", " ]") + "!border!" + str_word + "!border_title!" + str_word_list + "!border_title!"
            else:
                yield (translated + "<br>+[" + str(word_list)).replace("'", "").replace("[", "[ ").replace("]", " ]") + "!border!"
                count_word_list = 1


        yield str_word + "!border_title!" + str_word_list + "!border_title!" # 실시간 데이터
        time.sleep(1)







def get_response(request):
    # 실시간으로 데이터를 스트리밍하려면 StreamingHttpResponse 사용
    response = StreamingHttpResponse(get_words(request))
    response['Content-Type'] = 'text/html; charset=utf-8'
    return response



def get_response_js(request):
    response = StreamingHttpResponse(get_words_js(request))
    response['Content-Type'] = 'text/html; charset=utf-8'

    
    return response






