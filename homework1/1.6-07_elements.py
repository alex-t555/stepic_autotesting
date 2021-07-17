#!/usr/bin/env python3
"""
"""
import time
from selenium import webdriver

url = "http://suninjuly.github.io/huge_form.html"

try:
    wd = webdriver.Chrome()
    wd.get(url)

    elements = wd.find_elements_by_tag_name("input")
    for el in elements:
        el.send_keys("pass")

    submit = wd.find_element_by_css_selector("button.btn")
    submit.click()
finally:
    time.sleep(30)
    wd.quit()
