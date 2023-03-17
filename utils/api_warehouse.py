import datetime

import allure

from utils.http_method import HttpMethods
from environment import Env
from random import randint

"""Методы для тестирования магазина"""


class WarehouseApi:
    """Метод для создания склада"""

    @staticmethod
    def create_warehouse(headers):
        json_for_create_new_warehouse = {
            "name": f'Test Warehouse {datetime.datetime.now()}',
            "address": {
                "raw": "107045, г Москва, Красносельский р-н, ул Сретенка, д 28"
            }
        }
        post_url = f'{Env.URL}/v2/customer/warehouses'
        result_post_shop = HttpMethods.post(post_url, json_for_create_new_warehouse, headers)
        return result_post_shop

    """Метод для проверки всех складов"""

    @staticmethod
    def get_warehouse_all(headers):
        get_url = f'{Env.URL}/v2/customer/warehouses'
        result_get_warehouse_all = HttpMethods.get(get_url, headers)
        return result_get_warehouse_all

    """Метод для проверки склада"""

    @staticmethod
    def get_warehouse(warehouse_id, headers):
        get_url = f'{Env.URL}/v2/customer/warehouses/{warehouse_id}'
        result_get_warehouse = HttpMethods.get(get_url, headers)
        return result_get_warehouse

    """Метод для обновления склада"""

    @staticmethod
    def put_warehouse(warehouse_id, headers):
        json_for_put_warehouse = {
            "name": f'Test Warehouse PUT {datetime.datetime.now()}',
            "pickup": True,
            "comment": "Проверка метода PUT",
            "address": {
                "raw": "125009 г Москва, ул Тверская, д 22/2 корп 1"
            },
            "contact": {
                "fullName": "Складов Скад Складович",
                "email": f'Testsklad{randint(100, 9999)}@mail.ru',
                "phone": f"+79{randint(100000000, 999999999)}"
            }
        }
        put_url = f'{Env.URL}/v2/customer/warehouses/{warehouse_id}'
        result_put_warehouse = HttpMethods.put(put_url, json_for_put_warehouse, headers)
        return result_put_warehouse

    """Метод для редактирования полей склада"""

    @staticmethod
    def patch_warehouse(warehouse_id, headers):

        json_for_patch_warehouse = [
            {
                "op": "replace",
                "path": "visibility",
                "value": False
            }
        ]

        patch_url = f'{Env.URL}/v2/customer/warehouses/{warehouse_id}'
        # print(patch_url)
        result_patch_shop = HttpMethods.patch(patch_url, json_for_patch_warehouse, headers)
        return result_patch_shop

    """Метод для удаления склада"""

    @staticmethod
    def delete_warehouse(shop_id, headers):
        delete_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        # print(delete_url)
        result_delete_shop = HttpMethods.delete(delete_url, headers)
        # print(result_delete_shop)
        return result_delete_shop

    """Метод добавления в отчет метода POST"""

    @staticmethod
    def report_post():
        with allure.step(f"Метод POST {Env.URL}/v2/customer/warehouses"):
            return None
