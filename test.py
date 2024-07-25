from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

#driver = webdriver.Chrome()

#driver.quit()

requests = requests.get("https://www.cnn.com/").text
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'


soup = BeautifulSoup(requests, features="html.parser")

print(soup.a.prettify())

headlines = soup.find_all('a',href=True)

for headline in headlines:
    if headline['href'] and headline['href'][0:5] == '/2024':
        print(headline['href'])

