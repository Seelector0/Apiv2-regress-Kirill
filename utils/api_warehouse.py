import datetime
from utils.http_method import HttpMethods
from environment import Env
from random import randint


class WarehouseApi:
    """Методы для работы со складом"""

    @staticmethod
    def create_warehouse(headers):
        """Метод для создания склада"""
        json_for_create_new_warehouse = {
            "name": f'Test Warehouse {datetime.datetime.now()}',
            "address": {
                "raw": "107045, г Москва, Красносельский р-н, ул Сретенка, д 28"
            }
        }
        post_url = f'{Env.URL}/v2/customer/warehouses'
        result_post_shop = HttpMethods.post(post_url, json_for_create_new_warehouse, headers)
        return result_post_shop

    @staticmethod
    def get_warehouse_all(headers):
        """Метод для проверки всех складов"""
        get_url = f'{Env.URL}/v2/customer/warehouses'
        result_get_warehouse_all = HttpMethods.get(get_url, headers)
        return result_get_warehouse_all

    @staticmethod
    def get_warehouse(warehouse_id, headers):
        """Метод для проверки склада"""
        get_url = f'{Env.URL}/v2/customer/warehouses/{warehouse_id}'
        result_get_warehouse = HttpMethods.get(get_url, headers)
        return result_get_warehouse

    @staticmethod
    def put_warehouse(warehouse_id, headers):
        """Метод для обновления склада"""
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

    @staticmethod
    def patch_warehouse(warehouse_id, headers):
        """Метод для редактирования полей склада"""
        json_for_patch_warehouse = [
            {
                "op": "replace",
                "path": "visibility",
                "value": False
            }
        ]
        patch_url = f'{Env.URL}/v2/customer/warehouses/{warehouse_id}'
        result_patch_warehouse = HttpMethods.patch(patch_url, json_for_patch_warehouse, headers)
        return result_patch_warehouse

    @staticmethod
    def delete_warehouse(warehouse_id, headers):
        """Метод для удаления склада"""
        delete_url = f'{Env.URL}/v2/customer/warehouses/{warehouse_id}'
        result_delete_warehouse = HttpMethods.delete(delete_url, headers)
        return result_delete_warehouse
