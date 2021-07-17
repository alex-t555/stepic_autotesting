#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: ЗАГРУЗКА ФАЙЛА

В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

    - Открыть страницу http://suninjuly.github.io/file_input.html
    - Заполнить текстовые поля: имя, фамилия, email
    - Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    - Нажать кнопку "Submit"

Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте
полученное число в качестве ответа для этого задания.

"""

import os
import time
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"
path_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "test.txt")

try:
    wd = webdriver.Chrome()
    wd.get(link)

    wd.find_element_by_name("firstname").send_keys("Ivan")
    wd.find_element_by_name("lastname").send_keys("Petrov")
    wd.find_element_by_name("email").send_keys("i.petrov@example.com")
    wd.find_element_by_id("file").send_keys(path_file)

    wd.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(20)
    wd.quit()
