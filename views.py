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
    print(sentence)

    state_combo = sentence.split("!state!")[1]
    sentence = sentence.split("!state!")[0]

    print(777777777777)
    print(state_combo)
    print(sentence)

    state = "hjk"

    with open(os.path.join(os.path.dirname(__file__), 'static\\japan.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)
    korean_to_hiragana = data.get("korean_to_hiragana", {})

    list_lyrics = []
    for sentence_small in sentence.split("."):
        list_lyrics.append(sentence_small)
    list_lyrics = [item for item in list_lyrics if item != ""]



    if len(list_lyrics) == 1:
        if re.search(r'[一-龯]', list_lyrics[0]):
            state = "h"
    if len(list_lyrics) == 1:
        if not re.search(r'[一-龯]', list_lyrics[0]) and re.search(r'[ぁ-んァ-ン]', list_lyrics[0]):
            state = "j"
                
    if len(list_lyrics) >= 2:
        if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[0]) and not re.search(r'[一-龯]', list_lyrics[0]):
            state = "j"
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]):
                state = "j"
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and re.search(r'[一-龯]', list_lyrics[1]):
                state = "h"
            if not re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]):
                state = "jk"


    if len(list_lyrics) >= 2:
        if re.search(r'[一-龯]', list_lyrics[0]):
            state = "h"
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]):
                state = "hj"
            if not re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[1]): #####    2줄 한문 한글 sentence    hk   hj       한자 해석 hk      한자 한글히라가나 hj
                state = state_combo

    if len(list_lyrics) == 1:
        if re.search(r'[가-힣]', list_lyrics[0]):   ###  1줄 한글 sentence    j     k
            state = state_combo                

    if len(list_lyrics) >= 2:
        if re.search(r'[가-힣]', list_lyrics[0]) and re.search(r'[가-힣]', list_lyrics[1]):   # 2줄 j k jk    한글히라가나 한글히라가나 j      해석 해석 k        한글히라가나 해석 jk
            state = state_combo
                
            
    if len(list_lyrics) >= 3:
        if not re.search(r'[一-龯]', list_lyrics[0]) and not re.search(r'[一-龯]', list_lyrics[1]) and not re.search(r'[一-龯]', list_lyrics[2]):
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[0]) and re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]):
                state = "j"




    if len(list_lyrics) >= 4:
        print(list_lyrics)
        if re.search(r'[一-龯]', list_lyrics[0]) and re.search(r'[一-龯]', list_lyrics[3]):
            if re.search(r'[ぁ-ん|ァ-ヶ]', list_lyrics[1]):
                state = "hjk"
                print("hjk")
            else:
                state = "hkk"
                print("hkk")
    # list_lyrics = [item for item in list_lyrics if item != '']


    # h j hj k hk jk hjk hkk

    if state in ['h', 'j']:
        list_lyrics = [item for item in list_lyrics for _ in range(2)]
        
                            

    if state in ["hk", "jk"]:
        print(state)
        list_new = []
        for i, value in enumerate(list_lyrics):
            list_new.append(value)
            if (i+1) % 2 == 1:
                list_new.append(value)
        list_lyrics = list_new



        



    if state in ["hjk", "hkk", "jk"]:
        for i in range(len(list_lyrics)):
            if (i+1)%3 == 2:
                hiragana_sentence = ""
                for char in list_lyrics[i]:
                    hiragana_sentence += korean_to_hiragana.get(char, char)

                if state == "jk":
                    list_lyrics[i-1] = hiragana_sentence
                    list_lyrics[i] = hiragana_sentence
                else:
                    list_lyrics[i] = hiragana_sentence

    list_lyrics = [line.strip() for line in list_lyrics]

    print(list_lyrics)
    list_hanja = list_lyrics[::3]
    str_hanja = ".".join(list_hanja)
    
    word_list_total = []
    hiragana_pattern = re.compile(r'[ぁ-ん]$')
    suffixes = ['れ', 'られ', 'れる', 'られる', 'せる', 'させる', 'た', 'だ']
    stop_words = ['が', 'に', 'へ', 'の', 'し', 'て', 'など', 'を', 'お', 'は', 'と', 'も', 'だ', 'か', 'から', 'まで', 'なる', 'で', 'なっ', 'い', 'ます', 'です', 'ました','いる', 'です', 'する',  'でした', '。', '「', '」', '.', ',', '、', '？', '！', '・', ' ']

    tokenizer = Tokenizer()

    list_total = []


    if state in ['hj']:
        len_sentence = len(sentence.split("."))//2
        list_lyrics_temp = []
    if state in ['h', 'j']:
        len_sentence = len(sentence.split("."))
        list_lyrics_temp = []
    elif state in ['k']:
        len_sentence = len(sentence.split("."))
    else:
        len_sentence = len(list_lyrics)//3



    print(sentence.split("."))




    for idx_sentence in range(len_sentence):
        if state in ["hj", "h", "j"]:   ### hj    h j
            print(state)
            if state == "hj":
                list_sentence = sentence.split(".")
            if state in ["h", "j"]:
                list_sentence = list_lyrics

            for i in range(len(list_lyrics)):
                hiragana_sentence = ""
                for char in list_lyrics[i]:
                    hiragana_sentence += korean_to_hiragana.get(char, char)

            list_sentence = [item for item in list_sentence if item != ""]


            print(7)
            print(sentence.split("."))
            print(idx_sentence)
            print(len_sentence)

            hiragana_sentence = ""
            for char in list_sentence[2 * idx_sentence + 1]:
                hiragana_sentence += korean_to_hiragana.get(char, char)
            print(8888888888888)
            print(hiragana_sentence)

            translator = Translator(to_lang="ko", from_lang="ja")
            translated = translator.translate(hiragana_sentence) # .replace(".", ".<br>")
            korea = translated.strip()

            if state == "hj":
                list_lyrics_temp = []
                list_lyrics_temp.append(list_sentence[2 * idx_sentence])
                list_lyrics_temp.append(hiragana_sentence)
                list_lyrics_temp.append(korea)

                tokens = tokenizer.tokenize(list_sentence[2 * idx_sentence])

            if state == "h":
                list_lyrics_temp = []
                list_lyrics_temp.append(list_sentence[2 * idx_sentence])    # h
                list_lyrics_temp.append(hiragana_sentence)
                list_lyrics_temp.append(korea)

                tokens = tokenizer.tokenize(list_sentence[2 * idx_sentence])


            if state == "j":
                list_lyrics_temp = []
                list_lyrics_temp.append(hiragana_sentence)    # j
                list_lyrics_temp.append(hiragana_sentence)
                list_lyrics_temp.append(korea)

                print(888)
                print(hiragana_sentence)

                tokens = tokenizer.tokenize(hiragana_sentence)
                
            # tokens = tokenizer.tokenize(list_sentence[2 * idx_sentence])


        if state in ["k"]:   ### k
            print(state)


            list_sentence = sentence.split(".")

            for i in range(len(list_lyrics)):
                hiragana_sentence = ""
                for char in list_lyrics[i]:
                    hiragana_sentence += korean_to_hiragana.get(char, char)
                    list_lyrics[i] = hiragana_sentence

            list_sentence = [item for item in list_sentence if item != ""]
                

            translator = Translator(to_lang="ja", from_lang="ko")
            translated = translator.translate(sentence)

            list_new = []

            print(translated)
            print(list_lyrics)
            print(re.findall(r'[^。！？\.!?]+[。！？\.!?]*', translated))

            for idx_translated, item in enumerate(list_lyrics):
                print(idx_translated)
                list_new.append(re.findall(r'[^。！？\.!?]+[。！？\.!?]*', translated)[idx_translated])
                list_new.append(re.findall(r'[^。！？\.!?]+[。！？\.!?]*', translated)[idx_translated])
                list_new.append(item)

            print(list_new)
            list_lyrics = list_new


        else:
            tokens = tokenizer.tokenize(str_hanja.split(".")[idx_sentence])

        word_list = []

        for token in tokens:
            surface = token.surface
            print(surface)

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
        
                
        print(word_list)
        
        word_list = [
            word[:-3] + 'る' if word.endswith('られた') else
            word[:-3] + 'す' if word.endswith('された') else
            word[:-3] + 'す' if word.endswith('される') else
            word[:-3] + 'る' if word.endswith('られる') else
            word[:len(word)-1] if word.endswith('っ') and re.match(r'[\u4e00-\u9fff]', word[0]) else
            word
            for word in word_list
        ]



        print(list_lyrics)
        print(77777777777777777777777777777777777)
        print(state)

        if state in ["hj", "h", "j"]:
            print(7)
            yield "<span style='color: darkblue; font-size:20px;'>" + list_lyrics_temp[0] + "</span><br>" + list_lyrics_temp[1] + "<br><u>" + list_lyrics_temp[2] + "</u><br><br>"   # 1회성 가사 문장 전송

            

        else:
            print(8)
            for idx_lyrics in range(0, len(list_lyrics), 3):
                print(idx_lyrics)
                print(list_lyrics[idx_lyrics])
                if idx_lyrics == idx_sentence*3:
                    yield "<span style='color: darkblue; font-size:20px;'>" + list_lyrics[idx_lyrics] + "</span><br>" + list_lyrics[idx_lyrics+1] + "<br><u>" + list_lyrics[idx_lyrics+2] + "</u><br><br>"   # 1회성 가사 문장 전송































        
        
        for idx_word, word in enumerate(word_list):
            print(word)

            list_total.append(word)
            
            str_word = ""    # 히라가나 [한자] 한글뜻
            str_word_list = ""   # 각 word의 1번째 줄에만 word 원본
            
            html = requests.get(f"https://dic.daum.net/search.do?dic=jp&q={word}")
            soup = BeautifulSoup(html.text, "html.parser")
            
            list_hiragana = [div.find("a", class_=["txt_cleansch", "txt_searchword"]).text for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]
            list_meaning = [re.sub("\\(.*?\\)\\s*", "", div.find("span", class_="txt_search").text)[:7] for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]
            list_kanji = [div.find("span", class_="sub_txt").text.replace("\n", "").replace("\t", "").replace(" ", "").replace("口", "") if div.find("span", class_="sub_txt") else "" for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]


            print(list_hiragana)
            print(list_meaning)
            print(list_kanji)



            
            # 중복 단어 제거
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
            
            # 한자의 한글 뜻, 음   kanji_meaning
            kanji_meaning = ""
            if not list_kanji:   # 카타카나 word는 list_kanji = []
                pass
            elif list_kanji[0] == "":   # 숫자 word는 list_kanji = ['', '']
                pass
            elif ('一' <= list_kanji[0][0] <= '龥') or ('㐀' <= list_kanji[0][0] <= '䶵'):
                print(list_kanji[0])
                html = requests.get("https://dic.daum.net/search.do?dic=hanja&q=" + list_kanji[0])
                soup = BeautifulSoup(html.text, "html.parser")
                div = soup.find("div", class_="card_word")

                if not div:
                    continue
                
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

                if i > 0 and len(list_meaning[i]) > 6:   # 2번째 단어 부터 뜻이 7글자 이상이면 제거
                    continue
                    
                if re.match(r'[ア-ン]', word[0]) and re.match(r'[あ-ん]', list_hiragana[i][0]) and word != list_hiragana[i]:   # 가타카나 word 와 다른 가타카나 제거
                    continue

                if not re.match(r'[\u4e00-\u9fff]', word[0]) and list_hiragana[i] != word and i > 0:   # 히라가나 word와 다른 히라가나 단어
                    continue

                if re.match(r'[\u4e00-\u9fff]', word[0]) and list_kanji[i] == "":  # 한자 word의 [한자] 가 없는 경우
                    continue




                if kanji_meaning:
                    str_word += list_hiragana[i] + " [" + list_kanji[i] + "] " + list_meaning[i] + "&nbsp;&nbsp;&nbsp;" + kanji_meaning + "<br>"
                else:
                    str_word += list_hiragana[i] + " [" + list_kanji[i] + "] " + list_meaning[i] + "<br>"

            if idx_word == len(word_list)-1:
                str_word += "<br>"

            if str_word != "":
                yield str_word + "<br>"   # 실시간 단어 데이터

            if idx_word == len(word_list)-1 and idx_sentence == len(list_hanja)-1:
                yield str(list_total).replace("[", "[ ").replace("]", " ]").replace("'", "").replace(",", "&nbsp;") + "<br><br>"

            time.sleep(1)
                    




            








