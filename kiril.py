import bs4
import requests
import pyperclip
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def to_Korean(kiril):
    kiril = kiril.replace("а́", "а").replace("е́", "е").replace("и́", "и").replace("й", "й").replace("у́", "у").replace("ы́", "ы").replace("э́", "э").replace("ю", "ю").replace("я́", "я")
    korean = ""
    vowels = ["а", "е", "ё", "и", "й", "о", "о́", "у", "ы", "э", "ю", "я"]

    a2 = 0
    for i in range(0, len(kiril)):
        if a2==1: a2=0; continue
        if a2==2: a2=1; continue
        if a2==3: a2=2; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i + 1] == "о" and kiril[i + 1] == "г" and kiril[i + 1] == "о"): korean += "나바"; a2 = 3; continue

        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "а" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쌀"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "е" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쏄"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ё" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쑐"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "и" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "씰"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "й" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "씰"; a2 = 2; continue
        if (i+5 <= len(kiril)-1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i+2]+kiril[i+3]=="о́" and kiril[i+4]== "л" and kiril[i+5] in vowels): korean += "쏠"; a2=3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "о" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쌀"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "у" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쑬"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ы" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "씔"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "э" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쎌"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ю" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쓜"; a2 = 2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "я" and kiril[i + 3] == "л" and kiril[i + 4] in vowels): korean += "쌸"; a2 = 2; continue

        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "а" and kiril[i + 3] == "л"): korean += "쌀"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "е" and kiril[i + 3] == "л"): korean += "쏄"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ё" and kiril[i + 3] == "л"): korean += "쑐"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "и" and kiril[i + 3] == "л"): korean += "씰"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "й" and kiril[i + 3] == "л"): korean += "씰"; a2 = 3; continue
        if (i+5 <= len(kiril)-1) and (kiril[i] == "с" and kiril[i+1] == "с" and kiril[i+2]+kiril[i+3] == "о́" and kiril[i+4] == "л"): korean += "쏠"; a2=4; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "о" and kiril[i + 3] == "л"): korean += "쌀"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "у" and kiril[i + 3] == "л"): korean += "쑬"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ы" and kiril[i + 3] == "л"): korean += "씔"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "э" and kiril[i + 3] == "л"): korean += "쎌"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ю" and kiril[i + 3] == "л"): korean += "쓜"; a2 = 3; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "я" and kiril[i + 3] == "л"): korean += "쌸"; a2 = 3; continue






        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "발"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "발"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "갈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "달"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "잘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "깔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "랄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "말"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "날"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "빨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "랄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "살"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "딸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "팔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "할"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "짤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "а" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "찰"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "볠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "볠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "곌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뎰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "졜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "꼘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "롈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "몔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "녤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뼬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "롈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "셸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뗼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "폘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "혤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쪨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "е" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쳴"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뵬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뵬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "굘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "됼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "죨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "꾤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "룔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "묠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뇰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뾸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "룔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "숄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뚈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "푤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "횰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쬴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ё" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "춀"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "빌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "빌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "길"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "딜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "질"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "낄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "릴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "밀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "닐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "삘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "릴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "실"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "띨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "필"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "힐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "찔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "и" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "칠"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "빌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "빌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "길"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "딜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "질"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "낄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "릴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "밀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "닐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "삘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "릴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "실"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "띨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "필"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "힐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "찔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "й" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "칠"; a2 = 1; continue

        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "볼"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "볼"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "골"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "돌"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "졸"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "꼴"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "롤"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "몰"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "놀"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "뽈"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "롤"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "솔"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "똘"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "폴"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "홀"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "쫄"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о́" and kiril[i + 2]+kiril[i+3] == "л" and kiril[i + 4] in vowels): korean += "촐"; a2=2; continue




        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "발"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "발"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "갈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "달"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "잘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "깔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "랄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "말"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "날"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "빨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "랄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "살"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "딸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "팔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "할"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "짤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "찰"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "불"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "불"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "굴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "둘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "줄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "꿀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "룰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "물"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "눌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뿔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "룰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "술"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뚤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "풀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "훌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쭐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "у" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "출"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "븰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "븰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "긜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "딀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "즬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "끨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "릘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "밀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "늴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쁼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "릘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "싈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "띌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "픨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "흴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쯸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ы" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "칄"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "벨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "벨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "겔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "델"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "젤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "껠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "렐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "멜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "넬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뼬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "렐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "셀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뗄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "펠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "헬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쩰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "э" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "첼"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뷸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뷸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "귤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "듈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쥴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뀰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "률"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뮬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뉼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쁄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "률"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "슐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뜔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "퓰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "휼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쯀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ю" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "츌"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뱔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뱔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "걀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "댤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쟐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "꺌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "랼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "먈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "냘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "뺠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "랼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "샬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "땰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "퍌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "햘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "쨜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "я" and kiril[i + 2] == "л" and kiril[i + 3] in vowels): korean += "챨"; a2 = 1; continue


        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "바"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "바"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "가"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "다"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "자"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "까"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "라"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "마"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "나"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "빠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] == 'с'): korean += "라스"; a2 = 2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "라"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "사"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "따"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "파"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "하"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "짜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "а" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "차"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "볘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "볘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "계"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뎨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "졔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "꼐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "례"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "몌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "녜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뼤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "례"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "셰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뗴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "폐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "혜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쪠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "е" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쳬"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뵤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뵤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "교"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "됴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "죠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "꾜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "료"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "묘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뇨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뾰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "료"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쇼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뚀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "표"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "효"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쬬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ё" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쵸"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "비"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "비"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "기"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "디"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "지"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "끼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "리"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "미"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "니"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "삐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "리"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "시"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "띠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "피"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "히"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "찌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "и" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "치"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "비"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "비"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "기"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "디"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "지"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "끼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "리"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "미"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "니"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "삐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "리"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "시"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "띠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "피"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "히"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "찌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "й" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "치"; a2 = 1; continue


        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "보"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "보"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "고"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "도"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "조"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "꼬"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "로"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "모"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "노"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "뽀"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "로"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "소"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "또"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "포"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "호"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "쪼"; a2=2; continue
        if (i + 4 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о́" and kiril[i + 2] + kiril[i+3] not in vowels and kiril[i + 4] in vowels): korean += "초"; a2=2; continue



        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "바"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "바"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "가"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "다"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "자"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "까"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "라"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "마"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "나"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "빠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "라"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "사"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "따"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "파"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "하"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "짜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "차"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "부"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "부"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "구"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "두"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "주"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "꾸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "루"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "무"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "누"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뿌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "루"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "수"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뚜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "푸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "후"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쭈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "у" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "추"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "븨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "븨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "긔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "듸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "즤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "끠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "릐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "믜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "늬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쁴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "릐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "싀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "띄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "픠"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "희"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쯰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ы" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "츼"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "베"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "베"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "게"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "데"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "제"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "께"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "레"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "메"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "네"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뻬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "레"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "세"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "떼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "페"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "헤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쩨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "э" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "체"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뷰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뷰"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "규"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "듀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쥬"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뀨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "류"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뮤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뉴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쀼"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "류"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "슈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뜌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "퓨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "휴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쮸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ю" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "츄"; a2 = 1; continue

        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뱌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뱌"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "갸"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "댜"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쟈"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "꺄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "랴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "먀"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "냐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "뺘"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "랴"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "샤"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "땨"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "퍄"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "햐"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "쨔"; a2 = 1; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "я" and kiril[i + 2] not in vowels and kiril[i + 3] in vowels): korean += "챠"; a2 = 1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "а" and kiril[i + 2] in vowels): korean += "아"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "е" and kiril[i + 2] in vowels): korean += "예"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ё" and kiril[i + 2] in vowels): korean += "요"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "и" and kiril[i + 2] in vowels): korean += "이"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "й" and kiril[i + 2] in vowels): korean += "이"; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i]+kiril[i+1] == "о́" and kiril[i + 3] in vowels): korean += "오"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "о" and kiril[i + 2] in vowels): korean += "아"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "у" and kiril[i + 2] in vowels): korean += "우"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ы" and kiril[i + 2] in vowels): korean += "의"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "э" and kiril[i + 2] in vowels): korean += "에"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ю" and kiril[i + 2] in vowels): korean += "유"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "я" and kiril[i + 2] in vowels): korean += "야"; continue






        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] == "к"): korean += "깍"; a2=2; continue














        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "발"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "발"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "갈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "달"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "잘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "깔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "랄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "말"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "날"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "빨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "랄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "살"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "딸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "팔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "할"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "짤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "а" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "찰"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "볠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "볠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "곌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뎰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "졜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "꼘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "롈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "몔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "녤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뼬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "롈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "셸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뗼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "폘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "혤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쪨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "е" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쳴"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뵬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뵬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "굘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "됼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "죨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "꾤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "룔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "묠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뇰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뾸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "룔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "숄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뚈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "푤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "횰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쬴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ё" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "춀"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "빌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "빌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "길"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "딜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "질"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "낄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "릴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "밀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "닐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "삘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "릴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "실"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "띨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "필"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "힐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "찔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "и" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "칠"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "빌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "빌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "길"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "딜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "질"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "낄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "릴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "밀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "닐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "삘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "릴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "실"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "띨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "필"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "힐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "찔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "й" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "칠"; a2 = 2; continue



        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "볼"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "볼"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "골"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "돌"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "졸"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "꼴"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "롤"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "몰"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "놀"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "뽈"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "롤"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "솔"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "똘"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "폴"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "홀"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "쫄"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1]+kiril[i+2] == "о́" and kiril[i + 3] == "л") and (i+3==len(kiril) - 1 or (i+3<len(kiril)-1 and kiril[i+4] not in vowels)): korean += "촐"; a2=3; continue


        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "발"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "발"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "갈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "달"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "잘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "깔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "랄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "말"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "날"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "빨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "랄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "살"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "딸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "팔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "할"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "짤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "찰"; a2 = 2; continue






        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "불"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "불"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "굴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "둘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "줄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "꿀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "룰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "물"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "눌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "불"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "룰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "술"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뚤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "풀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "훌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쭐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "у" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "출"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "븰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "븰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "긜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "딀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "즬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "끨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "릘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "믤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "늴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쁼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "릘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "싈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "띌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "픨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "흴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쯸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ы" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "칄"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "벨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "벨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "겔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "델"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "젤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "껠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "렐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "멜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "넬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뻴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "렐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "셀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뗄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "펠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "헬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쩰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "э" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "첼"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뷸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뷸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "귤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "듈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쥴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뀰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "률"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뮬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뉼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쁄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "률"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "슐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뜔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "퓰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "휼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쯀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ю" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "츌"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뱔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뱔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "걀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "댤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쟐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "꺌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "랼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "먈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "냘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "뺠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "랼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "샬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "땰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "퍌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "햘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "쨜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "я" and kiril[i + 2] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "챨"; a2 = 2; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "а" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "알"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "е" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "옐"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ё" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "욜"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "и" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "일"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "й" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "일"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "о" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "알"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "о́" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "올"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "у" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "울"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ы" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "읠"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "э" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "엘"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ю" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "율"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "я" and kiril[i + 1] == "л") and (i + 2 == len(kiril) - 1 or (i + 2 < len(kiril) - 1 and kiril[i + 3] not in vowels)): korean += "얄"; a2 = 1; continue


        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "발"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "발"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "갈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "달"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "잘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "깔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "랄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "말"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "날"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "빨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "랄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "살"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "딸"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "팔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "할"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "짤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "а" and kiril[i + 2] == "л"): korean += "찰"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "볠"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "볠"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "곌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "뎰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "졜"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "꼘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "롈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "몔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "녤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "뼬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "롈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "셸"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "뗼"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "폘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "혤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "쪨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "е" and kiril[i + 2] == "л"): korean += "쳴"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "뵬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "뵬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "굘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "됼"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "죨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "꾤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "룔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "묠"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "뇰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "뾸"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "룔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "숄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "뚈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "푤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "횰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "쬴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ё" and kiril[i + 2] == "л"): korean += "춀"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "빌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "빌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "길"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "딜"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "질"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "낄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "릴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "밀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "닐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "삘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "릴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "실"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "띨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "필"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "힐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "찔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "и" and kiril[i + 2] == "л"): korean += "칠"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "빌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "빌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "길"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "딜"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "질"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "낄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "릴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "밀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "닐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "삘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "릴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "실"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "띨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "필"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "힐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "찔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "й" and kiril[i + 2] == "л"): korean += "칠"; a2=1; continue


        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "볼"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "볼"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "골"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "돌"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "졸"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "꼴"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "롤"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "몰"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "놀"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "뽈"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "롤"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "솔"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "똘"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "폴"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "홀"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "쫄"; a2=2; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "л"): korean += "촐"; a2=2; continue



        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "발"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "발"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "갈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "달"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "잘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "깔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "랄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "말"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "날"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "빨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "랄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "살"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "딸"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "팔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "할"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "짤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о" and kiril[i + 2] == "л"): korean += "찰"; a2=1; continue




        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "불"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "불"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "굴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "둘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "줄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "꿀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "룰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "물"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "눌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "불"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "룰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "술"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "뚤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "풀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "훌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "쭐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "у" and kiril[i + 2] == "л"): korean += "출"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "븰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "븰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "긜"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "딀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "즬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "끨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "릘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "믤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "늴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "쁼"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "릘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "싈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "띌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "픨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "흴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "쯸"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ы" and kiril[i + 2] == "л"): korean += "칄"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "벨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "벨"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "겔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "델"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "젤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "껠"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "렐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "멜"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "넬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "뻴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "렐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "셀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "뗄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "펠"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "헬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "쩰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "э" and kiril[i + 2] == "л"): korean += "첼"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "뷸"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "뷸"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "귤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "듈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "쥴"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "뀰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "률"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "뮬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "뉼"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "쁄"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "률"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "슐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "뜔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "퓰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "휼"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "쯀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ю" and kiril[i + 2] == "л"): korean += "츌"; a2=1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "뱔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "뱔"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "걀"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "댤"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "쟐"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "꺌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "랼"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "먈"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "냘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "뺠"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "랼"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "샬"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "땰"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "퍌"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "햘"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "쨜"; a2=1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "я" and kiril[i + 2] == "л"): korean += "챨"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "а" and kiril[i + 1] == "л"): korean += "알"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "е" and kiril[i + 1] == "л"): korean += "옐"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ё" and kiril[i + 1] == "л"): korean += "욜"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "и" and kiril[i + 1] == "л"): korean += "일"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "й" and kiril[i + 1] == "л"): korean += "일"; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i]+kiril[i+1] == "о́" and kiril[i + 2] == "л"): korean += "올"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "о" and kiril[i + 1] == "л"): korean += "알"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "у" and kiril[i + 1] == "л"): korean += "울"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ы" and kiril[i + 1] == "л"): korean += "읠"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "э" and kiril[i + 1] == "л"): korean += "엘"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ю" and kiril[i + 1] == "л"): korean += "율"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "я" and kiril[i + 1] == "л"): korean += "얄"; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "반"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "반"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "간"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "단"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "잔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "깐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "란"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "만"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "난"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "빤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "란"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "산"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "딴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "판"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "한"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "짠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "а" and kiril[i + 2] == "н"): korean += "챤"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "볜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "볜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "곈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "뎬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "졘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "꼔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "롄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "몐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "녠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "뼨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "롄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "셴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "뗸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "폔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "혠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "쪤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "е" and kiril[i + 2] == "н"): korean += "쳰"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "뵨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "뵨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "굔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "됸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "죤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "꾠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "룐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "묜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "뇬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "뾴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "룐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "숀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "뚄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "푠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "횬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "쬰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ё" and kiril[i + 2] == "н"): korean += "쵼"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "빈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "빈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "긴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "딘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "진"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "낀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "린"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "민"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "닌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "삔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "린"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "신"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "띤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "핀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "힌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "찐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "и" and kiril[i + 2] == "н"): korean += "친"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "빈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "빈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "긴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "딘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "진"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "낀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "린"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "민"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "닌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "삔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "린"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "신"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "띤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "핀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "힌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "찐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "й" and kiril[i + 2] == "н"): korean += "친"; a2 = 2; continue



        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "본"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "본"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "곤"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "돈"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "존"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "꼰"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "론"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "몬"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "논"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "뽄"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "론"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "손"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "똔"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "폰"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "혼"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "쫀"; a2=3; continue
        if (i + 3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "н"): korean += "촌"; a2=3; continue



        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "반"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "반"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "간"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "단"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "잔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "깐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "란"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "만"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "난"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "빤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "란"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "산"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "딴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "판"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "한"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "짠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о" and kiril[i + 2] == "н"): korean += "찬"; a2 = 2; continue






        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "분"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "분"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "군"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "둔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "준"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "꾼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "룬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "문"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "눈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "뿐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "룬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "순"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "뚠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "푼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "훈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "쭌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "у" and kiril[i + 2] == "н"): korean += "춘"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "븬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "븬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "긘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "듼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "즨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "끤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "릔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "믠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "늰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "쁸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "릔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "싄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "띈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "픤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "흰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "쯴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ы" and kiril[i + 2] == "н"): korean += "칀"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "벤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "벤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "겐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "덴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "젠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "껜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "렌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "멘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "넨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "뻰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "렌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "센"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "뗀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "펜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "헨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "쩬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "э" and kiril[i + 2] == "н"): korean += "첸"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "뷴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "뷴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "균"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "듄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "쥰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "뀬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "륜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "뮨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "뉸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "쁀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "륜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "슌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "뜐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "퓬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "휸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "쮼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ю" and kiril[i + 2] == "н"): korean += "츈"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "뱐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "뱐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "갼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "댠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "쟌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "꺈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "랸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "먄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "냔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "뺜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "랸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "샨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "땬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "퍈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "햔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "쨘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "я" and kiril[i + 2] == "н"): korean += "챤"; a2 = 2; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "а" and kiril[i + 1] == "н"): korean += "안"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "е" and kiril[i + 1] == "н"): korean += "옌"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ё" and kiril[i + 1] == "н"): korean += "욘"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "и" and kiril[i + 1] == "н"): korean += "인"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "й" and kiril[i + 1] == "н"): korean += "인"; a2 = 1; continue
        if (i+2 <= len(kiril)-1) and (kiril[i]+kiril[i+1] == "о́" and kiril[i+2] == "н"): korean += "온"; a2=2; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "о" and kiril[i + 1] == "н"): korean += "안"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "у" and kiril[i + 1] == "н"): korean += "운"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ы" and kiril[i + 1] == "н"): korean += "읜"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "э" and kiril[i + 1] == "н"): korean += "엔"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ю" and kiril[i + 1] == "н"): korean += "윤"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "я" and kiril[i + 1] == "н"): korean += "얀"; a2 = 1; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "밤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "밤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "감"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "담"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "잠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "깜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "람"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "맘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "남"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "빰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "람"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "삼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "땀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "팜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "함"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "짬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "а" and kiril[i + 2] == "м"): korean += "참"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "볨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "볨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "곔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "뎸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "졤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "꼠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "롐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "몜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "녬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "뼴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "롐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "솀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "똄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "폠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "혬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "쪰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "е" and kiril[i + 2] == "м"): korean += "쳼"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "뵴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "뵴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "굠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "둄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "죰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "꾬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "룜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "묨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "뇸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "뿀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "룜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "숌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "뚐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "푬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "횸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "쬼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ё" and kiril[i + 2] == "м"): korean += "춈"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "빔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "빔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "김"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "딤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "짐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "낌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "림"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "밈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "님"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "삠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "림"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "심"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "띰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "핌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "힘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "찜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "и" and kiril[i + 2] == "м"): korean += "침"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "빔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "빔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "김"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "딤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "짐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "낌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "림"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "밈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "님"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "삠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "림"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "심"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "띰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "핌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "힘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "찜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "й" and kiril[i + 2] == "м"): korean += "침"; a2 = 2; continue


        if (i+3 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "봄"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "봄"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "곰"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "돔"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "좀"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "꼼"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "롬"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "몸"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "놈"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "뽐"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "롬"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "솜"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "똠"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "폼"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "홈"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "쫌"; a2=3; continue
        if (i+3 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "м"): korean += "촘"; a2=3; continue


        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "밤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "밤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "감"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "담"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "잠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "깜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "람"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "맘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "남"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "빰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "람"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "삼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "땀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "팜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "함"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "짬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о" and kiril[i + 2] == "м"): korean += "찬"; a2 = 2; continue




        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "붐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "붐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "굼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "둠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "줌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "꿈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "룸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "뭄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "눔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "뿜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "룸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "숨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "뚬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "품"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "훔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "쭘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "у" and kiril[i + 2] == "м"): korean += "춤"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "븸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "븸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "긤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "딈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "즴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "끰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "릠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "믬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "늼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "삄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "릠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "싐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "띔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "픰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "흼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "찀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ы" and kiril[i + 2] == "м"): korean += "칌"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "벰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "벰"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "겜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "뎀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "젬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "껨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "렘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "멤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "넴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "뻼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "렘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "셈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "뗌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "펨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "헴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "쩸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "э" and kiril[i + 2] == "м"): korean += "쳄"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "븀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "븀"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "귬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "듐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "쥼"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "뀸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "륨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "뮴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "늄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "쁌"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "륨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "슘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "뜜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "퓸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "흄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "쯈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ю" and kiril[i + 2] == "м"): korean += "츔"; a2 = 2; continue

        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "뱜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "뱜"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "걈"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "댬"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "쟘"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "꺔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "럄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "먐"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "냠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "뺨"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "럄"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "샴"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "땸"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "퍔"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "햠"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "쨤"; a2 = 2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "я" and kiril[i + 2] == "м"): korean += "챰"; a2 = 2; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "а" and kiril[i + 1] == "м"): korean += "암"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "е" and kiril[i + 1] == "м"): korean += "옘"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ё" and kiril[i + 1] == "м"): korean += "욤"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "и" and kiril[i + 1] == "м"): korean += "임"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "й" and kiril[i + 1] == "м"): korean += "임"; a2 = 1; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i]+kiril[i+1] == "о́" and kiril[i+2] == "м"): korean += "옴"; a2=2; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "о" and kiril[i + 1] == "м"): korean += "암"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "у" and kiril[i + 1] == "м"): korean += "움"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ы" and kiril[i + 1] == "м"): korean += "읨"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "э" and kiril[i + 1] == "м"): korean += "엠"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ю" and kiril[i + 1] == "м"): korean += "윰"; a2 = 1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "я" and kiril[i + 1] == "м"): korean += "얌"; a2 = 1; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "밧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "밧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "갓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "닷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "잣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "깟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "랏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "맛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "낫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "빳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "랏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "삿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "땃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "팟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "핫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "짯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "а" and kiril[i + 2] == "т"): korean += "찻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "볫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "볫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "곗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "뎻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "졧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "꼣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "롓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "몟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "녯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "뼷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "롓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "솃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "똇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "폣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "혯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "쪳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "е" and kiril[i + 2] == "т"): korean += "쳿"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "뵷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "뵷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "굣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "둇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "죳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "꾯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "룟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "묫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "뇻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "뿃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "룟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "숏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "둇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "푯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "횻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "쬿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "ё" and kiril[i + 2] == "т"): korean += "춋"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "빗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "빗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "깃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "딧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "짓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "낏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "릿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "밋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "닛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "삣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "릿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "싯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "띳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "핏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "힛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "찟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "и" and kiril[i + 2] == "т"): korean += "칫"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "빗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "빗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "깃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "딧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "짓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "낏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "릿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "밋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "닛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "삣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "릿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "싯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "띳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "핏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "힛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "찟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "й" and kiril[i + 2] == "т"): korean += "칫"; a2 = 2; continue


        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "б" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "봇"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "в" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "봇"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "г" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "곳"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "д" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "돗"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "з" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "좃"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "к" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "꼿"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "л" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "롯"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "м" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "못"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "н" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "놋"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "п" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "뽓"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "р" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "롯"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "с" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "솟"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "т" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "똣"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "ф" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "폿"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "х" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "홋"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "ц" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "쫏"; a2=3; continue
        if (i+3 == len(kiril)-1 or (i+4 <= len(kiril)-1 and kiril[i+4] == "ь")) and (kiril[i] == "ч" and kiril[i+1]+kiril[i+2] == "о́" and kiril[i+3] == "т"): korean += "촛"; a2=3; continue





        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "밧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "밧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "갓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "닷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "잣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "깟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "랏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "맛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "낫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "빳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "랏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "삿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "땃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "팟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "핫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "짯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "о" and kiril[i + 2] == "т"): korean += "찬"; a2 = 2; continue



        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "붓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "붓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "굿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "둣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "줏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "꿋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "룻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "뭇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "눗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "뿟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "룻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "숫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "뚯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "풋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "훗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "쭛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "у" and kiril[i + 2] == "т"): korean += "춧"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "븻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "븻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "긧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "딋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "즷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "끳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "릣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "믯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "늿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "삇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "릣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "싓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "띗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "픳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "흿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "찃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "ы" and kiril[i + 2] == "т"): korean += "칏"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "벳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "벳"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "겟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "뎃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "젯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "껫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "렛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "멧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "넷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "뻿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "렛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "셋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "뗏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "펫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "헷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "쩻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "э" and kiril[i + 2] == "т"): korean += "쳇"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "븃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "븃"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "귯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "듓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "쥿"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "뀻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "륫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "뮷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "늇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "쁏"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "륫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "슛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "뜟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "퓻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "흇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "쯋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "ю" and kiril[i + 2] == "т"): korean += "츗"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "б" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "뱟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "в" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "뱟"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "г" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "걋"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "д" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "댯"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "з" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "쟛"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "к" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "꺗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "л" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "럇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "м" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "먓"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "н" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "냣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "п" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "뺫"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "р" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "럇"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "с" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "샷"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "т" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "땻"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ф" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "퍗"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "х" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "햣"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ц" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "쨧"; a2 = 2; continue
        if (i + 2 == len(kiril) - 1 or (i + 3 <= len(kiril) - 1 and kiril[i + 3] == "ь")) and (kiril[i] == "ч" and kiril[i + 1] == "я" and kiril[i + 2] == "т"): korean += "챳"; a2 = 2; continue

        if (i + 2 == len(kiril) - 1) and (kiril[i] == "а" and kiril[i + 1] == "т"): korean += "앗"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "е" and kiril[i + 1] == "т"): korean += "옛"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "ё" and kiril[i + 1] == "т"): korean += "욧"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "и" and kiril[i + 1] == "т"): korean += "잇"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "й" and kiril[i + 1] == "т"): korean += "잇"; a2 = 1; continue
        if (i+3 == len(kiril)-1) and (kiril[i]+kiril[i+1] == "о́" and kiril[i+2] == "т"): korean += "옷"; a2=2; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "о" and kiril[i + 1] == "т"): korean += "앗"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "у" and kiril[i + 1] == "т"): korean += "웃"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "ы" and kiril[i + 1] == "т"): korean += "읫"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "э" and kiril[i + 1] == "т"): korean += "엣"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "ю" and kiril[i + 1] == "т"): korean += "윳"; a2 = 1; continue
        if (i + 2 == len(kiril) - 1) and (kiril[i] == "я" and kiril[i + 1] == "т"): korean += "얏"; a2 = 1; continue

        if (i + 2 < len(kiril) - 1) and (kiril[i] == "а" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "앗"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "е" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "옛"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "ё" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "욧"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "и" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "잇"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "й" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "잇"; a2 = 1; continue
        # if (i + 2 < len(kiril) - 1) and (kiril[i] == "о" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "앗"; a2 = 1; continue
        if (i+3 < len(kiril) - 1) and (kiril[i]+kiril[i+1] == "о́" and kiril[i+2] == "т" and kiril[i+3] not in vowels): korean += "옷"; a2=2; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "у" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "웃"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "ы" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "읫"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "э" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "엣"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "ю" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "윳"; a2 = 1; continue
        if (i + 2 < len(kiril) - 1) and (kiril[i] == "я" and kiril[i + 1] == "т" and kiril[i+2] not in vowels): korean += "얏"; a2 = 1; continue


















        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "а"): korean += "싸"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "е"): korean += "쎼"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ё"): korean += "쑈"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "и"): korean += "씨"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "й"): korean += "씨"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "о"): korean += "싸"; a2=2; continue
        if (i+3 <= len(kiril)-1) and (kiril[i] == "с" and kiril[i+1] == "с" and kiril[i+2]+kiril[i+3] == "о́"): korean += "쏘"; a2=3; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "у"): korean += "쑤"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ы"): korean += "씌"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "э"): korean += "쎄"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "ю"): korean += "쓔"; a2=2; continue
        if (i + 2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "с" and kiril[i + 2] == "я"): korean += "쌰"; a2=2; continue







        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "а"): korean += "바"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "а"): korean += "바"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "а"): korean += "가"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "а"): korean += "다"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "а"): korean += "자"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "а"): korean += "까"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "а"): korean += "라"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "а"): korean += "마"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "а"): korean += "나"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "а"): korean += "빠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "а"): korean += "라"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "а"): korean += "사"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "а"): korean += "따"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "а"): korean += "파"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "а"): korean += "하"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "а"): korean += "짜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "а"): korean += "차"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "е"): korean += "볘"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "е"): korean += "볘"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "е"): korean += "계"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "е"): korean += "뎨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "е"): korean += "졔"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "е"): korean += "꼐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "е"): korean += "례"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "е"): korean += "몌"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "е"): korean += "녜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "е"): korean += "뼤"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "е"): korean += "례"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "е"): korean += "셰"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "е"): korean += "뗴"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "е"): korean += "폐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "е"): korean += "혜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "е"): korean += "쪠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "е"): korean += "쳬"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ё"): korean += "뵤"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ё"): korean += "뵤"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ё"): korean += "교"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ё"): korean += "됴"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ё"): korean += "죠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ё"): korean += "꾜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ё"): korean += "료"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ё"): korean += "묘"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ё"): korean += "뇨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ё"): korean += "뾰"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ё"): korean += "료"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ё"): korean += "쇼"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ё"): korean += "뚀"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ё"): korean += "표"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ё"): korean += "효"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ё"): korean += "쬬"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ё"): korean += "쵸"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "и"): korean += "비"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "и"): korean += "비"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "и"): korean += "기"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "и"): korean += "디"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "и"): korean += "지"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "и"): korean += "끼"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "и"): korean += "리"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "и"): korean += "미"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "и"): korean += "니"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "и"): korean += "삐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "и"): korean += "리"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и"): korean += "시"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "и"): korean += "시"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "и"): korean += "띠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "и"): korean += "피"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "и"): korean += "히"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "и"): korean += "찌"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "и"): korean += "치"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "й"): korean += "비"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "й"): korean += "비"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "й"): korean += "기"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "й"): korean += "디"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "й"): korean += "지"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "й"): korean += "끼"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "й"): korean += "리"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "й"): korean += "미"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "й"): korean += "니"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "й"): korean += "삐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "й"): korean += "리"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "й"): korean += "시"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "й"): korean += "띠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "й"): korean += "피"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "й"): korean += "히"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "й"): korean += "찌"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "й"): korean += "치"; a2=1; continue


        if (i+2 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i+1]+kiril[i+2] == "о́"): korean += "보"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i+1]+kiril[i+2] == "о́"): korean += "보"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i+1]+kiril[i+2] == "о́"): korean += "고"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i+1]+kiril[i+2] == "о́"): korean += "도"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i+1]+kiril[i+2] == "о́"): korean += "조"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i+1]+kiril[i+2] == "о́"): korean += "꼬"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i+1]+kiril[i+2] == "о́"): korean += "로"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i+1]+kiril[i+2] == "о́"): korean += "모"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i+1]+kiril[i+2] == "о́"): korean += "노"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i+1]+kiril[i+2] == "о́"): korean += "뽀"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i+1]+kiril[i+2] == "о́"): korean += "로"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i+1]+kiril[i+2] == "о́"): korean += "소"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i+1]+kiril[i+2] == "о́"): korean += "또"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i+1]+kiril[i+2] == "о́"): korean += "포"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i+1]+kiril[i+2] == "о́"): korean += "호"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i+1]+kiril[i+2] == "о́"): korean += "쪼"; a2=2; continue
        if (i+2 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i+1]+kiril[i+2] == "о́"): korean += "초"; a2=2; continue


        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "о"): korean += "바"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "о"): korean += "바"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "о"): korean += "가"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "о"): korean += "다"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "о"): korean += "자"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "о"): korean += "까"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "о"): korean += "라"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "о"): korean += "마"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "о"): korean += "나"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "о"): korean += "빠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "о"): korean += "라"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "о"): korean += "사"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "о"): korean += "따"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "о"): korean += "파"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "о"): korean += "하"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "о"): korean += "짜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "о"): korean += "차"; a2=1; continue


        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "у"): korean += "부"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "у"): korean += "부"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "у"): korean += "구"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "у"): korean += "두"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "у"): korean += "주"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "у"): korean += "꾸"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "у"): korean += "루"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "у"): korean += "무"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "у"): korean += "누"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "у"): korean += "뿌"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "у"): korean += "루"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "у"): korean += "수"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "у"): korean += "뚜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "у"): korean += "푸"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "у"): korean += "후"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "у"): korean += "쭈"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "у"): korean += "추"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ы"): korean += "븨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ы"): korean += "븨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ы"): korean += "긔"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ы"): korean += "듸"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ы"): korean += "즤"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ы"): korean += "끠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ы"): korean += "릐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ы"): korean += "믜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ы"): korean += "늬"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ы"): korean += "쁴"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ы"): korean += "릐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ы"): korean += "싀"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ы"): korean += "띄"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ы"): korean += "픠"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ы"): korean += "희"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ы"): korean += "쯰"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ы"): korean += "츼"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "э"): korean += "베"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "э"): korean += "베"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "э"): korean += "게"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "э"): korean += "데"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "э"): korean += "제"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "э"): korean += "께"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "э"): korean += "레"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "э"): korean += "메"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "э"): korean += "네"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "э"): korean += "뻬"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "э"): korean += "레"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "э"): korean += "세"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "э"): korean += "떼"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "э"): korean += "페"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "э"): korean += "헤"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "э"): korean += "쩨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "э"): korean += "체"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "ю"): korean += "뷰"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "ю"): korean += "뷰"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "ю"): korean += "규"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "ю"): korean += "듀"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "ю"): korean += "쥬"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "ю"): korean += "뀨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "ю"): korean += "류"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "ю"): korean += "뮤"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "ю"): korean += "뉴"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "ю"): korean += "쀼"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "ю"): korean += "류"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "ю"): korean += "슈"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "ю"): korean += "뜌"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "ю"): korean += "퓨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "ю"): korean += "휴"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "ю"): korean += "쮸"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "ю"): korean += "츄"; a2=1; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "я"): korean += "뱌"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "я"): korean += "뱌"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "я"): korean += "갸"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "я"): korean += "댜"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "я"): korean += "쟈"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "я"): korean += "꺄"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "я"): korean += "랴"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "я"): korean += "먀"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "я"): korean += "냐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "я"): korean += "뺘"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "я"): korean += "랴"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "я"): korean += "샤"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "я"): korean += "땨"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "я"): korean += "퍄"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "я"): korean += "햐"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "я"): korean += "쨔"; a2=1; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "я"): korean += "챠"; a2=1; continue

        if kiril[i] == "а": korean += "아"; continue
        if kiril[i] == "е": korean += "예"; continue
        if kiril[i] == "ё": korean += "요"; continue
        if kiril[i] == "и": korean += "이"; continue
        if kiril[i] == "й": korean += "이"; continue
        if (i+1 <= len(kiril)-1) and (kiril[i]+kiril[i+1] == "о́"): korean += "오"; a2=1; continue
        if kiril[i] == "о": korean += "아"; continue
        if kiril[i] == "у": korean += "우"; continue
        if kiril[i] == "ы": korean += "의"; continue
        if kiril[i] == "э": korean += "에"; continue
        if kiril[i] == "ю": korean += "유"; continue
        if kiril[i] == "я": korean += "야"; continue

        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "б" and kiril[i + 1] == "л"): korean += "블"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "в" and kiril[i + 1] == "л"): korean += "블"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "г" and kiril[i + 1] == "л"): korean += "글"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "д" and kiril[i + 1] == "л"): korean += "들"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ж" and kiril[i + 1] == "л"): korean += "쥘"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "з" and kiril[i + 1] == "л"): korean += "즐"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "к" and kiril[i + 1] == "л"): korean += "끌"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "л" and kiril[i + 1] == "л"): korean += "를"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "м" and kiril[i + 1] == "л"): korean += "믈"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "н" and kiril[i + 1] == "л"): korean += "늘"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "п" and kiril[i + 1] == "л"): korean += "쁠"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "р" and kiril[i + 1] == "л"): korean += "를"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i + 1] == "л"): korean += "슬"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "т" and kiril[i + 1] == "л"): korean += "뜰"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ф" and kiril[i + 1] == "л"): korean += "플"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "х" and kiril[i + 1] == "л"): korean += "흘"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ц" and kiril[i + 1] == "л"): korean += "쯜"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ч" and kiril[i + 1] == "л"): korean += "츨"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "ш" and kiril[i + 1] == "л"): korean += "쉴"; continue
        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "щ" and kiril[i + 1] == "л"): korean += "실"; continue


        if (i + 1 <= len(kiril) - 1) and (kiril[i] == "с" and kiril[i+1] == "с"): korean += "쓰"; a2=1; continue


        if kiril[i] == "б": korean += "브"; continue
        if kiril[i] == "в": korean += "브"; continue
        if kiril[i] == "г": korean += "그"; continue
        if kiril[i] == "д": korean += "드"; continue
        if kiril[i] == "ж": korean += "쥐"; continue
        if kiril[i] == "з": korean += "즈"; continue
        if kiril[i] == "к": korean += "끄"; continue
        if kiril[i] == "л": korean += "르"; continue
        if kiril[i] == "м": korean += "므"; continue
        if kiril[i] == "н": korean += "느"; continue
        if kiril[i] == "п": korean += "쁘"; continue
        if kiril[i] == "р": korean += "르"; continue
        if kiril[i] == "с": korean += "스"; continue
        if kiril[i] == "т": korean += "뜨"; continue
        if kiril[i] == "ф": korean += "프"; continue
        if kiril[i] == "х": korean += "흐"; continue
        if kiril[i] == "ц": korean += "쯔"; continue
        if kiril[i] == "ч": korean += "츠"; continue
        if kiril[i] == "ш": korean += "쉬"; continue
        if kiril[i] == "щ": korean += "시"; continue


    return korean




