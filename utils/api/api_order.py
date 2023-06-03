import datetime
from utils.http_method import HttpMethods
from environment import Env
from random import randint
"""Методы для тестирования магазина"""


class OrderApi:
    """Метод для создания склада"""

    @staticmethod
    def create_order(headers, warehouse_id, shop_id, payment_type, delivery_type, x_trace_id=None):
        """Создание заказа"""
        json_for_create_new_order = {
            "warehouse": {
                "id": warehouse_id
            },
            "shop": {
                "id": shop_id,
                "number": "RP_1678982530843"
            },
            "payment": {
                "type": payment_type,
                "declaredValue": 2500,
                "deliverySum": 180
            },
            "dimension": {
                "length": 869,
                "width": 886,
                "height": 171
            },
            "weight": 6,
            "delivery": {
                "type": delivery_type,
                "service": "RussianPost",
                "tariff": "4",
                "date": "",
                "time": {
                    "from": "",
                    "to": ""
                }
            },
            "recipient": {
                "familyName": "Wilkinson",
                "firstName": "Godfrey",
                "secondName": "Mona",
                "phoneNumber": "+72936656417",
                "email": "Elva_DuBuque@hotmail.com",
                "address": {
                    "raw": "101000, г Москва, ул Жуковского, д 3/4"
                }
            },
            "comment": "Hungary granular",
            "places": [
                {
                    "items": [
                        {
                            "article": "EE923147562813020029",
                            "name": "Chair",
                            "price": 1000,
                            "count": 1,
                            "weight": 1,
                            "vat": "0"
                        },
                        {
                            "article": "SI57024120327604055",
                            "name": "Shirt",
                            "price": 1000,
                            "count": 1,
                            "weight": 1,
                            "vat": "NO_VAT"
                        }
                    ]
                }
            ]
        }
        post_url = f'{Env.URL}/v2/orders'
        result_post_shop = HttpMethods.post(post_url, json_for_create_new_order, headers, x_trace_id)
        return result_post_shop

    """Метод для проверки всех складов"""

    @staticmethod
    def get_orders_all(headers):
        get_url = f'{Env.URL}/v2/orders/'
        result_get_orders_all = HttpMethods.get(get_url, headers)
        return result_get_orders_all

    """Метод для проверки склада"""

    @staticmethod
    def get_orders(order_id, headers, x_trace_id=None, report_allure=True):
        get_url = f'{Env.URL}/v2/orders/{order_id}'
        result_get_order = HttpMethods.get(get_url, headers=headers, x_trace_id=x_trace_id, report_allure=report_allure)
        return result_get_order

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
