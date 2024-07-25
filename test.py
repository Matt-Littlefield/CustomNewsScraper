from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

#driver = webdriver.Chrome()

#driver.quit()

requests = requests.get("https://www.cnn.com/").text
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'


soup = BeautifulSoup(markup, features="html.parser")

print(soup.a.prettify())
"""
headlines = soup.find_all('a',href=True)

for headline in headlines:
    print(headline.text)
    time.sleep(0.25)
"""



"""
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()
print(text)

"""

"""
driver.get("https://www.cnn.com/2024/07/24/politics/cnn-poll-kamala-harris-donald-trump/index.html")

title = driver.title
message = driver.find_element(by=By.NAME, value="description")

print(message.text)
"""
"""
soup = BeautifulSoup("https://www.cnn.com/2024/07/24/politics/cnn-poll-kamala-harris-donald-trump/index.html",features="html.parser")
print('\n')
print(soup)
"""