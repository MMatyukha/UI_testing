from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


browser = webdriver.Chrome()
try:
    wait =WebDriverWait(browser,10)
    browser.get('http://test-stage.geekbrains.ru:8080\login')
    wait.until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys("test1@test.ru")
    wait.until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".button"))).click()
    cookies = browser.get_cookies()
    print(cookies)
    browser.delete_all_cookies()
    browser.get('http://test-stage.geekbrains.ru:8080\profile')
    print(browser.current_url)
    wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys("test1@test.ru")
    wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button"))).click()
    cookies = browser.get_cookies()
    print(cookies)
    browser.get('http://test-stage.geekbrains.ru:8080\profile')
    print(browser.current_url)
finally:
    browser.quit()