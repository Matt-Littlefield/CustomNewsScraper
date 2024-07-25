from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#driver = webdriver.Chrome()
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

soup = BeautifulSoup("https://www.cnn.com/2024/07/24/politics/cnn-poll-kamala-harris-donald-trump/index.html",features="html.parser")
print('\n')
print(soup)

#driver.quit()
