#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: вывод PyTest

Попробуйте запустить ваши тесты из урока 3.2
https://stepik.org/lesson/36285/step/13 с помощью PyTest. В выводе найдите
последнюю строку, скопируйте её и отправьте в это задание. Отправьте текст,
который находится между  === и ===. 
"""

import time
from selenium import webdriver
import pytest


@pytest.fixture
def wd():
    _wd = webdriver.Chrome()
    yield _wd
    _wd.close()


def test_1(wd):
    LINK = "http://suninjuly.github.io/registration1.html"
    wd.get(LINK)
    input1 = wd.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = wd.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = wd.find_element_by_css_selector(".first_block .third")
    input3.send_keys("ipetrov@gmail.com")
    wd.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    welcome_text = wd.find_element_by_tag_name("h1").text

    assert welcome_text == "Congratulations! You have successfully registered!"


def test_2(wd):
    LINK = "http://suninjuly.github.io/registration2.html"
    wd.get(LINK)
    input1 = wd.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = wd.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = wd.find_element_by_css_selector(".first_block .third")
    input3.send_keys("ipetrov@gmail.com")
    wd.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    welcome_text = wd.find_element_by_tag_name("h1").text

    assert welcome_text == "Congratulations! You have successfully registered!"