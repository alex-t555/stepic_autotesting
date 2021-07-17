"""
test_items.py
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_exist_button_add_to_basket_on_product_page(browser: WebDriver) -> None:
    browser.get(link)
    button_is_exist = True
    try:
        browser.find_element_by_css_selector('#add_to_basket_form button.btn-add-to-basket')
    except NoSuchElementException:
        button_is_exist = False
    assert button_is_exist, 'Button "add to basket" does not exist on product page.'