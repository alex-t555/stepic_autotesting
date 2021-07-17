#!/usr/bin/env pyhton3
"""
Задание: переход на новую вкладку

В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно
переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

    - Открыть страницу http://suninjuly.github.io/redirect_accept.html
    - Нажать на кнопку
    - Переключиться на новую вкладку
    - Пройти капчу для робота и получить число-ответ

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Отправьте полученное число в
качестве ответа на это задание.

"""

import time
import math
from selenium import webdriver


def calc(n: str):
    return str(math.log(abs(12*math.sin(int(n)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    wd.find_element_by_css_selector("button.btn").click()
    wd.switch_to.window(wd.window_handles[1])

    x = wd.find_element_by_id("input_value").text
    wd.find_element_by_id("answer").send_keys(calc(x))

    wd.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(20)
    wd.quit()