def get_words(request):
    sentence = request.GET.get('sentence', '')
    sentence_temp = ""
    
    word_list = []
    suffixes = ['れ', 'られ', 'れる', 'られる', 'せる', 'させる', 'た', 'だ']
    stop_words = ['が', 'に', 'へ', 'の', 'し', 'て', 'など', 'を', 'お', 'は', 'と', 'も', 'だ', 'か', 'から', 'まで', 'なる', 'で', 'なっ', 'い', 'ます', 'です', 'ました','いる', 'です', 'する',  'でした', '。', '「', '」', '.', ',', '、', '？', '！', '・', ' ']


    if re.compile(r"[가-힣]").search(sentence):

        list_sentence = re.findall(r'[^。！？\?！｡\.]+[。！？\?！｡\.]?', sentence)
        list_sentence = [sentence.strip() for sentence in list_sentence]


        list_sentence = [
            sentence + "." if not re.search(r'[。！？\?！｡\.\?！]$', sentence) else sentence
            for sentence in list_sentence
        ]

        print(list_sentence)




        translator = Translator(to_lang="ja", from_lang="ko")


        list_translated = []
        for idx, item in enumerate(list_sentence):
            if len(item) >= 500:
                yield "1문장에 500자 이내 까지만 번역 가능합니다.<br><br>" + item
                return
            translated = translator.translate(item)
            list_translated.append(translated)
            yield "!response_start!" + "<span style='color: darkblue; font-size:20px;'>" + translated + "</span><br><u>" + item + "</u><br><br>"
        yield "!border!"

        print(list_translated)

        print(8)

        str_sentence = str(list_translated).replace("['", "").replace("']", "").replace("', '", " ")
        print(str_sentence)

        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(str_sentence)


        
    else:

        list_sentence = re.findall(r'[^。！？\?！｡\.]+[。！？\?！｡\.]?', sentence)
        list_sentence = [sentence.strip() for sentence in list_sentence]


        list_sentence = [
            sentence + "." if not re.search(r'[。！？\?！｡\.\?！]$', sentence) else sentence
            for sentence in list_sentence
        ]

        print(list_sentence)

        translator = Translator(to_lang="ko", from_lang="ja")

        list_translated = []
        for idx, item in enumerate(list_sentence):
            if len(item) >= 500:
                yield "1문장에 500자 이내 까지만 번역 가능합니다.<br><br>" + item
                return
            translated = translator.translate(item)
            yield "!response_start!" + "<span style='color: darkblue; font-size:20px;'>" + item + "</span><br><u>" + translated + "</u><br><br>"
        yield "!border!"

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
        word[:len(word)-1] if word.endswith('っ') and re.match(r'[\u4e00-\u9fff]', word[0]) else        
        word
        for word in word_list
        ]
    
    word_list = [word.replace('.', '') for word in word_list]    
    word_list = [word for word in word_list if not re.match(r"^[\u3000\u2000-\u200B\u00A0【】]+$", word)]




    list_total = []
    count_word_list = 0

    print(word_list)

    for word in (word_list):

        print(word)
        
        list_total.append(word)

        str_word = ""    # 히라가나 [한자] 한글뜻
        str_word_list = ""   # 각 word의 1번째 줄에만 word 원본

        html = requests.get(f"https://dic.daum.net/search.do?dic=jp&q={word}")
        soup = BeautifulSoup(html.text, "html.parser")

        list_hiragana = [div.find("a", class_=["txt_cleansch", "txt_searchword"]).text for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]
        list_meaning = [re.sub("\\(.*?\\)\\s*", "", div.find("span", class_="txt_search").text)[:7] for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]
        list_kanji = [div.find("span", class_="sub_txt").text.replace("\n", "").replace("\t", "").replace(" ", "").replace("口", "") if div.find("span", class_="sub_txt") else "" for div in soup.find_all("div", class_=["cleanword_type kujk_type", "search_type kujk_type"])[:8]]


        # 중복 단어 제거
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


        # 한자의 한글 뜻, 음   kanji_meaning

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

            if i > 0 and len(list_meaning[i]) > 6:   # 2번째 단어 부터 뜻이 7글자 이상이면 제거
                continue
            
            if re.match(r'[ア-ン]', word[0]) and re.match(r'[あ-ん]', list_hiragana[i][0]) and word != list_hiragana[i]:   # 가타카나 word 와 다른 가타카나 제거
                continue

            if not re.match(r'[\u4e00-\u9fff]', word[0]) and list_hiragana[i] != word and i > 0:   # 히라가나 word와 다른 히라가나 단어
                continue
            
            if re.match(r'[\u4e00-\u9fff]', word[0]) and list_kanji[i] == "":   # 한자 word의 [한자] 가 없는 경우
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

        yield str_word + "!border_title!" + str_word_list + "!border_title!" # 실시간 데이터
        # time.sleep(1)

    str_total = str(list_total).replace("[", "[ ").replace("]", " ]").replace("'", "").replace(", ", "&nbsp;&nbsp;")

    time.sleep(1)
    yield "!word_total!<br>" + str_total
        







def get_response(request):
    # 실시간으로 데이터를 스트리밍하려면 StreamingHttpResponse 사용
    response = StreamingHttpResponse(get_words(request))
    response['Content-Type'] = 'text/html; charset=utf-8'
    return response



def get_response_js(request):
    response = StreamingHttpResponse(get_words_js(request))
    response['Content-Type'] = 'text/html; charset=utf-8'

    
    return response






