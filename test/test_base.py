from utils.api.api_shop import ShopApi
from utils.api.api_warehouse import WarehouseApi
from utils.checking import Checking
import allure


@allure.description("Создание магазина POST")
def test_post_shop(access_token):
    result_post_shop = ShopApi.create_shop(headers=access_token)
    shop_id = result_post_shop.json().get('id')
    Checking.check_status_code(result=result_post_shop, status_code=201)
    Checking.check_json_required_keys(result=result_post_shop, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_shop, key_name='type', expected_value='Shop')
    Checking.check_json_value(result=result_post_shop, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_shop.json().get('url'), check_value=shop_id,
                                               regexp_pattern=r'\/shops\/(.+)$')
@allure.description("Получение магазина GET")
def test_get_shop(shop, access_token):
    shop_id = shop[1]
    result_get_shop = ShopApi.get_shop(shop_id=shop_id, headers=access_token)
    Checking.check_status_code(result=result_get_shop, status_code=200)
    Checking.check_json_required_keys(result=result_get_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                            'sender', 'trackingTag', 'visibility'])
    Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop_id)
    Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)
@allure.description("Получение списка магазинов GET")
def test_get_all_shops(shop, access_token):
    result_get_all_shops = ShopApi.get_shop_all(headers=access_token)
    Checking.check_status_code(result=result_get_all_shops, status_code=200)
    Checking.check_json_required_keys_array(result=result_get_all_shops, required_key=['id', 'number', 'name', 'uri',
                                                                                       'phone', 'sender', 'trackingTag',
                                                                                       'visibility'])
@allure.description("Обновление магазина PUT")
def test_put_shop(shop, access_token):
    shop_id = shop[1]
    result_put_shop = ShopApi.put_shop(shop_id=shop_id, headers=access_token)
    Checking.check_status_code(result=result_put_shop, status_code=204)

@allure.description("Редактирование полей магазина PATCH")
def test_patch_shop(shop, access_token):
    shop_id = shop[1]
    result_patch_shop = ShopApi.patch_shop(shop_id=shop_id, headers=access_token)
    Checking.check_status_code(result=result_patch_shop, status_code=200)
    Checking.check_json_required_keys(result=result_patch_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                              'sender', 'trackingTag',
                                                                              'visibility'])
    Checking.check_json_value(result=result_patch_shop, key_name='visibility', expected_value=True)
@allure.description(" Удаление магазина DELETE")
def test_delete_shop(shop, access_token):
    shop_id = shop[1]
    result_delete_shop = ShopApi.delete_shop(shop_id=shop_id, headers=access_token)
    Checking.check_status_code(result=result_delete_shop, status_code=409)
    # Получение магазина GET
    # result_get_shop = ShopApi.get_shop(shop_id=shop_id, headers=access_token)
    # Checking.check_status_code(result=result_get_shop, status_code=200)
    # Checking.check_json_required_keys(result=result_get_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
    #                                                                         'sender', 'trackingTag', 'visibility'])
    # Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop_id)
    # Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)


@allure.description("Тестирование склада")
def test_flow_warehouse(access_token):
    """Создание склада POST"""
    result_post_warehouse = WarehouseApi.create_warehouse(headers=access_token)
    warehouse_id = result_post_warehouse.json().get('id')
    Checking.check_status_code(result=result_post_warehouse, status_code=201)
    Checking.check_json_required_keys(result=result_post_warehouse, required_key=['id', 'type', 'url', 'status'])
    Checking.check_json_value(result=result_post_warehouse, key_name='type', expected_value='Warehouse')
    Checking.check_json_value(result=result_post_warehouse, key_name='status', expected_value=201)
    Checking.check_json_search_regexp_in_value(result=result_post_warehouse.json().get('url'),
                                               check_value=warehouse_id,
                                               regexp_pattern=r'\/warehouses\/(.+)$')

    """Получение склада GET"""
    result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse_id, headers=access_token)
    Checking.check_status_code(result=result_get_warehouse, status_code=200)
    Checking.check_json_required_keys(result=result_get_warehouse, required_key=['id', 'number', 'name', 'visibility',
                                                                                 'address', 'contact', 'workingTime',
                                                                                 'pickup', 'dpdPickupNum', 'comment'])
    Checking.check_json_value(result=result_get_warehouse, key_name='id', expected_value=warehouse_id)
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
    result_put_warehouse = WarehouseApi.put_warehouse(warehouse_id=warehouse_id, headers=access_token)
    Checking.check_status_code(result=result_put_warehouse, status_code=204)

    """Редактирование полей склада PATCH"""
    result_patch_warehouse = WarehouseApi.patch_warehouse(warehouse_id=warehouse_id, headers=access_token)
    Checking.check_status_code(result=result_patch_warehouse, status_code=200)
    Checking.check_json_required_keys(result=result_patch_warehouse, required_key=['id', 'number', 'name', 'visibility',
                                                                                   'address', 'contact', 'workingTime',
                                                                                   'pickup', 'dpdPickupNum', 'comment'])
    Checking.check_json_value(result=result_patch_warehouse, key_name='visibility', expected_value=False)

    """Получение склада GET"""
    result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse_id, headers=access_token)
    Checking.check_status_code(result=result_get_warehouse, status_code=200)
    Checking.check_json_required_keys(result=result_get_warehouse, required_key=['id', 'number', 'name', 'visibility',
                                                                                 'address', 'contact', 'workingTime',
                                                                                 'pickup', 'dpdPickupNum', 'comment'])
    Checking.check_json_value(result=result_get_warehouse, key_name='id', expected_value=warehouse_id)
    Checking.check_json_value(result=result_get_warehouse, key_name='visibility', expected_value=False)
    Checking.check_json_value(result=result_get_warehouse, key_name='pickup', expected_value=True)
    Checking.check_json_value_array_level_2(result=result_get_warehouse, key_level_1='contact', key_name='fullName',
                                            expected_value="Складов Скад Складович")
    Checking.check_json_search_regexp_in_value(result=result_get_warehouse.json().get('name'),
                                               check_value="Test Warehouse PUT",
                                               regexp_pattern=r'(Test Warehouse PUT).+$')
    """Удаление склада DELETE"""
    result_delete_shop = WarehouseApi.delete_warehouse(warehouse_id=warehouse_id, headers=access_token)
    Checking.check_status_code(result=result_delete_shop, status_code=204)

    """Получение склада GET"""
    result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse_id, headers=access_token)
    Checking.check_status_code(result=result_get_warehouse, status_code=404)

