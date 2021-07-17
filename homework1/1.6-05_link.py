#!/usr/bin/env python3
"""
ЗАДАНИЕ

На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по
ней:

    1. Добавьте в самый верх своего кода import math
    2. Добавьте команду в код, которая откроет страницу:
        http://suninjuly.github.io/find_link_text
    3. Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который
    нужно найти, зашифрован формулой:
        str(math.ceil(math.pow(math.pi, math.e)*10000))
    (можно вставить данное выражение в свой код, а можно выполнить в
    интерпретаторе, скопировать оттуда результат и уже его использовать в вашем
    коде)

    4. Добавьте команду для клика по найденной ссылке: она перенесет вас на
    форму регистрации

    5. Заполните скриптом форму так же как вы делали в предыдущем шаге урока

    6. После успешного заполнения вы получите код - отправьте его в качестве
    ответа на это задание

ВАЖНО! Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются
реже, чем атрибуты элементов. Но лучше избегать такого метода поиска. Например,
если приложение имеет несколько языков интерфейса, ваши тесты будут проходить
только с определенным языком интерфейса. Применяйте этот метод с осторожностью
и помните про возможные ограничения.
"""
import time
import math
from selenium import webdriver


url = "http://suninjuly.github.io/find_link_text"
s = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    wd = webdriver.Chrome()
    wd.get(url)

    link = wd.find_element_by_link_text(s)
    link.click()

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
    wd.quit()
