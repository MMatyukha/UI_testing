from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
try:
    driver.implicitly_wait(10)
    driver.get('http://test-stage.geekbrains.ru:8080\login')
    driver.find_element_by_name("email").send_keys("test1@test.ru")
    driver.find_element_by_name('password').send_keys("123456")
    driver(EC.element_to_be_clickable((By.CSS_SELECTOR,".button"))).click()
    driver.get('http://test-stage.geekbrains.ru:8080/slow')
    driver.find_element((By.NAME, "text_input"))).send_keys("test")
    driver.find_element((By.ID, "button"))).click()
    driver.find_element((By.NAME, "text_input"))).send_keys("test")
    driver.find_element((By.ID, "button"))).click()
    assert driver.find_element_by_css_selector('.notification.is-success').text == 'Успех.', "Не  успех"
finally:
   driver.quit()