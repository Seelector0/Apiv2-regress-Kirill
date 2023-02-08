
import pytest
import requests


@pytest.fixture()
def access_token():
    """Получение Brear_Token"""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        'client_id': "b912d871-fa13-4edc-8606-656a461e7dfb",
        'client_secret': "c0b33e8d8abd097cd0a17c7521ed49558166698d06f99fcba1483545e062e866ee8083326a4b323c"
    }
    resource = requests.post('http://apiv2.localhost/auth/access_token', data=data, headers=headers)
    token = {
        "Authorization": f"Bearer {resource.json()['access_token']}"
        # "Content-Type": "application/json"
    }
    return token


    # if "access_token" in resource.json():
    #     token = resource.json()['access_token']
    #     return token
    # elif "error" in resource.json():
    #     print(f'Ошибка токена: {resource.json()}')











