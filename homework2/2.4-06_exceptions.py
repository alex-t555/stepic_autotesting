#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ:

Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду
browser.find_element_by_id("button") после открытия страницы
http://suninjuly.github.io/cats.html?

"""

from selenium import webdriver


link = "http://suninjuly.github.io/cats.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    wd.find_element_by_id("button").click()
finally:
    wd.quit()
