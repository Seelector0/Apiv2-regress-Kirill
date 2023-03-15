import allure

from conftest import new_warehouse, new_shop
from utils.api_shop import ShopApi
from utils.api_warehouse import WarehouseApi
from utils.checking import Checking
from utils.clear_db import clear_db


@allure.description("Тестирование магазина")
def test_flow_int_shop(new_shop, access_token):
    print(f'\nСоздание магазина POST')
    result_post_shop = new_shop
    shop_id = result_post_shop.json().get('id')
    Checking.check_status_code(result=result_post_shop, status_code=201)
    Checking.check_json_required_keys(result=result_post_shop, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_shop, key_name='type', expected_value='Shop')
    Checking.check_json_value(result=result_post_shop, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_shop.json().get('url'), check_value=shop_id,
                                               regexp_pattern=r'\/shops\/(.+)$')

    print("Получение магазина GET")

    result_get_shop = ShopApi.get_shop(shop_id, headers=access_token)
    Checking.check_status_code(result_get_shop, 200)
    Checking.check_json_required_keys(result_get_shop,
                                      ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop_id)
    Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)

    print("Получение списка магазинов GET")
    result_get_all = ShopApi.get_shop_all(access_token)
    Checking.check_status_code(result_get_all, 200)
    Checking.check_json_required_keys(result_get_shop,
                                      ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])

    print("Обновление магазина PUT")
    result_put_shop = ShopApi.put_shop(shop_id, access_token)
    Checking.check_status_code(result_put_shop, 204)

    print("Редактирование полей магазина PATCH")
    result_patch_shop = ShopApi.patch_shop(shop_id, access_token)
    Checking.check_status_code(result_patch_shop, 200)
    Checking.check_json_required_keys(result_patch_shop,
                                      ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_patch_shop, key_name='visibility', expected_value=False)

    print("Удаление магазина DELETE")
    result_delete_shop = ShopApi.delete_shop(shop_id, access_token)
    Checking.check_status_code(result_delete_shop, 409)

    print("Получение магазина GET")
    result_get_shop = ShopApi.get_shop(shop_id, access_token)
    Checking.check_status_code(result_get_shop, 200)
    Checking.check_json_required_keys(result_get_shop,
                                      ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop_id)
    Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=False)
    print(shop_id)


def test_flow_warehouse(new_warehouse):
    print(f'\nСоздание склада POST')
    result_post_warehouse = new_warehouse
    warehouse_id = result_post_warehouse.json().get('id')
    print(warehouse_id)
    Checking.check_status_code(result=result_post_warehouse, status_code=201)


def test_create_new_order(new_warehouse, new_shop):
    result_post_warehouse = new_warehouse
    warehouse_id = result_post_warehouse.json().get('id')
    result_post_shop = new_shop
    shop_id = result_post_shop.json().get('id')
    print('создание заказа')
    print(warehouse_id)
    print(shop_id)
    clear_db(shop_id=f"'{shop_id}'", warehouse_id=f"'{warehouse_id}'")
