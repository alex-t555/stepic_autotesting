#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: ПОИСК ЭЛЕМЕНТОВ С ПОМОЩЬЮ SELENIUM

Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с
помощью Selenium. Если всё сделано правильно, то вы увидите окно с проверочным
кодом. Это число вам нужно ввести в качестве ответа в этой задаче.

!Обратите внимание, что время для ввода данных ограничено. Однако благодаря
Selenium вы сможете выполнить задачу до того, как время истечёт.

Для решения этой задачи мы подготовили для вас шаблон кода, в который нужно
только подставить нужные значения для поиска вместо слов value1, value2 и т.д.
Обратите внимание, что значения нужно заключать в кавычки, т.к. они должны
передаваться в виде строки.
"""
import time
from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    input1 = wd.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = wd.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = wd.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = wd.find_element_by_id("country")
    input4.send_keys("Russia")
    button = wd.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    # wd.close()
    wd.quit()
