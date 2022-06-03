import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

class Github:
  def __init__(self, username: str, password: str, ch: str, name: str) -> None:
    self.username = username,
    self.password = password,
    self.ch = ch, 
    self.name = name

  def login(self) -> bool:
    try:
      driver.get('https://github.com/login')
       

      WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="login_field"]'))
      )
      email = driver.find_element(by=By.XPATH,value='//*[@id="login_field"]')
      email.send_keys(self.username)

      passw = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
      passw.send_keys(self.password)

      signiin = driver.find_element(by=By.XPATH, value='//*[@id="login"]/div[4]/form/div/input[12]')
      signiin.click()

      time.sleep(3)
      incorrect = driver.find_elements(by=By.XPATH,value='//*[@id="js-flash-container"]')
      if len(incorrect) > 0:

        WebDriverWait(driver, 20).until(
          EC.presence_of_element_located((By.XPATH, '//*[@id="repos-container"]/h2/a'))
        ) 

        new = driver.find_element(by=By.XPATH, value='//*[@id="repos-container"]/h2/a')
        new.click()

        WebDriverWait(driver, 20).until(
          EC.presence_of_element_located((By.XPATH, '//*[@id="repository_name"]'))
        )

        repo_name = driver.find_element(by=By.XPATH, value='//*[@id="repository_name"]')
        repo_name.send_keys(self.name)

        if self.ch == 'Public':
          public = driver.find_element(by=By.XPATH, value='//*[@id="repository_visibility_public"]')
          public.click()

        else:
          private = driver.find_element(by=By.XPATH, value='//*[@id="repository_visibility_private"]')
          private.click()

        time.sleep(3)
        create = driver.find_element(by=By.XPATH, value='//*[@id="new_repository"]/div[5]/button')
        create.click()
        return True
      else:
        return False

    except Exception as e:
      return e

