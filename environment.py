from dotenv import load_dotenv
import os

load_dotenv()

"""Выбор окружения в зависимости от указанного в файле .env"""


class Env:
    db_metaship = os.environ.get('DB_METASHIPL')
    if os.environ.get('STAGE') == 'Local':
        URL = os.environ.get('URL_LOCAL')
        client_id = os.environ.get('CLIENT_ID_LOCAL')
        client_secret = os.environ.get('CLIENT_SECRET_LOCAL')
        db_user = os.environ.get('DB_USER_LOCAL')
        db_password = os.environ.get('DB_PASSWORD_LOCAL')
        db_host = os.environ.get('DB_HOST_LOCAL')
        db_port = os.environ.get('DB_PORT')
    elif os.environ.get('STAGE') == 'Develop':
        URL = os.environ.get('URL')
        client_id = os.environ.get('CLIENT_ID')
        client_secret = os.environ.get('CLIENT_SECRET')
