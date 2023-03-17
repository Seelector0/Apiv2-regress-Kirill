import time

import allure

from utils.api_delivery_service import DeliveryServiceApi
from utils.api_order import OrderApi
from utils.api_parcelr import ParcelApi


@allure.description("Тестирование магазина")
def test_create_new_connections_rp(new_shop, access_token):
    print(new_shop)
    result_post_new_connections = DeliveryServiceApi.create_new_connection_rp(shop_id=new_shop[1], headers=access_token)


def test_create_new_order(new_order, access_token):
    OrderApi.report_post()
    print(new_order)
    time.sleep(3)


def test_create_new_parcel_2(new_parcel, access_token):
    ParcelApi.report_post()
    print(new_parcel)
