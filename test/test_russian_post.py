from utils.api.api_delivery_service import DeliveryServiceApi
from utils.api.api_order import OrderApi
from utils.checking import Checking
import allure
import pytest


@allure.description("Тестирование подключения Почты России")
def test_new_connection(access_token, shop):
    """Создание подключения POST"""
    result_post_connections = DeliveryServiceApi.delivery_service_russian_post(shop_id=shop[1], headers=access_token)
    Checking.check_status_code(result=result_post_connections, status_code=201)
    Checking.check_json_required_keys(result=result_post_connections, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_connections, key_name='type', expected_value='Delivery')
    Checking.check_json_value(result=result_post_connections, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_connections.json().get('url'),
                                               check_value=shop[1],
                                               regexp_pattern=r'\/shops\/(.+)\/delivery_services\/.*')

    """Получение настроек службы доставки Почта России GET"""
    result_get_connections = DeliveryServiceApi.get_delivery_service_code(shop_id=shop[1], headers=access_token,
                                                                          code='RussianPost')
    Checking.check_status_code(result=result_get_connections, status_code=200)
    Checking.check_json_required_keys(result=result_get_connections, required_key=['code', 'name', 'hasAggregation',
                                                                                   'credentials'])
    Checking.check_json_value(result=result_get_connections, key_name='code', expected_value='RussianPost')
    Checking.check_json_value(result=result_get_connections, key_name='name', expected_value='Почта России')
    Checking.check_json_value(result=result_get_connections, key_name='hasAggregation', expected_value=True)
    Checking.check_json_value_array_level_3(result=result_get_connections, key_level_1='credentials',
                                            key_level_2='data', key_name='type', expected_value="integration")

    """Получение настроек всех служб доставки GET"""
    result_get_all_connections = DeliveryServiceApi.get_delivery_service(shop_id=shop[1], headers=access_token)
    Checking.check_status_code(result=result_get_all_connections, status_code=200)
    Checking.check_json_required_keys_array(result=result_get_all_connections, required_key=['code', 'name',
                                                                                             'hasAggregation', 'id',
                                                                                             'active', 'visibility',
                                                                                             'type', 'moderation'])

    """Редактирование полей службы доставки PATCH"""
    result_patch_connections = DeliveryServiceApi.patch_delivery_service_code(shop_id=shop[1], code='RussianPost',
                                                                              headers=access_token)
    Checking.check_status_code(result=result_patch_connections, status_code=200)
    Checking.check_json_required_keys(result=result_patch_connections, required_key=['code', 'name', 'hasAggregation',
                                                                                     'credentials'])
    Checking.check_json_value_array_level_2(result=result_patch_connections, key_level_1='credentials',
                                            key_name='visibility', expected_value=False)
    Checking.check_json_value_array_level_4(result=result_patch_connections, key_level_1='credentials',
                                            key_level_2='settings', key_level_3='tariffs',
                                            key_name='restrict', expected_value=None)
    Checking.check_json_value_array_level_4(result=result_patch_connections, key_level_1='credentials',
                                            key_level_2='settings', key_level_3='tariffs',
                                            key_name='exclude', expected_value=['14', '25'])

    """Обновление службы доставки PUT"""
    result_put_connections = DeliveryServiceApi.put_delivery_service(shop_id=shop[1], code='RussianPost',
                                                                     headers=access_token)
    Checking.check_status_code(result=result_put_connections, status_code=409)

    """Удаление службы доставки DELETE"""
    result_delete_connections = DeliveryServiceApi.delete_delivery_service(shop_id=shop[1], code='RussianPost',
                                                                           headers=access_token)
    Checking.check_status_code(result=result_delete_connections, status_code=409)

    """Деактивация службы доставки POST"""
    result_deactivate_connections = DeliveryServiceApi.delivery_service_deactivate(shop_id=shop[1], code='RussianPost',
                                                                                   headers=access_token)
    Checking.check_status_code(result=result_deactivate_connections, status_code=204)

    """Активация службы доставки POST"""
    result_activate_connections = DeliveryServiceApi.delivery_service_activate(shop_id=shop[1], code='RussianPost',
                                                                               headers=access_token)
    Checking.check_status_code(result=result_activate_connections, status_code=204)


@pytest.mark.parametrize("payment_type", ["Paid", "PayOnDelivery"])
def test_create_new_order(access_token, shop, warehouse, connection, payment_type):
    result_post_order = OrderApi.create_order(shop_id=shop[1], warehouse_id=warehouse[1], headers=access_token,
                                              payment_type=payment_type)
    Checking.check_status_code(result=result_post_order, status_code=201)
#
#
# def test_create_new_parcel(access_token, shop, warehouse, connection, order):
#     # time.sleep(5)
#     result_post_parcel = ParcelApi.create_parcel(order_id=order[1], headers=access_token)


# def test_create_new_parcel_2(new_parcel, access_token):
#     print(new_parcel)
#     print(new_parcel.json().get('id'))
#
# def test_create_new_order3(new_order, access_token):
#     print(new_order)
#     print(new_order.json().get('id'))


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
