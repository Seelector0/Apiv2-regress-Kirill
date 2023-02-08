import allure
import requests
from utils.logger import Logger

"""Список HTTP методов"""


class HttpMethods:

    @staticmethod
    def get(url, headers):
        with allure.step("GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=headers)
            Logger.add_responce(result)
            return result

    @staticmethod
    def post(url, body, headers):
        with allure.step("POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json=body, headers=headers)
            Logger.add_responce(result)
            return result

    @staticmethod
    def put(url, body, headers):
        with allure.step("PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=headers)
            Logger.add_responce(result)
            return result

    @staticmethod
    def patch(url, body, headers):
        with allure.step("PATCH"):
            Logger.add_request(url, method="PATCH")
            result = requests.patch(url, json=body, headers=headers)
            Logger.add_responce(result)
            return result

    @staticmethod
    def delete(url, headers):
        with allure.step("DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, headers=headers)
            Logger.add_responce(result)
            return result
