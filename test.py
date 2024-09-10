from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor
import re

def cleanList(list):
    for i in range(0,list.count('')):
        list.remove('')
    return list

def parseHeadline(headline):
    returnList = []
    nextPage = requests.get(headline).text
    nextSoup = BeautifulSoup(nextPage,"html.parser")
    texts = nextSoup.find_all("p")
    for p in texts:
        tempString = p.text
        tempString = re.sub(r'[^a-zA-Z0-9 ]', '', tempString)
        tempList = list(tempString.split(" "))
        tempList = [word.lower() for word in tempList]
        if tempList.count('') > 0:
            tempList = cleanList(tempList)
        returnList.append(tempList)
    return returnList

def main():
    request = requests.get("https://www.cnn.com/").text
    markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'


    soup = BeautifulSoup(request, features="html.parser")

    headlines = ["https://www.cnn.com" + a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("/2024")]

    headlines = list(set(headlines))
    for headline in headlines:
        print(headline)
    print(len(headlines))

    with ThreadPoolExecutor() as exe:
        results = exe.map(parseHeadline,headlines)


    searchTerm = "trump"
    for result in results:
        for i in range(0,len(result)):
            if searchTerm in result[i]:
                print(headlines[i])
                break
