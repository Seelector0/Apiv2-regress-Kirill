import allure

from utils.api_shop import ShopApi
from utils.api_warehouse import WarehouseApi
from utils.checking import Checking
from utils.clear_db import clear_db


@allure.description("Тестирование магазина")
def test_flow_int_shop(shop, access_token):
    """Создание магазина POST"""
    ShopApi.report_post()
    result_post_shop = shop[0]
    Checking.check_status_code(result=result_post_shop, status_code=201)
    Checking.check_json_required_keys(result=result_post_shop, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_shop, key_name='type', expected_value='Shop')
    Checking.check_json_value(result=result_post_shop, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_shop.json().get('url'), check_value=shop[1],
                                               regexp_pattern=r'\/shops\/(.+)$')

    """Получение магазина GET"""
    result_get_shop = ShopApi.get_shop(shop_id=shop[1], headers=access_token)
    Checking.check_status_code(result=result_get_shop, status_code=200)
    Checking.check_json_required_keys(result=result_get_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                            'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop[1])
    Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)

    """Получение списка магазинов GET"""
    result_get_all_shops = ShopApi.get_shop_all(headers=access_token)
    Checking.check_status_code(result=result_get_all_shops, status_code=200)
    Checking.check_json_required_keys_array(result=result_get_all_shops, required_key=['id', 'number', 'name', 'uri',
                                                                                       'phone', 'sender', 'trackingTag',
                                                                                       'visibility'])

    """Обновление магазина PUT"""
    result_put_shop = ShopApi.put_shop(shop_id=shop[1], headers=access_token)
    Checking.check_status_code(result=result_put_shop, status_code=204)

    """Редактирование полей магазина PATCH"""
    result_patch_shop = ShopApi.patch_shop(shop_id=shop[1], headers=access_token)
    Checking.check_status_code(result=result_patch_shop, status_code=200)
    Checking.check_json_required_keys(result=result_patch_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                              'sender', 'trackingTag',
                                                                              'visibility'])
    Checking.check_json_value(result=result_patch_shop, key_name='visibility', expected_value=False)

    """Удаление магазина DELETE"""
    result_delete_shop = ShopApi.delete_shop(shop_id=shop[1], headers=access_token)
    Checking.check_status_code(result=result_delete_shop, status_code=409)

    """Получение магазина GET"""
    result_get_shop = ShopApi.get_shop(shop_id=shop[1], headers=access_token)
    Checking.check_status_code(result=result_get_shop, status_code=200)
    Checking.check_json_required_keys(result=result_get_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                            'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop[1])
    Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=False)


def test_flow_warehouse(warehouse, access_token):
    """Создание склада POST"""
    WarehouseApi.report_post()
    result_post_warehouse = warehouse[0]
    Checking.check_status_code(result=result_post_warehouse, status_code=201)
    Checking.check_json_required_keys(result=result_post_warehouse, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_warehouse, key_name='type', expected_value='Warehouse')
    Checking.check_json_value(result=result_post_warehouse, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_warehouse.json().get('url'),
                                               check_value=warehouse[1],
                                               regexp_pattern=r'\/warehouses\/(.+)$')

    """Получение склада GET"""
    result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse[1], headers=access_token)
    Checking.check_status_code(result=result_get_warehouse, status_code=200)
    Checking.check_json_required_keys(result=result_get_warehouse, required_key=['id', 'number', 'name', 'visibility',
                                                                                 'address', 'contact', 'workingTime',
                                                                                 'pickup', 'dpdPickupNum', 'comment'])
    Checking.check_json_value(result=result_get_warehouse, key_name='id', expected_value=warehouse[1])
    Checking.check_json_value(result=result_get_warehouse, key_name='visibility', expected_value=True)
    Checking.check_json_search_regexp_in_value(result=result_get_warehouse.json().get('name'),
                                               check_value="Test Warehouse", regexp_pattern=r'(Test Warehouse).+$')
    """Получение списка складов GET"""
    result_get_all_warehouses = WarehouseApi.get_warehouse_all(headers=access_token)
    Checking.check_status_code(result=result_get_all_warehouses, status_code=200)
    Checking.check_json_required_keys_array(result=result_get_all_warehouses, required_key=['id', 'number', 'name',
                                                                                            'visibility', 'address',
                                                                                            'contact', 'workingTime',
                                                                                            'pickup', 'dpdPickupNum',
                                                                                            'comment'])
    """Обновление склада PUT"""
    result_put_warehouse = WarehouseApi.put_warehouse(warehouse_id=warehouse[1], headers=access_token)
    Checking.check_status_code(result=result_put_warehouse, status_code=204)

    """Редактирование полей магазина PATCH"""
    result_patch_warehouse = WarehouseApi.patch_warehouse(warehouse_id=warehouse[1], headers=access_token)
    Checking.check_status_code(result=result_patch_warehouse, status_code=200)
    Checking.check_json_required_keys(result=result_patch_warehouse, required_key=['id', 'number', 'name', 'visibility',
                                                                                   'address', 'contact', 'workingTime',
                                                                                   'pickup', 'dpdPickupNum', 'comment'])
    Checking.check_json_value(result=result_patch_warehouse, key_name='visibility', expected_value=False)

    """Получение магазина GET"""
    result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse[1], headers=access_token)
    Checking.check_status_code(result=result_get_warehouse, status_code=200)
    Checking.check_json_required_keys(result=result_get_warehouse, required_key=['id', 'number', 'name', 'visibility',
                                                                                 'address', 'contact', 'workingTime',
                                                                                 'pickup', 'dpdPickupNum', 'comment'])
    Checking.check_json_value(result=result_get_warehouse, key_name='id', expected_value=warehouse[1])
    Checking.check_json_value(result=result_get_warehouse, key_name='visibility', expected_value=False)
    Checking.check_json_value(result=result_get_warehouse, key_name='pickup', expected_value=True)
    print(result_get_warehouse.json()["contact"]["fullName"])
    Checking.check_json_value1(key_name="fullName", response_value=result_get_warehouse.json()["contact"]["fullName"], expected_value="Складов Скад Складович")
    Checking.check_json_search_regexp_in_value(result=result_get_warehouse.json().get('name'),
                                               check_value="Test Warehouse PUT", regexp_pattern=r'(Test Warehouse PUT).+$')



# clear_db(shop_id=f"'{shop_id}'", warehouse_id=f"'{warehouse_id}'")
