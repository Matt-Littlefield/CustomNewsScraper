from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor

def parseHeadline(headline):
    nextPage = requests.get(headline).text
    nextSoup = BeautifulSoup(nextPage,"html.parser")
    text = nextSoup.find_all("p")
    return text


request = requests.get("https://www.cnn.com/").text
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'


soup = BeautifulSoup(request, features="html.parser")

headlines = ["https://www.cnn.com" + a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("/2024")]
"""
for headline in headlines:
    nextPage = requests.get(headline).text
    nextSoup = BeautifulSoup(nextPage,"html.parser")
    text = nextSoup.find_all("p")
    for p in text:
        print(p.text)
"""
with ThreadPoolExecutor() as exe:
    results = exe.map(parseHeadline,headlines)

for i in range(len(tuple(results))):
    print(results)

"""
for r in results:
    for p in r:
        print(p.text)
    break
"""