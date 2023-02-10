from utils.http_method import HttpMethods
from environment import Env

"""Методы для тестирования GoogleMapsApi"""


class MetashipApi:
    """Метод для создания магазина"""

    @staticmethod
    def create_shop(headers):

        json_for_create_new_shop = {
            "name": "Test Shop 2023-02-07T08:55:23.436Z",
            "uri": "clotilde.name"
        }

        post_url = f'{Env.URL}/v2/customer/shops'
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_shop, headers)
        print(result_post.text)
        return result_post

    """Метод для проверки магазина"""

    @staticmethod
    def get_shop(shop_id, headers):
        get_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        print(get_url)
        result_get = HttpMethods.get(get_url, headers)
        print(result_get.text)
        return result_get

    """Метод для обновления магазина"""

    @staticmethod
    def put_shop(shop_id, headers):

        json_for_put_shop = {
            "name": "Test Shop R 2023-02-07T14:10:05.652Z",
            "uri": "ezequiel.biz",
            "phone": "75672955802",
            "sender": "Juana Hagenes"
        }

        put_url = f'{Env.URL}/v2/customer/shops/{shop_id}'
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_put_shop, headers)
        return result_put
