from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def wait_until_present(driver, by, value, timeout=10):
  return WebDriverWait(driver, timeout).until(
      EC.presence_of_element_located((by, value))
  )

def alert_present():
   try:
       wait = WebDriverWait(browser, 1)
       wait.until(EC.alert_is_present())
       return True
   except TimeoutException:
       return False

browser = webdriver.Chrome()
try:
    wait =WebDriverWait(browser,10)
    browser.get('http://test-stage.geekbrains.ru:8080\login')
    wait.until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys("test1@test.ru")
    wait.until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".button"))).click()
    browser.get('http://test-stage.geekbrains.ru:8080/iframe')
    browser.switch_to.frame(0)
    browser.find_element_by_css_selector('#photo')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button"))).click()
    assert alert_present(), 'Успех!'
    confirm = browser.switch_to.alert
    confirm.accept()
     
finally:
   browser.quit()