#!/usr/bin/env pyhton3
"""
ЗАДАНИЕ: ОФОРМЛЯЕМ ТЕСТЫ В СТИЛЕ UNITTEST

Попробуйте оформить тесты из первого модуля в стиле unittest.
    - Возьмите тесты из шага —
    https://stepik.org/lesson/138920/step/11?unit=196194
    - Создайте новый файл
    - Создайте в нем класс с тестами, который должен наследоваться от
    unittest.TestCase по аналогии с предыдущим шагом
    - Перепишите в стиле unittest тест для страницы
    http://suninjuly.github.io/registration1.html
    - Перепишите в стиле unittest второй тест для страницы
    http://suninjuly.github.io/registration2.html
    - Оформите финальные проверки в тестах в стиле unittest, например,
    используя проверочный метод assertEqual
    - Запустите получившиеся тесты из файла
    - Просмотрите отчёт о запуске и найдите последнюю строчку
    - Отправьте эту строчку в качестве ответа на это задание

Обратите внимание, что по задумке должно выбрасываться исключение
NoSuchElementException во втором тесте. Если вы использовали конструкцию
try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во
всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты
даже при наличии неожиданного исключения.
"""

import time
import unittest
from selenium import webdriver


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome()

    def teardown(self):
        self.wd.close()

    def test_1(self):
        LINK = "http://suninjuly.github.io/registration1.html"
        self.wd.get(LINK)
        input1 = self.wd.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = self.wd.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = self.wd.find_element_by_css_selector(".first_block .third")
        input3.send_keys("ipetrov@gmail.com")
        self.wd.find_element_by_css_selector("button.btn").click()

        time.sleep(1)
        welcome_text = self.wd.find_element_by_tag_name("h1").text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!"
        )

    def test_2(self):
        LINK = "http://suninjuly.github.io/registration2.html"
        self.wd.get(LINK)
        input1 = self.wd.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = self.wd.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = self.wd.find_element_by_css_selector(".first_block .third")
        input3.send_keys("ipetrov@gmail.com")
        self.wd.find_element_by_css_selector("button.btn").click()

        time.sleep(1)
        welcome_text = self.wd.find_element_by_tag_name("h1").text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!"
        )


if __name__ == "__main__":
    unittest.main()
