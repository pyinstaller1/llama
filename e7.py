



import requests
from bs4 import BeautifulSoup
import re
import urllib3
import warnings



http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
warnings.filterwarnings('ignore', category=urllib3.exceptions.InsecureRequestWarning)





import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("it works very well really in paris.")

lemmas = [token.lemma_ for token in doc if not token.is_stop]
print(lemmas)




print(doc[1].lemma_)
print(doc[1].pos_)
print(doc[1].is_stop)

# print(nlp.Defaults.stop_words)

print(88888888888888)





import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = stopwords.words('english')

# print(stop_words)

print(77777777777777777)






doc = nlp("it shouldn't do very well in paris")

# 불용어를 제외한 단어 추출
filtered_tokens = [token.text for token in doc if not token.is_stop and token.text != '.']

# 결과 출력
print(filtered_tokens)





























word = "work"
print(word)

html = requests.get("https://www.wordreference.com/enko/" + word)
soup = BeautifulSoup(html.text, "html.parser")

span = soup.find("span", {"class": "pronWR tooltip pronWidget"})
pron = "[" + span.text.split("/")[1].replace("ˈ", "")+ "]"
print(pron)


tr = soup.find_all("tr", {"class": "even"})
meaning = ", ".join([tr_meaning.find("td", {"class": "ToWrd"}).contents[0].strip() for tr_meaning in tr[:5*3] if tr_meaning.find("td", {"class": "ToWrd"}) ])
print(meaning)


    
print (word + " [" + pron + "] " + meaning)
















