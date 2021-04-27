from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



browser = webdriver.Chrome()
try:
    wait =WebDriverWait(browser,10)
    browser.get('http://test-stage.geekbrains.ru:8080\login')
    wait.until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys("test1@test.ru")
    wait.until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".button"))).click()
    browser.get('http://test-stage.geekbrains.ru:8080\drag_and_drop')
    el_from = browser.find_element_by_css_selector('div#square')
    target = browser.find_element_by_css_selector('#photo')
    action_chains = ActionChains(browser)
    action_chains.click_and_hold(target).move_to_element(el_from).release().perform()
    alert = browser.switch_to.alert
    assert alert.text == 'Успех!'
    alert.accept()
finally:
    browser.quit()