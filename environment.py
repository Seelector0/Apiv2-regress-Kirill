from dotenv import load_dotenv
import os

load_dotenv()

"""Выбор окружения в зависимости от указанного в файле .env"""


class Env:

    if os.environ.get('STAGE') == 'Local':
        URL = os.environ.get('URL_LOCAL')
        client_id = os.environ.get('CLIENT_ID_LOCAL')
        client_secret = os.environ.get('CLIENT_SECRET_LOCAL')
        db_user = os.environ.get('DB_USER_LOCAL')
        db_password = os.environ.get('DB_PASSWORD_LOCAL')
        db_host = os.environ.get('DB_HOST_LOCAL')
        db_user_id = os.environ.get('USER_ID_LOCAl')
    elif os.environ.get('STAGE') == 'Develop':
        URL = os.environ.get('URL')
        client_id = os.environ.get('CLIENT_ID')
        client_secret = os.environ.get('CLIENT_SECRET')
        db_user = os.environ.get('DB_USER_DEV')
        db_password = os.environ.get('DB_PASSWORD_DEV')
        db_host = os.environ.get('DB_HOST_DEV')