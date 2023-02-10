import allure

from utils.api import MetashipApi
from utils.checking import Checking


@allure.epic("Test flow int shop")
class TestShop:

    @allure.description("Test create, update, delete shop")
    def test_flow_int_shop(self, access_token):
        print(f'\nСоздание магазина POST')
        result_post = MetashipApi.create_shop(access_token)
        check_post = result_post.json()
        shop_id = check_post.get('id')
        Checking.check_status_code(result_post, 201)

        print("Получение магазина GET")
        result_get = MetashipApi.get_shop(shop_id, access_token)
        Checking.check_status_code(result_get, 200)

        print("Получение списка магазинов GET")
        result_get_all = MetashipApi.get_shop_all(access_token)
        Checking.check_status_code(result_get_all, 200)

        print("Обновление магазина PUT")
        result_put = MetashipApi.put_shop(shop_id, access_token)
        Checking.check_status_code(result_put, 204)

        print("Удаление магазина DELETE")
        result_delete = MetashipApi.delete_shop(shop_id, access_token)
        Checking.check_status_code(result_delete, 409)

        print("Получение магазина GET")
        result_get = MetashipApi.get_shop(shop_id, access_token)
        Checking.check_status_code(result_get, 200)

        print("Редактирование полей магазина PATCH")
        result_patch = MetashipApi.patch_shop(shop_id, access_token)
        Checking.check_status_code(result_patch, 200)

        print("Получение магазина GET")
        result_get = MetashipApi.get_shop(shop_id, access_token)
        Checking.check_status_code(result_get, 200)
