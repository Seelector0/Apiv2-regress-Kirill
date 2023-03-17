import allure

from utils.api_delivery_service import DeliveryServiceApi
from utils.api_order import OrderApi
from utils.api_parcelr import ParcelApi
from utils.api_shop import ShopApi
from utils.api_warehouse import WarehouseApi
from utils.checking import Checking
from utils.clear_db import clear_db


@allure.description("Тестирование магазина")

def test_create_new_connections_rp(new_shop, access_token):
    print(new_shop)
    result_post_new_connections = DeliveryServiceApi.create_new_connection_rp(shop_id=new_shop, headers=access_token)

def test_create_new_order(new_order, access_token):
    print(new_order)



# def test_create_new_order_2(new_shop, new_warehouse, access_token):
#     result_post_order = OrderApi.create_order(shop_id=new_shop, warehouse_id=new_warehouse, headers=access_token, sec=6)
#     print(result_post_order.json().get('id'))


# def test_create_new_parcel(new_order, access_token):
#     result_post_parcel = ParcelApi.create_parcel(order_id=new_order, headers=access_token)

def test_create_new_parcel_2(new_parcel, access_token):
    print(new_parcel)
    # print(new_parcel.json().get('id'))







# def test_create_new_order(new_order, access_token):
#     # result_post_warehouse = new_warehouse
#     # warehouse_id = result_post_warehouse.json().get('id')
#     # result_post_shop = new_shop
#     # shop_id = result_post_shop.json().get('id')
#     # result_post_order = OrderApi.create_order(shop_id=new_shop, warehouse_id=new_warehouse, headers=access_token)
#     # order_id = result_post_order.json().get('id')
#     print(new_order)
#     print(new_order.json().get('id'))
#     # print(warehouse_id)
#     # print(shop_id)
#     # clear_db(shop_id=f"'{shop_id}'", warehouse_id=f"'{warehouse_id}'")



# def test_create_new_order3(new_order, access_token):
#     print(new_order)
#     print(new_order.json().get('id'))
