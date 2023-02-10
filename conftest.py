import pytest
import requests
from environment import Env


@pytest.fixture()
def access_token():
    """Получение Brear_Token"""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = dict(grant_type="client_credentials", client_id=Env.client_id, client_secret=Env.client_secret)
    resource = requests.post(url=f'{Env.URL}/auth/access_token', data=data, headers=headers)
    token = {
        "Authorization": f'Bearer {resource.json()["access_token"]}'
    }
    return token
