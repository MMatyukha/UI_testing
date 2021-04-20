from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from   selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_until_clickable(driver, by, value, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

driver_d = webdriver.Chrome()
try:
    wait =WebDriverWait(driver_d,10)
    driver_d.get('http://test-stage.geekbrains.ru:8080\login')
    wait.until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys("test1@test.ru")
    wait.until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".button"))).click()
    driver_d.get('http://test-stage.geekbrains.ru:8080/timer')
    like_locator = (By.CSS_SELECTOR, "label.#demo")
    wait.until(EC.text_to_be_present_in_element(like_locator,'100'))
    driver_d.find_element(By.CSS_SELECTOR,".button").click()
    WebDriverWait(driver_d, 10).until(EC.alert_is_present())
    alert = driver_d.switch_to.alert
     assert "Успех!" in alert.text
finally:
   driver_d.quit()
