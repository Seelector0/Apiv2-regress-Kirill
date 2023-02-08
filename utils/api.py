from conftest import access_token
from utils.http_method import HttpMethods


"""Методы для тестирования GoogleMapsApi"""

base_url = "http://apiv2.localhost" #Базовая URL

class MetashipApi():

    """Метод для создания магазина"""

    @staticmethod
    def create_shop(headers):

        post_resource = "/v2/customer/shops" # endopoint метода GET

        json_for_create_new_shop = {
            "name": "Test Shop 2023-02-07T08:55:23.436Z",
            "uri": "clotilde.name"
        }

        post_url = f'{base_url}{post_resource}'
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_shop, headers)
        print(result_post.text)
        return result_post

    """Метод для проверки магазина"""

    @staticmethod
    def get_shop(shop_id, headers):
        get_resource = "/v2/customer/shops/"
        get_url = f'{base_url}{get_resource}{shop_id}'
        print(get_url)
        result_get = HttpMethods.get(get_url, headers)
        print(result_get.text)
        return result_get

    """Метод для обновления магазина"""

    @staticmethod
    def put_shop(shop_id, headers):
        put_resource = "/v2/customer/shops/"

        json_for_put_shop = {
            "name":"Test Shop R 2023-02-07T14:10:05.652Z",
            "uri":"ezequiel.biz",
            "phone":"75672955802",
            "sender":"Juana Hagenes"
        }

        put_url = f'{base_url}{put_resource}{shop_id}'
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_put_shop, headers)
        return result_put




