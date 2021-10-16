import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Safari()
driver.get("https://egrul.nalog.ru/index.html")

query_form = driver.find_element(By.ID, 'query')
query_form.clear()
query_form.send_keys("9705093554")

find_button = driver.find_element(By.ID, 'btnSearch')
find_button.click()

time.sleep(3)
data = driver.find_element(By.CLASS_NAME, 'res-text').text.split(',')
data[0] = 'Адрес: ' + data[0]


print(1)