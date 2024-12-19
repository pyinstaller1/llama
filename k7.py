



import requests
from bs4 import BeautifulSoup
import re
import urllib3
import warnings



http = urllib3.PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)
warnings.filterwarnings('ignore', category=urllib3.exceptions.InsecureRequestWarning)




list = "беспилотник"
# list = "найду"
# list = "найти"
list = re.sub(r'\u0301', '', list)
print(list)

html = requests.get("https://en.wiktionary.org/wiki/" + list)
soup = BeautifulSoup(html.text, "html.parser")

span = soup.find("span", {"class": "form-of-definition use-with-mention"})



if span:
    print("span yes")
    i_tag = soup.find("i", {"class": "Cyrl mention"})
    print(i_tag.text)

    html = requests.get("https://en.wiktionary.org/wiki/" + re.sub(r'\u0301', '', i_tag.text))
    soup = BeautifulSoup(html.text, "html.parser")




    stress = soup.find("strong", {"class": "Cyrl headword"})
    if stress:
        stress = stress.text
    else:
        stress = ""




    meaning = soup.find_all("span", {"class": "mention-gloss"})
    meaning = "   ".join([a.text for a in meaning[:3]])



    

    if meaning:
        pass
    else:
        meaning = soup.select('ol a')
        meaning = "   ".join([a.text for a in meaning[:3]])


        if meaning:
            pass
        else:
            meaning = ""



        



    

    
else:
    print("span no")

    html = requests.get("https://en.wiktionary.org/wiki/" + list)
    soup = BeautifulSoup(html.text, "html.parser")


    stress = soup.find("strong", {"class": "Cyrl headword"})
    if stress:
        stress = stress.text
    else:
        stress = ""





    
    meaning = soup.find_all("span", {"class": "mention-gloss"})
    meaning = "   ".join([a.text for a in meaning[:3]])


    
    if meaning:
        pass
    else:
        meaning = soup.select('ol a')
        meaning = "   ".join([a.text for a in meaning[:3]])


        if meaning:
            pass
        else:
            meaning = ""













print(stress)
print(meaning)
















