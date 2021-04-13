from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get('http://test-stage.geekbrains.ru:8080\login')
    driver.find_element_by_name("email").send_keys("test1@test.ru")
    driver.find_element_by_name('password').send_keys("123456")
    driver.find_element_by_css_selector("button.button.is-block.is-info.is-large.is-fullwidth").click()
    driver.find_element(By.XPATH," /html/body/section/div[2]/div/div/aside/ul/li[1]/a").click()
    driver.find_element(By.NAME,'test').send_keys("test_or_test")
    driver.find_element_by_css_selector("button.button.is-block.is-info.is-large.is-fullwidth").click()
    assert driver.find_element_by_css_selector('.notification.is-success').text == 'Успех.', "Не  успех"
    driver.find_element(By.NAME, 'field4').send_keys("test_all")
    driver.find_element_by_css_selector("button.button.is-block.is-info.is-large.is-fullwidth").click()
    assert  not driver.find_elementby_css_selector('.notification.is-danger').text == "Правильное поле.","Неправильное поле."
    time.sleep(5)
finally:
   driver.quit()
