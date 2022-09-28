from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import config
import time

class InstaFollower():

  def __init__(self):
    options = Options()
    options.add_argument("start-maximized")
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
  
  def login(self):
    self.driver.get("https://www.instagram.com/accounts/login/")
    self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
    time.sleep(1)

    login_box = self.driver.find_elements(By.CLASS_NAME, 'zyHYP')
    login_box[0].send_keys(config.email)
    login_box[1].send_keys(config.password)
    submit = self.driver.find_element(By.CLASS_NAME, 'y3zKF')
    submit.click()
    time.sleep(5)
  
  def find_followers(self):
    self.driver.get(f"https://www.instagram.com/{config.account_to_follow}/followers/")
    time.sleep(5)

  def follow(self):
    follow_buttons = self.driver.find_elements(By.CLASS_NAME, '_acas')
    for each in follow_buttons:
      try:
        each.click()
      except ElementClickInterceptedException:
        self.driver.find_element(By.CLASS_NAME, '_a9_1').click()
      time.sleep(1)
