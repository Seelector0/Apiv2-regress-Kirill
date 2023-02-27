from dotenv import load_dotenv
import os

load_dotenv()

"""Выбор окружения в зависимости от указанного в файле .env"""


class Env:
    if os.environ.get('STAGE') == 'Local':
        URL = os.environ.get('URL_LOCAL')
        client_id = os.environ.get('CLIENT_ID_LOCAL')
        client_secret = os.environ.get('CLIENT_SECRET_LOCAL')
    elif os.environ.get('STAGE') == 'Develop':
        URL = os.environ.get('URL')
        client_id = os.environ.get('CLIENT_ID')
        client_secret = os.environ.get('CLIENT_SECRET')
