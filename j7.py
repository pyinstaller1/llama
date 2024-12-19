



import requests
from bs4 import BeautifulSoup
import re
import urllib3
import warnings



http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
warnings.filterwarnings('ignore', category=urllib3.exceptions.InsecureRequestWarning)




list = "要"






html = requests.get("https://www.weblio.jp/content/" + list)
soup = BeautifulSoup(html.text, "html.parser")
soup = soup.find("div", class_="kiji")
hiragana = "   ".join([a.text.split("【")[0].split("〔")[0][:8] for a in soup.find_all("h2", class_="midashigo")])
print(hiragana)




html = requests.get("https://dic.daum.net/search.do?dic=jp&q=" + list)
soup = BeautifulSoup(html.text, "html.parser")
meaning = "   ".join([a.text[:8] for a in soup.find_all("span", class_="txt_search")[:8]])
print(meaning)


















