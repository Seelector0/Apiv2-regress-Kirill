import re
import allure
from typing import Tuple


class Checking:
    """Методы для проверки запросов"""

    @staticmethod
    def check_status_code(result, status_code: int):
        """Метод для проверки статус кода"""
        with allure.step(f"Статус код в ответе {status_code}"):  # добавляем отображение в allure проверки
            assert status_code == result.status_code, \
                f"Статус код не верный! Ожидаемый: {status_code}. Фактический: {result.status_code}"
            # print(f'Статус код: {status_code} PASSED')

    @staticmethod
    def check_json_required_keys_exact(result, required_key: list):
        """Метод для проверки наличия ключей в ответе запроса, обязательно указываются все ключи"""
        with allure.step(f"Обязательные ключи {required_key} присутствуют"):
            token = result.json()  # модулем json преобразуем строку в формат json result.json() json.loads(result.text)
            assert list(token) == required_key, \
                f"Ключи не верные! Фактические: {list(token)}. Ожидаемые: {required_key}"
            # print(f'Обязательные ключи {list(token)} присутствуют')

    @staticmethod
    def check_response_body_key_not_empty(result, key):
        """Метод для проверки, что значение по указанному ключу в теле ответа не пустое"""
        with allure.step(f"Значение по ключу '{key}' не пустое"):
            response_body = result.json()
            assert key in response_body and response_body[key] is not None, f"Значение по ключу '{key}' пустое или " \
                                                                            f"отсутствует"

    @staticmethod
    def check_json_required_keys(result, required_key: list):
        """Метод для проверки наличия ключей в ответе запроса, необязательно указывать все ключи"""
        with allure.step(f"Ключи {required_key} присутствуют"):
            assert all(key in result.json() for key in required_key), \
                f"Ключи не верные! Фактические: {list(result.json())}. Ожидаемые: {required_key}"
            # print(f'Обязательные ключи {list(token)} присутствуют')

    @staticmethod
    def check_json_required_keys_array(result, required_key: list):
        """Метод для проверки наличия ключей в массиве, необязательно указывать все ключи"""
        with allure.step(f"Ключи {required_key} присутствуют"):
            for array in result.json():
                assert all(key in array for key in required_key), \
                    f"Ключи не верные! Фактические: {array}. Ожидаемые: {required_key}"
            # print(f'Обязательные ключи {list(token)} присутствуют')

    @staticmethod
    def check_json_value(result, key_name: str, expected_value):
        """Метод для проверки значения в ответе запроса"""
        with allure.step(f"В ключе {key_name} верное ожидаемое значение {expected_value}"):
            check = result.json()
            check_info = check.get(key_name)
            assert check_info == expected_value, \
                f"Ожидаемое значение в ключе {key_name} не верное! Фактическое: {check_info}. " \
                f"Ожидаемое: {expected_value}"

    @staticmethod
    def check_json_search_regexp_in_value(result, regexp_pattern, check_value):
        """Метод для проверки по регулярному выражению, выбираем определенное значение с помощью regexp и сравниваем"""
        with allure.step(f"Значение {result} из ответа соответствует {check_value}"):
            result = re.search(regexp_pattern, result)
            assert check_value == result.group(1), \
                f"Значение {result} из ответа не соответствует {check_value}"
            # print(f'Значение из ответа {result} соответствует {check_value}')

    @staticmethod
    def check_json_value_nested(
            result,
            key_tuple: Tuple[str, ...],
            expected_value
    ):
        """Метод для проверки значения в ответе запроса на любом уровне вложенности."""
        result = result.json()
        for key_name in key_tuple:
            result = result.get(key_name, {})

        check_info = result
        assert check_info == expected_value, \
            f"Ожидаемое значение в ключе {key_tuple} не верное! Фактическое: {check_info}. " \
            f"Ожидаемое: {expected_value}"

    @staticmethod
    def check_unique_ids(result, id_key):
        """Проверка уникальности идентификаторов в списке объектов"""
        with allure.step(f"Проверка уникальности ключа {id_key}"):
            objects = result.json()
            object_ids = set()
            for obj in objects:
                obj_id = obj.get(id_key)
                assert obj_id is not None, f"Объект не содержит идентификатор {id_key}"
                assert obj_id not in object_ids, f"Дублирующийся идентификатор {id_key}: {obj_id}"
                object_ids.add(obj_id)

    # """Метод для проверки слова в ответе по заданному значению"""

    # @staticmethod
    # def check_json_search_word_in_value(result, field_name, search_word):
    #     with allure.step(f"Значение {search_word} присутствуют"):
    #         check = result.json()
    #         check_info = check.get(field_name)
    #         assert search_word in check_info
    #         print(f'Слово {search_word} присутствует!!!')
