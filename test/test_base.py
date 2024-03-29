from utils.api.api_shop import ShopApi
from utils.api.api_warehouse import WarehouseApi
from utils.checking import Checking
import allure


@allure.epic("№1_Магазин")
class TestShop:

    @allure.title("Создание магазина методом POST")
    def test_post_shop(self, shop, access_token):
        result_post_shop = shop[0]
        Checking.check_status_code(result=result_post_shop, status_code=201)
        Checking.check_json_required_keys(result=result_post_shop, required_key=['id', 'type', 'url', 'status'])
        Checking.check_json_value(result=result_post_shop, key_name='type', expected_value='Shop')
        Checking.check_json_value(result=result_post_shop, key_name='status', expected_value=201)
        Checking.check_json_search_regexp_in_value(result=result_post_shop.json().get('url'), check_value=shop[1],
                                                   regexp_pattern=r'\/shops\/(.+)$')

    @allure.title("Получение магазина GET")
    def test_get_shop(self, shop, access_token):
        result_get_shop = ShopApi.get_shop(shop_id=shop[1], headers=access_token)
        Checking.check_status_code(result=result_get_shop, status_code=200)
        Checking.check_json_required_keys(result=result_get_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                                'sender', 'trackingTag', 'visibility'])
        Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop[1])
        Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)

    @allure.title("Получение списка магазинов GET")
    def test_get_all_shops(self, shop, access_token):
        result_get_all_shops = ShopApi.get_shop_all(headers=access_token)
        Checking.check_status_code(result=result_get_all_shops, status_code=200)
        Checking.check_json_required_keys_array(result=result_get_all_shops,
                                                required_key=['id', 'number', 'name', 'uri',
                                                              'phone', 'sender', 'trackingTag',
                                                              'visibility'])

    @allure.title("Обновление магазина PUT")
    def test_put_shop(self, shop, access_token):
        result_put_shop = ShopApi.put_shop(shop_id=shop[1], headers=access_token)
        Checking.check_status_code(result=result_put_shop, status_code=204)

    @allure.title("Редактирование полей магазина PATCH")
    def test_patch_shop(self, shop, access_token):
        result_patch_shop = ShopApi.patch_shop(shop_id=shop[1], headers=access_token)
        Checking.check_status_code(result=result_patch_shop, status_code=200)
        Checking.check_json_required_keys(result=result_patch_shop,
                                          required_key=['id', 'number', 'name', 'uri', 'phone',
                                                        'sender', 'trackingTag',
                                                        'visibility'])
        Checking.check_json_value(result=result_patch_shop, key_name='visibility', expected_value=True)

    @allure.title("Удаление магазина DELETE")
    def test_delete_shop(self, shop, access_token):
        result_delete_shop = ShopApi.delete_shop(shop_id=shop[1], headers=access_token)
        Checking.check_status_code(result=result_delete_shop, status_code=409)
        # Проверка, что магазин не удалился и его можно получить
        result_get_shop = ShopApi.get_shop(shop_id=shop[1], headers=access_token)
        Checking.check_status_code(result=result_get_shop, status_code=200)
        Checking.check_json_required_keys(result=result_get_shop, required_key=['id', 'number', 'name', 'uri', 'phone',
                                                                                'sender', 'trackingTag', 'visibility'])
        Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop[1])
        Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)


