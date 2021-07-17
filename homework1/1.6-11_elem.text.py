#!/usr/bin/env pyhton3
"""

"""
import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"

try:
    wd = webdriver.Chrome()
    wd.get(link)

    input1 = wd.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")

    input2 = wd.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")

    input3 = wd.find_element_by_css_selector(".first_block .third")
    input3.send_keys("ipetrov@gmail.com")

    submit_btn = wd.find_element_by_css_selector("button.btn")
    submit_btn.click()

    time.sleep(1)

    welcome_el = wd.find_element_by_tag_name("h1")
    welcome_text = welcome_el.text

    assert welcome_text == "Congratulations! You have successfully registered!"
finally:
    time.sleep(3)
    wd.quit()
