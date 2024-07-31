from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

#driver = webdriver.Chrome()

#driver.quit()

request = requests.get("https://www.cnn.com/").text
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'


soup = BeautifulSoup(request, features="html.parser")

headlines = soup.find_all('a',href=True)

for headline in headlines:
    if headline['href'] and headline['href'][0:5] == '/2024':
        page = "https://www.cnn.com" + headline['href']
        nextpage = requests.get(page).text
        next = BeautifulSoup(nextpage,"html.parser")
        text = next.find_all("p")
        for p in text:
            print(p.text)