def input_Text(st):

    st = st.lower().replace("  ", " ").replace("\n", " ").replace("-", " ").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace(",", "").replace(".", "").replace("q", "").replace("w", "").replace("e", "").replace("r", "").replace("t", "").replace("y", "").replace("u", "").replace("i", "").replace("o", "").replace("p", "").replace("[", "").replace("]", "").replace("a", "").replace("s", "").replace("d", "").replace("f", "").replace("g", "").replace("h", "").replace("j", "").replace("k", "").replace("l", "").replace(":", "").replace("'", "").replace("z", "").replace("x", "").replace("c", "").replace("v", "").replace("b", "").replace("n", "").replace("m", "").replace("<", "").replace(">","").replace("/", "").replace("?", "")
    st = st.replace("1", "").replace("1", "").replace("1", "").replace("1", "").replace("1", "").replace("1", "")
    nowords = ["не", "но", "о", "в", "что", "как", "к", "на", "за", "быть", "и", "так", "нет", "уже", "не", "не", "не", "не", "не", "не", "не"]

    st = "union " + st
    st = st.replace("union ", "")
    st += " "

    list = []
    list_temp1 = []
    list_temp_count = 0
    j = 0
    for i in range(0, len(st)):
        if st[i] == " ":
            list_temp = ""
            for j in range(list_temp_count, i):
                if st[j] != " ": list_temp += st[j]

            if list_temp != "": list_temp1.append(list_temp)
            list_temp = ""
            if j != 0: list_temp_count = j + 2

    for i in range(0, len(list_temp1)):
        if list_temp1[i] not in nowords:
            list.append(list_temp1[i])

    return list




