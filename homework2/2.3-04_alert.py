#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: ПРИНИМАЕМ ALERT

В этой задаче вам нужно написать программу, которая будет выполнять следующий
сценарий:

    - Открыть страницу http://suninjuly.github.io/alert_accept.html
    - Нажать на кнопку
    - Принять confirm
    - На новой странице решить капчу для роботов, чтобы получить число с ответом

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Отправьте полученное число в
качестве ответа на это задание.

"""

import time
import math
from selenium import webdriver

def calc(n: str):
    return str(math.log(abs(12*math.sin(int(n)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    wd.find_element_by_css_selector("button.btn").click()
    wd.switch_to.alert.accept()

    x = wd.find_element_by_id("input_value").text
    wd.find_element_by_id("answer").send_keys(calc(x))

    wd.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(20)
    wd.quit()
