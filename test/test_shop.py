import allure

from utils.api import MetashipApi
from utils.checking import Checking


@allure.epic("Test flow int shop")
class TestShop:

    @allure.description("Test create, update, delete shop")
    def test_flow_int_shop(self, access_token):
        print(f'\nСоздание магазина POST')
        result_post_shop = MetashipApi.create_shop(access_token)
        shop_id = result_post_shop.json().get('id')
        Checking.check_status_code(result_post_shop, 201)
        Checking.check_json_key(result_post_shop, ['id', 'type', 'url', 'status'])
        Checking.check_json_value(result_post_shop, field_name='type', expected_value='Shop')



        print("Получение магазина GET")
        result_get_shop = MetashipApi.get_shop(shop_id, access_token)
        Checking.check_status_code(result_get_shop, 200)
        Checking.check_json_key(result_get_shop,
                                ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])

        print("Получение списка магазинов GET")
        result_get_all = MetashipApi.get_shop_all(access_token)
        Checking.check_status_code(result_get_all, 200)
        Checking.check_json_key(result_get_shop,
                                ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])

        print("Обновление магазина PUT")
        result_put_shop = MetashipApi.put_shop(shop_id, access_token)
        Checking.check_status_code(result_put_shop, 204)

        print("Редактирование полей магазина PATCH")
        result_patch_shop = MetashipApi.patch_shop(shop_id, access_token)
        Checking.check_status_code(result_patch_shop, 200)
        Checking.check_json_key(result_patch_shop,
                                ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])

        print("Удаление магазина DELETE")
        result_delete_shop = MetashipApi.delete_shop(shop_id, access_token)
        Checking.check_status_code(result_delete_shop, 409)

        print("Получение магазина GET")
        result_get_shop = MetashipApi.get_shop(shop_id, access_token)
        Checking.check_status_code(result_get_shop, 200)
        Checking.check_json_key(result_get_shop,
                                ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