def get_Original(list):

    list_original = []
    list_stress = []
    list_korean = []
    list_meaning = []

    list_original_text = ""
    j = 0
    print("kiril")
    print(list)
    for i in range(0, len(list)):
        print("https://www.multitran.com/c/m.exe?l1=1&l2=2&s=" + list[i])
        html = requests.get("https://www.multitran.com/c/m.exe?l1=1&l2=2&s=" + list[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")

        if str(type(obj.find("td", {"class": "gray"}))) == "<class 'bs4.element.Tag'>":

            tds = obj.findAll("td", {"class": "trans"})[0]
            as1 = tds.find("a").text
            list_meaning.append(as1)

            tds = obj.find("td", {"class": "gray"}).text.replace("\n", "").replace("\r", "").replace("\xa0", "").replace(" n", "").replace(" v", "").replace(" adj.", "").replace(" adv.", "").replace(" abbr.", "")
            list_original.append(tds)

            html = requests.get("https://www.multitran.com/m.exe?a=118&l1=2&l2=1&init=1&s=" + tds, verify = False)
            obj = bs4.BeautifulSoup(html.content, "html.parser")
            divs = obj.find("div", {"style":"margin-top:0.2em;margin-bottom:0.2em;"})

            if str(divs) == "None":
                tds7 = obj.findAll("td", {"class": "wordforms"})[1].text
                list_stress.append(tds7)
                list_korean.append(to_Korean(tds7.lower()))
                print(tds7 + " [" + list_korean[j] + "] " + list_meaning[j])
            else:
                tds7 = divs.findAll("td")
                if tds7[1].text == " Мужской род":
                    list_stress.append(tds7[6].text.replace("\xa0", ""))
                    list_korean.append(to_Korean(tds7[6].text.lower()))
                    print(tds7[6].text + " [" + list_korean[j] + "] " + list_meaning[j])
                elif tds7[1].text == " Единственное число":
                    list_stress.append(tds7[4].text.replace("\xa0", ""))
                    list_korean.append(to_Korean(tds7[4].text.lower()))
                    print(tds7[4].text + " [" + list_korean[j] + "] " + list_meaning[j])
                else:
                    list_stress.append(tds7[1].text.replace("\xa0", ""))
                    list_korean.append(to_Korean(tds7[1].text.lower()))
                    print(tds7[1].text + " [" + list_korean[j] + "] " + list_meaning[j])

            j += 1

    print("")
    print(list_stress)
    print("")


    return list_original, list_korean, list_meaning







list_original = []























def get_Original_Word(list):
    html = requests.get("https://www.wordreference.com/ruen/" + list)
    soup = bs4.BeautifulSoup(html.text, "html.parser")

    div = soup.find("div", {"id": "otherDicts"})
    span = div.find("span", {"class": "hw"})


    if span:
        stress = span.text.replace("|", "")

        a = div.select("a")
        meaning = "   ".join(meaning_a.text for meaning_a in a[:3])


    else:
        html = requests.get("https://en.wiktionary.org/wiki/" + list)
        soup = bs4.BeautifulSoup(html.text, "html.parser")


        i = soup.find("i", {"class": "Cyrl mention"})


        if i:
            stress = i.text.replace("|", "")

        
            html = requests.get("https://www.wordreference.com/ruen/" + stress)
            soup = bs4.BeautifulSoup(html.text, "html.parser")

            div = soup.find("div", {"id": "otherDicts"})
            a = div.select("a")
            meaning = "   ".join(meaning_a.text for meaning_a in a[:3])
        else:
            stress = ""
            meaning = ""

    korean = to_Korean(stress.lower())

    return stress, korean, meaning




















def get_Meaning(list_original, list_korean, list_meaning):

    list_meaning7 = []
    list_meaning8 = []
    list_meaning88 = []
    list_meaning888 = []

    for i in range(0, len(list_original)):
        html = requests.get("https://tr-ex.me/translation/russian-english/" + list_original[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")
        if len(obj.findAll("a", {"class": "translation"})) != 0:
            as1 = obj.findAll("a", {"class": "translation"})[0].text
        else:
            as1 = ""
        list_meaning7.append(as1)

        html = requests.get("https://www.wordreference.com/ruen/" + list_original[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")

        spans = obj.find("div", {"id": "otherDicts"})
        if len(spans.findAll("a")) != 0:
            as1 = spans.findAll("a")[0].text
        else:
            as1 = ""
        list_meaning8.append(as1)

        html = requests.get("https://en.openrussian.org/ru/" + list_original[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")

        if str(type(obj.find("p", {"class": "tl"}))) != "<class 'NoneType'>":
            spans = obj.find("p", {"class": "tl"}).text
        else:
            spans = ""
        list_meaning88.append(spans)


        html = requests.get("https://dic.daum.net/search.do?dic=ru&q=" + list_original[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")
        if str(type(obj.find("div", {"class": "search_word"}))) != "<class 'NoneType'>":
            divs = obj.find("div", {"class": "search_word"})
            as1 = divs.find("a").text
        else:
            as1 = ""
        list_meaning888.append(as1)

        print(list_original[i] + " [" + list_korean[i] + "] " + list_meaning[i] + " * " + list_meaning7[i] + " * " + list_meaning8[i] + " * " + list_meaning88[i] + " * " + list_meaning888[i])
    print(str(i + 1) + " 건 완료")






















def get_Stress_Meaning(st):
    st = st.lower().replace("  ", " ").replace("\n", " ").replace("-", " ").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace(",", "").replace(".", "").replace("q", "").replace("w", "").replace("e", "").replace("r", "").replace("t", "").replace("y", "").replace("u", "").replace("i", "").replace("o", "").replace("p", "").replace("[", "").replace("]", "").replace("a", "").replace("s", "").replace("d", "").replace("f", "").replace("g", "").replace("h", "").replace("j", "").replace("k", "").replace("l", "").replace(":", "").replace("'", "").replace("z", "").replace("x", "").replace("c", "").replace("v", "").replace("b", "").replace("n", "").replace("m", "").replace("<", "").replace(">",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "").replace(
        "/", "").replace("?", "")
    st = st.replace("1", "").replace("1", "").replace("1", "").replace("1", "").replace("1", "").replace("1", "")
    nowords = ["не", "но", "в", "что", "как", "к", "на", "за", "быть", "и", "так", "нет", "уже", "не", "не", "не", "не", "не", "не", "не"]

    st = "union " + st
    st = st.replace("union ", "")
    st += " "


    list = []
    list_temp1 = []
    list_temp_count = 0

    j = 0
    for i in range(0, len(st)):
        if st[i] == " ":
            list_temp = ""
            for j in range(list_temp_count, i):
                if st[j] != " ": list_temp += st[j]

            if list_temp != "": list_temp1.append(list_temp)
            list_temp = ""
            if j != 0: list_temp_count = j + 2

    for i in range(0, len(list_temp1)):
        if list_temp1[i] not in nowords:
            list.append(list_temp1[i].lower())



    list_korean = []
    list_meaning = []
    list_meaning7 = []
    list_meaning8 = []
    list_meaning88 = []

    list_original_text = ""
    for i in range(0, len(list)):
        html = requests.get("https://www.multitran.com/c/m.exe?l1=1&l2=2&s=" + list[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")

        if str(type(obj.find("td", {"class": "gray"}))) == "<class 'bs4.element.Tag'>":
            tds = obj.findAll("td", {"class": "trans"})[0]
            as1 = tds.find("a").text
            list_meaning.append(as1)
        else:
            list_meaning.append("")
        list_korean.append(to_Korean(list[i]))

        html = requests.get("https://tr-ex.me/translation/russian-english/" + list[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")
        if len(obj.findAll("a", {"class": "translation"})) != 0:
            as1 = obj.findAll("a", {"class": "translation"})[0].text
        else:
            as1 = ""
        list_meaning7.append(as1)

        html = requests.get("https://www.wordreference.com/ruen/" + list[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")

        spans = obj.find("div", {"id": "otherDicts"})
        if len(spans.findAll("a")) != 0:
            as1 = spans.findAll("a")[0].text
        else:
            as1 = ""
        list_meaning8.append(as1)

        html = requests.get("https://en.openrussian.org/ru/" + list[i], verify = False)
        obj = bs4.BeautifulSoup(html.content, "html.parser")

        if str(type(obj.find("p", {"class": "tl"}))) != "<class 'NoneType'>":
            spans = obj.find("p", {"class": "tl"}).text
        else:
            spans = ""
        list_meaning88.append(spans)

        print(list[i] + " [" + list_korean[i] + "] " + list_meaning[i] + " * " + list_meaning7[i] + " * " + list_meaning8[i] + " * " + list_meaning88[i])

    print(str(i + 1) + "건 완료")
