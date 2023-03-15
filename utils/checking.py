"""Методы для проверки ответов наших запросов"""
import re

import allure


class Checking:
    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(result, status_code):
        with allure.step(f"Статус код в ответе {status_code}"):  # добавляем отображение в allure проверки
            assert status_code == result.status_code, \
                f"Статус код не верный! Ожидаемый: {status_code}. Фактический: {result.status_code}"
            # print(f'Статус код: {status_code} PASSED')

    """Метод для проверки наличия обязательных ключей в ответе запроса, обязательно указываются все ключи"""

    @staticmethod
    def check_json_required_keys_exact(result, required_key):
        with allure.step(f"Обязательные ключи {required_key} присутствуют"):
            token = result.json()  # модулем json преобразуем строку в формат json result.json() json.loads(result.text)
            assert list(token) == required_key, \
                f"Ключи не верные! Фактические: {list(token)}. Ожидаемые: {required_key}"
            # print(f'Обязательные ключи {list(token)} присутствуют')

    """Метод для проверки наличия ключей обязательных в ответе запроса, не обязательно указывать все ключи"""

    @staticmethod
    def check_json_required_keys(result, required_key):
        with allure.step(f"Ключи {required_key} присутствуют"):
            assert all(key in result.json() for key in required_key), \
                f"Ключи не верные! Фактические: {list(result.json())}. Ожидаемые: {required_key}"
            # print(f'Обязательные ключи {list(token)} присутствуют')

    """Метод для проверки наличия ключей обязательных в массиве, не обязательно указывать все ключи"""
    @staticmethod
    def check_json_required_keys_obj(result, required_key):
        with allure.step(f"Ключи {required_key} присутствуют"):
            for obj in result.json():
                assert all(key in obj for key in required_key), \
                f"Ключи не верные! Фактические: {list(result.json())}. Ожидаемые: {required_key}"
            # print(f'Обязательные ключи {list(token)} присутствуют')

    """Метод для проверки значения в ответе запроса"""

    @staticmethod
    def check_json_value(result, key_name, expected_value):
        with allure.step(f"В ключе {key_name} верное ожидаемое значение {expected_value}"):
            check = result.json()
            check_info = check.get(key_name)
            assert check_info == expected_value, \
                f"Ожидаемое значение в ключе {key_name} не верное! Фактическое: {check_info}. Ожидаемое: {expected_value}"
            # print(f'Ожидаемое значение {expected_value} присутствуют')


    """Метод для проверки по регулярному выражению, выбираем определенное значение с помощью regexp и сравниваем"""

    @staticmethod
    def check_json_search_regexp_in_value(result, regexp_pattern, check_value):
        with allure.step(f"Значение {result} из ответа соответствует {check_value}"):
            result = re.search(regexp_pattern, result)
            assert check_value == result.group(1), \
                f"Значение {result} из ответа не соответствует {check_value}"
            # print(f'Значение из ответа {result} соответствует {check_value}')

    # """Метод для проверки слова в ответе по заданному значению"""

    # @staticmethod
    # def check_json_search_word_in_value(result, field_name, search_word):
    #     with allure.step(f"Значение {search_word} присутствуют"):
    #         check = result.json()
    #         check_info = check.get(field_name)
    #         assert search_word in check_info
    #         print(f'Слово {search_word} присутствует!!!')
