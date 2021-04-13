from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
   driver.get('http://test-stage.geekbrains.ru:8080\login')
   driver.find_element_by_name("email").send_keys("test1@test.ru")
   driver.find_element_by_name('password').send_keys("123456")
   driver.find_element_by_css_selector("button.button.is-block.is-info.is-large.is-fullwidth").click()
   driver.find_element(By.XPATH,"/html/body/section/div[2]/div/div/aside/ul/li[2]/a").click()
   driver.find_element(By.NAME, "name").send_keys("test")
   driver.find_element(By.NAME, "surname").send_keys("test")
   driver.find_element(By.NAME, "email").send_keys("test@test.ru")
   driver.find_element(By.NAME, "city").send_keys("Krakov")
   driver.find_element_by_css_selector("button.button.is-block.is-info.is-large.is-fullwidth").click()
   time.sleep(5)
finally:
   driver.quit()
