from audioop import add
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Research():

  def __init__(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc4R0V02lRuWnXP3OIBBZlbyVFH5yGtwfqXaGVAi8_uep0WBQ/viewform")

  def input(self, addresses, links, costs):
    count = 0
    while count < 9:
      addressbox = self.driver.find_elements(By.CLASS_NAME, 'zHQkBf')[0]
      costbox = self.driver.find_elements(By.CLASS_NAME, 'zHQkBf')[1]
      linkbox = self.driver.find_elements(By.CLASS_NAME, 'zHQkBf')[2]
      submit = self.driver.find_element(By.CLASS_NAME, 'Fxmcue')

      addressbox.send_keys(addresses[count])
      costbox.send_keys(costs[count])
      linkbox.send_keys(links[count])
      submit.click()
      time.sleep(2)

      another = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
      another.click()
      time.sleep(2)

      count += 1


