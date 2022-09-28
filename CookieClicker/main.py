from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from store import Store

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(1)
driver.find_element('xpath', '//*[@id="langSelect-EN"]').click()
time.sleep(1)

cookie = driver.find_element('xpath', '//*[@id="bigCookie"]')
store = Store(driver)


loop_end_time = time.time() + 300
while time.time() < loop_end_time:
    for _ in range(100):
        cookie.click()
    store.make_purchase()

print(driver.find_element('xpath', '//*[@id="cookies"]').text.split('\n')[1])
