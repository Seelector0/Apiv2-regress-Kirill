import uuid
import requests
import allure

from utils.logger import Logger


class HttpMethods:
    """Список HTTP методов"""

    @staticmethod
    def _send_request(method, url, headers, body=None, x_trace_id=None, report_allure=True):
        """Отправляет HTTP-запрос с возможностью выбора добавления в отчет Allure и указания x_trace_id"""
        Logger.add_request(url, method=method)  # пишем в лог запрос
        if x_trace_id is None:  # стандартное значение x_trace_id генерируется случайно
            x_trace_id = str(uuid.uuid4())
        headers["x-trace-id"] = str(x_trace_id)  # можно прокинуть к тесту и указать нужный x_trace_id

        if method == "GET":
            result = requests.get(url=url, headers=headers)
        elif method == "POST":
            result = requests.post(url=url, json=body, headers=headers)
        elif method == "PUT":
            result = requests.put(url=url, json=body, headers=headers)
        elif method == "PATCH":
            result = requests.patch(url=url, json=body, headers=headers)
        elif method == "DELETE":
            result = requests.delete(url=url, headers=headers)
        else:
            raise ValueError(f"Неподдерживаемый HTTP method: {method}")

        if report_allure:  # стандартное значение метод добавляется в отчет Allure
            with allure.step(f"Метод {method} {url}"):
                Logger.add_response(result)
        else:  # можно прокинуть к тесту и указать report_allure=False, тогда запись в отчет не попадет
            Logger.add_response(result)

        return result

    @staticmethod
    def get(url, headers, x_trace_id=None, report_allure=True):
        """Метод GET с возможностью выбора добавления в отчет Allure и указания x_trace_id"""
        return HttpMethods._send_request("GET", url, headers, x_trace_id=x_trace_id, report_allure=report_allure)

    @staticmethod
    def post(url, body, headers, x_trace_id=None, report_allure=True):
        """Метод POST с возможностью выбора добавления в отчет Allure и указания x_trace_id"""
        return HttpMethods._send_request("POST", url, headers, body=body, x_trace_id=x_trace_id,
                                         report_allure=report_allure)

    @staticmethod
    def put(url, body, headers, x_trace_id=None, report_allure=True):
        """Метод PUT с возможностью выбора добавления в отчет Allure и указания x_trace_id"""
        return HttpMethods._send_request("PUT", url, headers, body=body, x_trace_id=x_trace_id,
                                         report_allure=report_allure)

    @staticmethod
    def patch(url, body, headers, x_trace_id=None, report_allure=True):
        """Метод PATCH с возможностью выбора добавления в отчет Allure и указания x_trace_id"""
        return HttpMethods._send_request("PATCH", url, headers, body=body, x_trace_id=x_trace_id,
                                         report_allure=report_allure)

    @staticmethod
    def delete(url, headers, x_trace_id=None, report_allure=True):
        """Метод DELETE с возможностью выбора добавления в отчет Allure и указания x_trace_id"""
        return HttpMethods._send_request("DELETE", url, headers, x_trace_id=x_trace_id, report_allure=report_allure)
