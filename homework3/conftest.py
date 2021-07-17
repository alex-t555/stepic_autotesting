#!/usr/bin/env python3
"""
config file pytest

"""
from typing import Generator
from _pytest.config.argparsing import Parser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--browser_name', action='store', default='chrome',
                    help='Choose browser: chrome or firefox')


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print("\nstart browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print("\nquit browser..")
    browser.quit()