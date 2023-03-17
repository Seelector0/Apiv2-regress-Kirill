
import pytest
import requests
from environment import Env
from utils.api_order import OrderApi
from utils.api_parcelr import ParcelApi
from utils.api_shop import ShopApi
from utils.api_warehouse import WarehouseApi


@pytest.fixture(scope="module")
def access_token():
    """Получение Brear_Token"""

    data = dict(grant_type="client_credentials", client_id=Env.client_id, client_secret=Env.client_secret)
    resource = requests.post(url=f'{Env.URL}/auth/access_token', data=data)
    token = {
        "Authorization": f'Bearer {resource.json()["access_token"]}'
    }
    return token


@pytest.fixture(scope="module")
def new_shop(access_token):
    result_post_shop = ShopApi.create_shop(headers=access_token)
    shop_id = result_post_shop.json().get('id')
    return result_post_shop, shop_id


@pytest.fixture(scope="module")
def new_warehouse(access_token):
    result_post_warehouse = WarehouseApi.create_warehouse(headers=access_token)
    shop_id = result_post_warehouse.json().get('id')
    return result_post_warehouse, shop_id


@pytest.fixture(scope="module")
def new_order(access_token, new_shop, new_warehouse):
    result_post_order = OrderApi.create_order(shop_id=new_shop[1], warehouse_id=new_warehouse[1], headers=access_token)
    order_id = result_post_order.json().get('id')
    return result_post_order, order_id


@pytest.fixture(scope="module")
def new_parcel(access_token, new_order):
    parcel_id = []
    result_post_parcel = ParcelApi.create_parcel(order_id=new_order[1], headers=access_token)
    for parcel in result_post_parcel.json():
        parcel_id.append(parcel["id"])
        parcel_id = parcel_id[0]
    return result_post_parcel, parcel_id
