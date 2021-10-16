from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Safari()
driver.get("https://egrul.nalog.ru/index.html")

query_form = driver.find_element_by_id('query')
query_form.clear()
query_form.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
find_button = driver.find_element_by_id('btnSearch')
driver.find_element_by_id("submit").click()

print(1)