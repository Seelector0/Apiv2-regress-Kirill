import pytest
import requests
from environment import Env
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
    return result_post_shop


@pytest.fixture(scope="module")
def new_warehouse(access_token):
    result_post_warehouse = WarehouseApi.create_warehouse(headers=access_token)
    return result_post_warehouse
