from utils.http_method import HttpMethods
from environment import Env


class DeliveryServiceApi:
    """Методы для подключения служб доставки"""

    @staticmethod
    def delivery_service_russian_post(shop_id: str, headers: str):
        """Подключение Почты России"""
        json_delivery_service_russian_post = {
            "deliveryServiceCode": "RussianPost",
            "data": {
                "token": "A_DlNhO2HJGXf2mx5qPyA9Z2qDiqQoiE",
                "secret": "dkBwaW1wYXkucnU6KEgpeW1beCtPRUoh",
                "type": "integration",
                "intakePostOfficeCode": "101000",
                "externalDeliveryCode": "123"
            }
        }
        post_url = f'{Env.URL}/v2/customer/shops/{shop_id}/delivery_services'
        delivery_service_russian_post = HttpMethods.post(post_url, json_delivery_service_russian_post, headers)
        return delivery_service_russian_post

    @staticmethod
    def get_delivery_service(shop_id: str, headers: str):
        """Метод для получения настроек по всем службам доставки"""
        get_url = f'{Env.URL}/v2/customer/shops/{shop_id}/delivery_services'
        result_get_delivery_service = HttpMethods.get(get_url, headers)
        return result_get_delivery_service

    @staticmethod
    def get_delivery_service_code(shop_id: str, code: str, headers: str):
        """Метод для получения настроек по конкретной службе доставки"""
        get_url = f'{Env.URL}/v2/customer/shops/{shop_id}/delivery_services/{code}'
        result_get_delivery_service_code = HttpMethods.get(get_url, headers)
        return result_get_delivery_service_code

    @staticmethod
    def patch_delivery_service_code(shop_id: str, code: str, headers: str):
        """Метод для редактирования настроек службы доставки"""
        json_for_patch_delivery_service = [
            {
                "op": "replace",
                "path": "visibility",
                "value": False
            },
            {
                "op": "replace",
                "path": "settings.tariffs",
                "value": {
                    "exclude": [
                        "14",
                        "25"
                    ],
                    "restrict": None
                }
            }
        ]
        patch_url = f'{Env.URL}/v2/customer/shops/{shop_id}/delivery_services/{code}'
        result_patch_delivery_service_code = HttpMethods.patch(url=patch_url, body=json_for_patch_delivery_service,
                                                               headers=headers)
        return result_patch_delivery_service_code

    @staticmethod
    def delivery_service_activate(shop_id: str, code: str, headers: str):
        """Активация службы доставки"""
        post_url = f'{Env.URL}/v2/customer/shops/{shop_id}/delivery_services/{code}/activate'
        delivery_service_activate = HttpMethods.post(url=post_url, body=None, headers=headers)
        return delivery_service_activate

    @staticmethod
    def delivery_service_deactivate(shop_id: str, code: str, headers: str):
        """Деактивация службы доставки"""
        post_url = f'{Env.URL}/v2/customer/shops/{shop_id}/delivery_services/{code}/deactivate'
        delivery_service_deactivate = HttpMethods.post(url=post_url, body=None, headers=headers)
        return delivery_service_deactivate
