# UI_testing
1.	Составление CSS-селекторов
Составить CSS-селекторы для следующих элементов на странице https://geekbrains.ru/events:
●	логотип GeekBrains:
[class="gb-left-menu__logo "]

 
[class="svg-icon icon-webinar"]

курсы =[class="svg-icon icon-courses"]
1 вебинар =.gb-event-info__item.gb-event-info__title
2.	Составление XPath
логотип GeekBrains= //body[@class=svg-iconicon-logo]
 вебинары= //body[@class= svg-icon icon-webinar]
курсы= //body[@class= svg-icon icon-courses]
1вебинар= //body[@class= gb-event-info__item.gb-event-info__title]

1.	Запуск и завершение браузера
Напишите свой скрипт: запустите браузер, откройте страницу https://geekbrains.ru/events, завершите браузер. В качестве ответа приложите свой скрипт.

from selenium import webdriver
import time

brouser= webdriver.Chrome()
browser.get('https://geekbrains.ru/events')
time.sleep(10)
browser.quit()
