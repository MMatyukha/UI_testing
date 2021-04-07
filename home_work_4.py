1.Ргистрация

from selenium import webdriver
import time

brouser= webdriver.Chrome()
try:
    browser.get("http://test-stage.geekbrains.ru:8080")
    time.sleep(5)
    email_field = browser.find_element_by_name("[email]").send_keys("test@test.ru")
    login = browser.find_element_by_name("[name]").send_keys("test")
    password = browser.find_element_by_name("[password]").send_keys("123456")
    password = browser.find_element_by_class("[button is-block is-info is-large is-fullwidth]").click()
    time.sleep(5)
finally:
   browser.quit()
   
2.Вход

from selenium import webdriver
import time

brouser= webdriver.Chrome()
try:
    browser.get(" http://test-stage.geekbrains.ru:8080/many_fields")
    time.sleep(5)
    print(browser.find_element_by_class_name('test').text)
    assert browser.find_element_by_class_name('field2').text == "Войти", "Неверный текст"
    time.sleep(5)
finally:
   browser.quit()
   
    2. Написание скрипта для заполнения информации о себе
	from selenium import webdriver
import time

brouser= webdriver.Chrome()
try:
    browser.get("http://test-stage.geekbrains.ru:8080/about1")
    time.sleep(5)
	title = browser.find_element(By.CSS_SELECTOR, "h3.title")
    assert title.text == "О себе", "Неверный текст"
    search_field = browser.find_element(By.NAME, "name").send_keys("test")
    search_field = browser.find_element(By.NAME, "surname").send_keys("test")
	search_field = browser.find_element(By.NAME, "email").send_keys("test@test.ru")
    search_field = browser.find_element(By_Name,"city").send_keys("Dublin")
    assert browser.find_element_(By.link_text,"Подтвердить").text == "Подтвердить", "Неверный текст кнопки"
    time.sleep(5)
finally:
   browser.quit()