import allure

from utils.api_shop import ShopApi
from utils.api_warehouse import WarehouseApi
from utils.checking import Checking
from utils.clear_db import clear_db


@allure.description("Тестирование магазина")
def test_flow_int_shop(new_shop, access_token):
    print(f'\nСоздание магазина POST')
    ShopApi.report_post()
    result_post_shop = new_shop[0]
    Checking.check_status_code(result=result_post_shop, status_code=201)
    Checking.check_json_required_keys(result=result_post_shop, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_shop, key_name='type', expected_value='Shop')
    Checking.check_json_value(result=result_post_shop, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_shop.json().get('url'), check_value=new_shop[1],
                                               regexp_pattern=r'\/shops\/(.+)$')

    print("Получение магазина GET")
    result_get_shop = ShopApi.get_shop(new_shop[1], headers=access_token)
    Checking.check_status_code(result_get_shop, 200)
    Checking.check_json_required_keys(result_get_shop,
                                      ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=new_shop[1])
    Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)

    print("Получение списка магазинов GET")
    result_get_all_shops = ShopApi.get_shop_all(access_token)
    Checking.check_status_code(result_get_all_shops, 200)
    Checking.check_json_required_keys_array(result=result_get_all_shops, required_key=['id', 'number', 'name', 'uri',
                                                                                       'phone', 'sender', 'trackingTag',
                                                                                       'visibility'])

    print("Обновление магазина PUT")
    result_put_shop = ShopApi.put_shop(new_shop[1], access_token)
    Checking.check_status_code(result_put_shop, 204)

    print("Редактирование полей магазина PATCH")
    result_patch_shop = ShopApi.patch_shop(new_shop[1], access_token)
    Checking.check_status_code(result_patch_shop, 200)
    Checking.check_json_required_keys(result=result_patch_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                              'sender', 'trackingTag',
                                                                              'visibility'])
    Checking.check_json_value(result=result_patch_shop, key_name='visibility', expected_value=False)

    print("Удаление магазина DELETE")
    result_delete_shop = ShopApi.delete_shop(new_shop[1], access_token)
    Checking.check_status_code(result_delete_shop, 409)

    print("Получение магазина GET")
    result_get_shop = ShopApi.get_shop(new_shop[1], access_token)
    Checking.check_status_code(result_get_shop, 200)
    Checking.check_json_required_keys(result=result_get_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                            'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=new_shop[1])
    Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=False)
    print(new_shop[1])


def test_flow_warehouse(new_warehouse, access_token):
    print(f'\nСоздание склада POST')
    WarehouseApi.report_post()
    result_post_warehouse = new_warehouse[0]
    Checking.check_status_code(result=result_post_warehouse, status_code=201)
    Checking.check_json_required_keys(result=result_post_warehouse, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_warehouse, key_name='type', expected_value='Warehouse')
    Checking.check_json_value(result=result_post_warehouse, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_warehouse.json().get('url'),
                                               check_value=new_warehouse[1],
                                               regexp_pattern=r'\/warehouses\/(.+)$')

    print("Получение склада GET")
    result_get_warehouse = WarehouseApi.get_warehouse(new_warehouse[1], headers=access_token)
    Checking.check_status_code(result_get_warehouse, 200)
    Checking.check_json_required_keys(result=result_get_warehouse, required_key=['id', 'number', 'name', 'visibility',
                                                                                 'address', 'contact', 'workingTime',
                                                                                 'pickup', 'dpdPickupNum', 'comment'])
    Checking.check_json_value(result=result_get_warehouse, key_name='id', expected_value=new_warehouse[1])
    Checking.check_json_value(result=result_get_warehouse, key_name='visibility', expected_value=True)
    Checking.check_json_search_regexp_in_value(result=result_get_warehouse.json().get('name'),
                                               check_value="Test Warehouse", regexp_pattern=r'(Test Warehouse).+$')
    print("Получение списка складов GET")
    result_get_all_warehouses = WarehouseApi.get_warehouse_all(access_token)
    Checking.check_status_code(result_get_all_warehouses, 200)
    Checking.check_json_required_keys_array(result=result_get_all_warehouses, required_key=['id', 'number', 'name',
                                                                                            'visibility', 'address',
                                                                                            'contact', 'workingTime',
                                                                                            'pickup', 'dpdPickupNum',
                                                                                            'comment'])
    print("Обновление склада PUT")
    result_put_warehouse = WarehouseApi.put_warehouse(new_warehouse[1], access_token)
    Checking.check_status_code(result_put_warehouse, 204)
