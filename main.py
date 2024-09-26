from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor
import re
import json
from flask import request
from flask import Flask, render_template

app = Flask(__name__)


def cleanList(list):
    for i in range(0,list.count('')):
        list.remove('')
    return list

def parseHeadline(headline):
    returnList = [headline]
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

def index():
    return render_template("index.html")

@app.route('/')
def main():
    request = requests.get("https://www.cnn.com/").text
    markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'


    soup = BeautifulSoup(request, features="html.parser")

    headlines = ["https://www.cnn.com" + a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("/2024")]

    headlines = list(set(headlines))

    with ThreadPoolExecutor() as exe:
        results = exe.map(parseHeadline,headlines)

    links = []
    searchTerm = "trump"
    for result in results:
        for i in range(1,len(result)):
            if searchTerm in result[i]:
                links.append(result[0])
                break

    return render_template("index.html",links = links)

if __name__ == "__main__":
    app.run(debug=True)