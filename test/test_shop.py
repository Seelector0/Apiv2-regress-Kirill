from utils.api import MetashipApi
from utils.checking import Cheking


def test_create_new_shop(access_token):

    print(f'\n"Метод POST"')
    result_post = MetashipApi.create_shop(access_token)
    check_post = result_post.json()
    shop_id = check_post.get('id')
    Cheking.check_status_code(result_post, 201)

    print("Метод GET")
    result_get = MetashipApi.get_shop(shop_id, access_token)
    Cheking.check_status_code(result_get, 200)

    print("Метод GET ALL")
    result_get_all = MetashipApi.get_shop_all(access_token)
    Cheking.check_status_code(result_get_all, 200)

    print("Метод PUT")
    result_put = MetashipApi.put_shop(shop_id, access_token)
    Cheking.check_status_code(result_put, 204)

    print("Метод DELETE")
    result_delete = MetashipApi.delete_shop(shop_id, access_token)
    Cheking.check_status_code(result_delete, 409)

    print("Метод GET")
    result_get = MetashipApi.get_shop(shop_id, access_token)
    Cheking.check_status_code(result_get, 200)

    print("Метод PATCH")
    result_patch = MetashipApi.patch_shop(shop_id, access_token)
    Cheking.check_status_code(result_patch, 200)

    print("Метод GET")
    result_get = MetashipApi.get_shop(shop_id, access_token)
    Cheking.check_status_code(result_get, 200)
