from utils.http_method import HttpMethods
from environment import Env
from random import randint
import datetime


class ShopApi:
    """Методы для работы с магазином"""

    @staticmethod
    def create_shop(headers: str):
        """Метод для создания магазина"""
        json_for_create_new_shop = {
            "name": f'Shop Int {datetime.datetime.now()}',
            "uri": f'bestshop{randint(100, 9999)}.ru'
        }

        post_url = f'{Env.URL}/v2/customer/shops'
        result_post_shop = HttpMethods.post(url=post_url, body=json_for_create_new_shop, headers=headers)
        return result_post_shop

    @staticmethod
    def get_shop_all(headers: str):
        """Метод для проверки всех магазинов"""
        get_url = f'{Env.URL}/v2/customer/shops'
        result_get_shop_all = HttpMethods.get(url=get_url, headers=headers)
        return result_get_shop_all

    @staticmethod
    def get_shop(shop_id: str, headers: str):
        """Метод для проверки магазина"""
        get_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        result_get_shop = HttpMethods.get(url=get_url, headers=headers)
        return result_get_shop

    @staticmethod
    def put_shop(shop_id: str, headers: str):
        """Метод для обновления магазина"""
        json_for_put_shop = {
            "name": f'Shop Int PUT {datetime.datetime.now()}',
            "uri": f'bestshop{randint(100, 9999)}.ru',
            "phone": f"79{randint(100000000, 999999999)}",
            "sender": "Тестов Тест Тестович"
        }

        put_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        result_put_shop = HttpMethods.put(url=put_url, body=json_for_put_shop, headers=headers)
        return result_put_shop

    @staticmethod
    def patch_shop(shop_id: str, headers: str):
        """Метод для редактирования полей магазина"""
        json_for_patch_shop = [
            {
                "op": "replace",
                "path": "visibility",
                "value": True
            }
        ]

        patch_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        result_patch_shop = HttpMethods.patch(url=patch_url, body=json_for_patch_shop, headers=headers)
        return result_patch_shop

    @staticmethod
    def delete_shop(shop_id: str, headers: str):
        """Негативная проверка: Метод для удаления магазина"""
        delete_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        result_delete_shop = HttpMethods.delete(url=delete_url, headers=headers)
        return result_delete_shop

    @staticmethod
    def get_shops_id(headers: str):
        """Метод получения id магазинов"""
        get_url = f'{Env.URL}/v2/customer/shops'
        shops_list = HttpMethods.get_not_allure(url=get_url, headers=headers)
        shops_id_list = []
        for shop in shops_list.json():
            shops_id_list += shop.get('id').split()
        return shops_id_list
