#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: ЖДЕМ НУЖНЫЙ ТЕКСТ НА СТРАНИЦЕ

Попробуем теперь написать программу, которая будет бронировать нам дом для
отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по
более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий
сценарий:
    - Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    - Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить
    не меньше 12 секунд)
    - Нажать на кнопку "Book"
    - Решить уже известную нам математическую задачу (используйте ранее
    написанный код) и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100, используйте
метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его
в качестве ответа на это задание.

"""

import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(n: str):
    return str(math.log(abs(12*math.sin(int(n)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    WebDriverWait(wd, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    wd.find_element_by_id("book").click()

    x = wd.find_element_by_id("input_value").text
    wd.find_element_by_id("answer").send_keys(calc(x))
    wd.find_element_by_id("solve").click()
finally:
    time.time(20)
    wd.quit()