@allure.epic("№2_Склад")
class TestWarehouse:
    @allure.title("Создание склада POST")
    def test_post_warehouse(self, warehouse, access_token):
        result_post_warehouse = warehouse[0]
        Checking.check_status_code(result=result_post_warehouse, status_code=201)
        Checking.check_json_required_keys(result=result_post_warehouse, required_key=['id', 'type', 'url', 'status'])
        Checking.check_json_value(result=result_post_warehouse, key_name='type', expected_value='Warehouse')
        Checking.check_json_value(result=result_post_warehouse, key_name='status', expected_value=201)
        Checking.check_json_search_regexp_in_value(result=result_post_warehouse.json().get('url'),
                                                   check_value=warehouse[1],
                                                   regexp_pattern=r'\/warehouses\/(.+)$')

    @allure.title("Получение склада GET")
    def test_get_warehouse(self, warehouse, access_token):
        result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse[1], headers=access_token)
        Checking.check_status_code(result=result_get_warehouse, status_code=200)
        Checking.check_json_required_keys(result=result_get_warehouse,
                                          required_key=['id', 'number', 'name', 'visibility',
                                                        'address', 'contact', 'workingTime',
                                                        'pickup', 'dpdPickupNum', 'comment'])
        Checking.check_json_value(result=result_get_warehouse, key_name='id', expected_value=warehouse[1])
        Checking.check_json_value(result=result_get_warehouse, key_name='visibility', expected_value=True)
        Checking.check_json_search_regexp_in_value(result=result_get_warehouse.json().get('name'),
                                                   check_value="Test Warehouse", regexp_pattern=r'(Test Warehouse).+$')

    @allure.title("Получение списка складов GET")
    def test_get_all_warehouse(self, warehouse, access_token):
        result_get_all_warehouses = WarehouseApi.get_warehouse_all(headers=access_token)
        Checking.check_status_code(result=result_get_all_warehouses, status_code=200)
        Checking.check_json_required_keys_array(result=result_get_all_warehouses, required_key=['id', 'number', 'name',
                                                                                                'visibility', 'address',
                                                                                                'contact',
                                                                                                'workingTime',
                                                                                                'pickup',
                                                                                                'dpdPickupNum',
                                                                                                'comment'])

    @allure.title("Обновление склада PUT")
    def test_put_warehouse(self, warehouse, access_token):
        result_put_warehouse = WarehouseApi.put_warehouse(warehouse_id=warehouse[1], headers=access_token)
        Checking.check_status_code(result=result_put_warehouse, status_code=204)

    @allure.title("Редактирование полей склада PATCH")
    def test_patch_warehouse(self, warehouse, access_token):
        result_patch_warehouse = WarehouseApi.patch_warehouse(warehouse_id=warehouse[1], headers=access_token)
        Checking.check_status_code(result=result_patch_warehouse, status_code=200)
        Checking.check_json_required_keys(result=result_patch_warehouse,
                                          required_key=['id', 'number', 'name', 'visibility',
                                                        'address', 'contact', 'workingTime',
                                                        'pickup', 'dpdPickupNum', 'comment'])
        Checking.check_json_value(result=result_patch_warehouse, key_name='visibility', expected_value=False)

        # Проверка, что склад обновился
        result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse[1], headers=access_token)
        Checking.check_status_code(result=result_get_warehouse, status_code=200)
        Checking.check_json_required_keys(result=result_get_warehouse,
                                          required_key=['id', 'number', 'name', 'visibility',
                                                        'address', 'contact', 'workingTime',
                                                        'pickup', 'dpdPickupNum', 'comment'])
        Checking.check_json_value(result=result_get_warehouse, key_name='id', expected_value=warehouse[1])
        Checking.check_json_value(result=result_get_warehouse, key_name='visibility', expected_value=False)
        Checking.check_json_value(result=result_get_warehouse, key_name='pickup', expected_value=True)

        Checking.check_json_value_nested(result=result_get_warehouse, key_tuple=('contact', 'fullName'),
                                         expected_value="Складов Виктор Сергеевич")

        Checking.check_json_search_regexp_in_value(result=result_get_warehouse.json().get('name'),
                                                   check_value="Test Warehouse PUT",
                                                   regexp_pattern=r'(Test Warehouse PUT).+$')

    @allure.title("Удаление склада DELETE")
    def test_delete_warehouse(self, warehouse, access_token):
        result_delete_shop = WarehouseApi.delete_warehouse(warehouse_id=warehouse[1], headers=access_token)
        Checking.check_status_code(result=result_delete_shop, status_code=204)
        result_get_warehouse = WarehouseApi.get_warehouse(warehouse_id=warehouse[1], headers=access_token)
        Checking.check_status_code(result=result_get_warehouse, status_code=404)
