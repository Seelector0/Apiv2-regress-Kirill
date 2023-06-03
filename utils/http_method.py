from utils.logger import Logger
import allure
import requests


class HttpMethods:
    """Список HTTP методов"""

    @staticmethod
    def get(url, headers, report_allure=True):
        """Метод GET с возможностью выбора добавления в отчет Allure"""
        Logger.add_request(url, method="GET")  # пишем в лог запрос

        result = requests.get(url=url, headers=headers)

        if report_allure:
            with allure.step(f"Метод GET {url}"):
                Logger.add_response(result)

        else:
            Logger.add_response(result)

        return result

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

