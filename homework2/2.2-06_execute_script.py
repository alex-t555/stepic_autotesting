#!/usr/bin/env pyhton3
"""
Задание на execute_script

В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться
с ужасным и огромным футером, который дизайнер всё никак не успевает
переделать. Вам потребуется написать код, чтобы:

    - Открыть страницу http://SunInJuly.github.io/execute_script.html.
    - Считать значение для переменной x.
    - Посчитать математическую функцию от x.
    - Проскроллить страницу вниз.
    - Ввести ответ в текстовое поле.
    - Выбрать checkbox "I'm the robot".
    - Переключить radiobutton "Robots rule!".
    - Нажать на кнопку "Submit".

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Отправьте полученное число в
качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, чтобы
сделать прокрутку в область видимости элементов, перекрытых футером.

"""

import time
import math
from selenium import webdriver


def calc(n: str):
    return str(math.log(abs(12*math.sin(int(n)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    x = wd.find_element_by_id("input_value").text
    wd.find_element_by_id("answer").send_keys(calc(x))

    button = wd.find_element_by_css_selector("button.btn")
    wd.execute_script("return arguments[0].scrollIntoView(true);", button)
    wd.find_element_by_id("robotCheckbox").click()
    wd.find_element_by_id("robotsRule").click()
    button.click()
finally:
    time.sleep(20)
    wd.quit()
