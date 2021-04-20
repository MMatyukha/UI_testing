from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
try:
    wait =WebDriverWait(driver,10)
    driver.get('http://test-stage.geekbrains.ru:8080\login')
    wait.until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys("test1@test.ru")
    wait.until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys("123456")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".button"))).click()
    driver.get('http://test-stage.geekbrains.ru:8080/slow')
    wait.until(EC.element_to_be_clickable((By.NAME, "text_input"))).send_keys("test")
    wait.until(EC.element_to_be_clickable((By.ID, "button"))).click()
    wait.until(EC.element_to_be_clickable((By.NAME, "text_input"))).send_keys("test")
    wait.until(EC.element_to_be_clickable((By.ID, "button"))).click()
	assert driver.find_element_by_css_selector('.notification.is-success').text == 'Успех.', " Поле   не заполнено!"
finally:
   driver.quit()