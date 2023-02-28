import allure

from utils.api import MetashipApi
from utils.checking import Checking


@allure.epic("Test flow int shop")
class TestShop:

    @allure.description("Test create, update, delete shop")
    def test_flow_int_shop(self, access_token):
        print(f'\nСоздание магазина POST')
        result_post_shop = MetashipApi.create_shop(headers=access_token)
        shop_id = result_post_shop.json().get('id')
        Checking.check_status_code(result=result_post_shop, status_code=201)
        Checking.check_json_required_keys(result=result_post_shop, required_key=['id', 'type', 'url', 'status'])
        Checking.check_json_value(result=result_post_shop, key_name='type', expected_value='Shop')
        Checking.check_json_value(result=result_post_shop, key_name='status', expected_value=201)
        Checking.check_json_search_regexp_in_value(result=result_post_shop.json().get('url'), check_value=shop_id,
                                                   regexp_pattern=r'\/shops\/(.+)$')


        print("Получение магазина GET")
        result_get_shop = MetashipApi.get_shop(shop_id, headers=access_token)
        Checking.check_status_code(result_get_shop, 200)
        Checking.check_json_required_keys(result_get_shop,
                                          ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
        Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop_id)
        Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=True)


        print("Получение списка магазинов GET")
        result_get_all = MetashipApi.get_shop_all(access_token)
        Checking.check_status_code(result_get_all, 200)
        Checking.check_json_required_keys(result_get_shop,
                                          ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])

        print("Обновление магазина PUT")
        result_put_shop = MetashipApi.put_shop(shop_id, access_token)
        Checking.check_status_code(result_put_shop, 204)

        print("Редактирование полей магазина PATCH")
        result_patch_shop = MetashipApi.patch_shop(shop_id, access_token)
        Checking.check_status_code(result_patch_shop, 200)
        Checking.check_json_required_keys(result_patch_shop,
                                          ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
        Checking.check_json_value(result=result_patch_shop, key_name='visibility', expected_value=False)

        print("Удаление магазина DELETE")
        result_delete_shop = MetashipApi.delete_shop(shop_id, access_token)
        Checking.check_status_code(result_delete_shop, 409)

        print("Получение магазина GET")
        result_get_shop = MetashipApi.get_shop(shop_id, access_token)
        Checking.check_status_code(result_get_shop, 200)
        Checking.check_json_required_keys(result_get_shop,
                                          ['id', 'number', 'name', 'uri', 'phone', 'sender', 'trackingTag', 'visibility'])
        Checking.check_json_value(result=result_get_shop, key_name='id', expected_value=shop_id)
        Checking.check_json_value(result=result_get_shop, key_name='visibility', expected_value=False)
