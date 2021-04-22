from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


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
    browser.get('http://test-stage.geekbrains.ru:8080/three_button')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(10)"))).click()
    wait.until(EC.alert_is_present())
    prompt = browser.switch_to.alert
    assert "Как тебя зовут?" in prompt.text
    prompt.send_keys("Kitty")
    prompt.accept()
    assert  not browser.find_element_by_css_selector('#prompt_text').text == "Привет,Kitty"
    browser.refresh()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(10)"))).click()
    wait.until(EC.alert_is_present())
    prompt.dismiss()
    assert  not browser.find_element_by_css_selector('#prompt_text').text == "Не ответили на вопрос :"
finally:
   browser.quit()