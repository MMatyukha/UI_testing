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
    browser.get('http://test-stage.geekbrains.ru:8080/open_new_window')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button"))).click()
    print(browser.window_handles)
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    first_window_w =browser.switch_to.window(first_window)
    first_window_url=browser.current_url
    second_window_w = browser.switch_to.window(second_window)
    second_window_url = browser.current_url
    print('Заголовок страницы 1: ' + browser.title + ',' + ' адрес страницы: ' + first_window_url)
    print('Заголовок страницы: ' + browser.title + ',' + ' адрес страницы: ' + second_window_url)
    browser.switch_to.window(second_window)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button"))).click()
    assert alert_present(),'Успех!'
    confirm = browser.switch_to.alert
    confirm.accept()
    print(browser.window_handles)
finally:
   browser.quit()