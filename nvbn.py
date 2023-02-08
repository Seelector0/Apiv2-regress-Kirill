import requests

"""Exchange authorization code for an access token"""

headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        # "Accept": "application/json;charset=UTF-8"
    }

data = {
        "grant_type": "client_credentials",
        'client_id': "b912d871-fa13-4edc-8606-656a461e7dfb",
        'client_secret': "c0b33e8d8abd097cd0a17c7521ed49558166698d06f99fcba1483545e062e866ee8083326a4b323c"
    }

res = requests.post('http://apiv2.localhost/auth/access_token', data=data, headers=headers)
token = {
        "Authorization": f"Bearer {res.json()['access_token']}"
    }
print(token)
# if "access_token" in res.json():
#     token = res.json()['access_token']
# elif "error" in res.json():
#     print(f'Ошибка токена: {res.json()}')




# if "error" in res.json():
#     print(f'Ошибка токена: {res.json()}')
# else:
#     token = res.json()['access_token']





# headers = {
#         "Authorization": f'Bearer {token}'
#     }
#
# res_get = requests.get('http://apiv2.localhost/v2/customer/shops/5647604a-e2a2-4711-ba6b-146e9d23229c', headers=headers)
# print(res_get.text)