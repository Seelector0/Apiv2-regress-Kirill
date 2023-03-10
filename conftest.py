import pytest
import requests
from environment import Env


@pytest.fixture(scope="module")
def access_token():
    """Получение Brear_Token"""

    data = dict(grant_type="client_credentials", client_id=Env.client_id, client_secret=Env.client_secret)
    resource = requests.post(url=f'{Env.URL}/auth/access_token', data=data)
    token = {
        "Authorization": f'Bearer {resource.json()["access_token"]}'
    }
    return token
