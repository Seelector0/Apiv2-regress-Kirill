from utils.api import MetashipApi


def test_create_new_shop(access_token):
    print(f'\n"Метод POST"')
    result_post = MetashipApi.create_shop(access_token)
    check_post = result_post.json()
    shop_id = check_post.get('id')
    print(shop_id)

    print("Метод GET")
    result_get = MetashipApi.get_shop(shop_id, access_token)

    print("Метод GET ALL")
    result_get = MetashipApi.get_shop_all(access_token)

    print("Метод PUT")
    result_get = MetashipApi.put_shop(shop_id, access_token)

    print("Метод GET")
    result_get = MetashipApi.get_shop(shop_id, access_token)

    print("Метод PATCH")
    result_get = MetashipApi.patch_shop(shop_id, access_token)

    print("Метод GET")
    result_get = MetashipApi.get_shop(shop_id, access_token)
