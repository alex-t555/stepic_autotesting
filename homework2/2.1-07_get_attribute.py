#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: ПОИСК СОКРОВИЩА С ПОМОЩЬЮ GET_ATTRIBUTE

В данной задаче вам нужно с помощью роботов решить ту же математическую задачу,
как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке",
точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:
    - Открыть страницу http://suninjuly.github.io/get_attribute.html.
    - Найти на ней элемент-картинку, который является изображением сундука с
    сокровищами.
    - Взять у этого элемента значение атрибута valuex, которое является
    значением x для задачи.
    - Посчитать математическую функцию от x (сама функция остаётся неизменной).
    - Ввести ответ в текстовое поле.
    - Отметить checkbox "I'm the robot".
    - Выбрать radiobutton "Robots rule!".
    - Нажать на кнопку "Submit".

Для вычисления значения выражения в п.4 используйте функцию calc(x) из
предыдущей задачи.

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже и
нажмите кнопку "Submit", чтобы получить баллы за задание.

"""

import time
import math
from selenium import webdriver


def calc(n: str):
    return str(math.log(abs(12*math.sin(int(n)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    x = wd.find_element_by_id("treasure").get_attribute("valuex")
    wd.find_element_by_id("answer").send_keys(calc(x))
    wd.find_element_by_id("robotCheckbox").click()
    wd.find_element_by_id("robotsRule").click()
    wd.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(20)
    wd.quit()
