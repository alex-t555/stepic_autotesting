#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: ПОИСК ЭЛЕМЕНТА ПО XPATH

На этот раз воспользуемся возможностью искать элементы по XPath.

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же
форму регистрации, как в шаге 3, при этом в нее добавилась куча одинаковых
кнопок отправки. Но сработает только кнопка с текстом "Submit", и наша задача
нажать в коде именно на неё.

Ваши шаги:
    1. В коде из шага 4 замените ссылку на
    http://suninjuly.github.io/find_xpath_form.
    2. Подберите уникальный XPath-селектор так, чтобы он находил только кнопку
    с текстом Submit. XPath можете формулировать как угодно (по тексту, по
    структуре, по атрибутам) - главное, чтобы он работал.
    3. Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил
    с помощью XPath.
    4. Запустите ваш код.

Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код,
который нужно отправить в качестве ответа на это задание.
"""

import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"

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
    button = wd.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    wd.quit()
