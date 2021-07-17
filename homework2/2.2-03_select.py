#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: РАБОТА С ВЫПАДАЮЩИМ СПИСКОМ

Для этой задачи мы придумали еще один вариант капчи для роботов. Придется
немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:
    - Открыть страницу http://suninjuly.github.io/selects1.html
    - Посчитать сумму заданных чисел
    - Выбрать в выпадающем списке значение равное расчитанной сумме
    - Нажать кнопку "Submit"

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Отправьте полученное число в
качестве ответа для этого задания.

Когда ваш код заработает, попробуйте запустить его на странице
http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже должен пройти
успешно.

ПОДСКАЗКА: если вы получаете ошибку в духе "argument of type 'int' is not
iterable", перепроверьте тип переменной, которую вы передаете в функцию поиска.
Нужно передать строку!

"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    num1 = wd.find_element_by_id("num1").text
    num2 = wd.find_element_by_id("num2").text

    select = Select(wd.find_element_by_id("dropdown"))
    select.select_by_value(str(int(num1) + int(num2)))

    wd.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(20)
    wd.quit()
