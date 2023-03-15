import datetime
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
        # print(post_url)
        result_post_shop = HttpMethods.post(post_url, json_for_create_new_warehouse, headers)
        # print(result_post_shop.text)
        return result_post_shop

    """Метод для проверки всех складов"""

    @staticmethod
    def get_warehouse_all(headers):
        get_url = f'{Env.URL}/v2/customer/shops'
        # print(get_url)
        result_get_shop_all = HttpMethods.get(get_url, headers)
        # print(result_get_shop_all.text)
        return result_get_shop_all

    """Метод для проверки склада"""

    @staticmethod
    def get_warehouse(shop_id, headers):
        get_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        # print(get_url)
        result_get_shop = HttpMethods.get(get_url, headers)
        # print(result_get_shop.text)
        return result_get_shop

    """Метод для обновления склада"""

    @staticmethod
    def put_warehouse(shop_id, headers):

        json_for_put_shop = {
            "name": f'Shop Int PUT {datetime.datetime.now()}',
            "uri": f'bestshop{randint(100, 9999)}.ru',
            "phone": f"79{randint(100000000, 999999999)}",
            "sender": "Тестов Тест Тестович"
        }

        put_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        # print(put_url)
        result_put_shop = HttpMethods.put(put_url, json_for_put_shop, headers)
        return result_put_shop

    """Метод для редактирования полей склада"""

    @staticmethod
    def patch_warehouse(shop_id, headers):

        json_for_patch_shop = [
            {
                "op": "replace",
                "path": "visibility",
                "value": False
            }
        ]

        patch_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        # print(patch_url)
        result_patch_shop = HttpMethods.patch(patch_url, json_for_patch_shop, headers)
        return result_patch_shop

    """Метод для удаления склада"""

    @staticmethod
    def delete_warehouse(shop_id, headers):
        delete_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        # print(delete_url)
        result_delete_shop = HttpMethods.delete(delete_url, headers)
        # print(result_delete_shop)
        return result_delete_shop
