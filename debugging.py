import pytest
import requests
from environment import Env



def access_token():
    """Получение Brear_Token"""
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = dict(grant_type="client_credentials", client_id=Env.client_id, client_secret=Env.client_secret)
    resource = requests.post(url=f'{Env.URL}/auth/access_token', data=data, headers=headers)
    print(resource.url)
    # token = {
    #     "Authorization": f"Bearer {resource.json()['access_token']}"
    #     # 'Content-Type': "application/json"
    # }
    # print(token)

access_token()