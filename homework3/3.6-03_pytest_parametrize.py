#!/usr/bin/env python3
"""
ЗАДАНИЕ: ПАРАМЕТРИЗАЦИЯ ТЕСТОВ

Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на
правильное решение. Мы смогли локализовать несколько url-адресов задач, где
появляются кусочки сообщений.

Ваша задача — реализовать автотест со следующим сценарием действий:
    - открыть страницу
    - ввести правильный ответ
    - нажать кнопку "Отправить"
    - дождаться фидбека о том, что ответ правильный
    - проверить, что текст в опциональном фидбеке полностью совпадает с
    "Correct!"

Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

Правильным ответом на задачу в заданных шагах является число:

    import time
    import math

    answer = math.log(int(time.time()))

Используйте маркировку pytest для параметризации и передайте в тест список
ссылок в качестве параметров:

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также
настройте нужные ожидания, чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в
опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки
текста в одно предложение и отправьте в качестве ответа на это задание.

ВАЖНО! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас
установлено правильное локальное время (https://time.is/ru/). Ответ для каждой
задачи нужно пересчитывать отдельно, иначе они устаревают.
"""

import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def driver() -> webdriver.Chrome:
    """ func initial and quit driver """
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.mark.parametrize('url', [
                                'https://stepik.org/lesson/236895/step/1',
                                'https://stepik.org/lesson/236896/step/1',
                                'https://stepik.org/lesson/236897/step/1',
                                'https://stepik.org/lesson/236898/step/1',
                                'https://stepik.org/lesson/236899/step/1',
                                'https://stepik.org/lesson/236903/step/1',
                                'https://stepik.org/lesson/236904/step/1',
                                'https://stepik.org/lesson/236905/step/1' ])
def test_time(driver, url):
    """ method test """
    driver.get(url)

    element = WebDriverWait(driver, 12).until(
        lambda d: d.find_element_by_css_selector("textarea.ember-text-area")
    )
    answer = math.log(int(time.time()))
    element.send_keys(str(answer))
    driver.find_element_by_css_selector("button.submit-submission").click()

    element = WebDriverWait(driver, 12).until(
        # lambda d: d.find_element_by_css_selector("div.attempt__message")
        lambda d: d.find_element_by_css_selector("pre.smart-hints__hint")
    )
    # text = driver.find_element_by_css_selector("pre.smart-hints__hint").text
    text = element.text
    assert text == "Correct!"