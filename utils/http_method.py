from utils.logger import Logger
import allure
import requests


class HttpMethods:
    """Список HTTP методов"""

    @staticmethod
    def get(url, headers):
        """Метод GET"""
        with allure.step(f"Метод GET {url}"):  # отображение в allure
            Logger.add_request(url, method="GET")  # пишем в лог запрос
            result = requests.get(url=url,
                                  headers=headers)  # определяем как выглядит запрос и какие параметры должны быть
            Logger.add_response(result)  # пишем в лог ответ
            return result  # отдаем результат

    @staticmethod
    def post(url, body, headers):
        """Метод POST"""
        with allure.step(f"Метод POST {url}"):
            Logger.add_request(url, method="POST")
            result = requests.post(url=url, json=body, headers=headers)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body, headers):
        """Метод PUT"""
        with allure.step(f"Метод PUT {url}"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url=url, json=body, headers=headers)
            Logger.add_response(result)
            return result

    @staticmethod
    def patch(url, body, headers):
        """Метод PATCH"""
        with allure.step(f"Метод PATCH {url}"):
            Logger.add_request(url, method="PATCH")
            result = requests.patch(url=url, json=body, headers=headers)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, headers):
        """Метод DELETE"""
        with allure.step(f"Метод DELETE {url}"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url=url, headers=headers)
            Logger.add_response(result)
            return result

    @staticmethod
    def get_not_allure(url, headers):
        """Метод GET без записи в отчет Allure"""
        Logger.add_request(url, method="GET")  # пишем в лог запрос
        result = requests.get(url=url, headers=headers)  # определяем как выглядит запрос и какие параметры должны быть
        Logger.add_response(result)  # пишем в лог ответ
        return result  # отдаем результат
