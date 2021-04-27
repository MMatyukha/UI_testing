import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




browser = webdriver.Chrome()
try:
    wait =WebDriverWait(browser,10)
    browser.get('http://test-stage.geekbrains.ru:8080\login')
    first_url = browser.current_url
    wait.until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys("test1@test.ru")
    wait.until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".button"))).click()
    browser.execute_script("document.querySelector('li:nth-child(1) > a').click()")
    url = browser.execute_script('return document.url')
    assert first_url != url
    browser.execute_script("document.querySelector('li:nth-child(2) > a').click()")
    url1 = browser.execute_script('return document.url')
    assert first_url != url1
    browser.execute_script("document.querySelector('li:nth-child(3) > a').click()")
    url2 = browser.execute_script('return document.url')
    assert first_url != url2
    browser.execute_script("document.querySelector('li:nth-child(4) > a').click()")
    url3 = browser.execute_script('return document.url')
    assert first_url != url3
    browser.execute_script("document.querySelector('li:nth-child(4) > a').click()")
    url4 = browser.execute_script('return document.url')
    assert first_url != url4
    browser.execute_script("document.querySelector('li:nth-child(5) > a').click()")
    url6 = browser.execute_script('return document.url')
    assert first_url != url6
    browser.execute_script("document.querySelector('li:nth-child(6) > a').click()")
    url7 = browser.execute_script('return document.url')
    assert first_url != url7
    browser.execute_script("document.querySelector('li:nth-child(7) > a').click()")
    url7_1 = browser.execute_script('return document.url')
    assert first_url != url7_1
    browser.execute_script("document.querySelector('li:nth-child(8) > a').click()")
    url7_2 = browser.execute_script('return document.url')
    assert first_url != url7_2
    browser.execute_script("document.querySelector('li:nth-child(9) > a').click()")
    url7_3 = browser.execute_script('return document.url')
    assert first_url != url7_3
    browser.execute_script("document.querySelector('li:nth-child(10) > a').click()")
    url8 = browser.execute_script('return document.url')
    assert first_url != url8
finally:
    browser.quit()