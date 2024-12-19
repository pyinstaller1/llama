



import requests
from bs4 import BeautifulSoup
import re



list = "найду"# "найти"
list = re.sub(r'\u0301', '', list)
print(list)

html = requests.get("https://en.wiktionary.org/wiki/" + list)
soup = BeautifulSoup(html.text, "html.parser")
# i_tag = soup.find("i", {"class": "Cyrl mention"})
div = soup.find("div", {"id": "mw-content-text"})
# print(div)




# v<span class="form-of-definition use-with-mention">
span = soup.find("span", {"class": "form-of-definition use-with-mention"})
print(span)


if span:
    print("span yes")
    i_tag = soup.find("i", {"class": "Cyrl mention"})
    print(i_tag.text)
    
else:
    print("span no")


"""
if i_tag:
    print(i_tag.text)
    print(soup)
else:
    print(1)
    html = requests.get("https://en.wiktionary.org/wiki/" + list)
    soup = BeautifulSoup(html.text, "html.parser")
    print(soup)
"""



