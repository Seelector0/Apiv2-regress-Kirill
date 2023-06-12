from psycopg2 import Error

from environment import Env
import psycopg2


def connect_to_database(database=None):
    """Подключение к БД"""
    try:
        connection = psycopg2.connect(database=database, user=Env.db_user,
                                      password=Env.db_password, host=Env.db_host)
        return connection
    except (Exception, Error) as errors:
        print("Ошибка при подключении к базе данных", errors)
        return None


def delete_records(connection, cursor, table, condition, value):
    """Удаление записи из БД"""
    try:
        cursor.execute(f"DELETE FROM {table} where {condition} = '{value}'")
        connection.commit()
        counts = cursor.rowcount
        print(counts, f"записей из таблицы {table} успешно удалены")
    except (Exception, Error) as errors:
        print("Ошибка при удалении записей", errors)


def delete_records_related(connection, cursor, table_1, table_2, condition_1, condition_2, value):
    """Удаление связанных записей из одной БД"""
    try:
        cursor.execute(f"""
            DELETE FROM {table_1}
            WHERE {condition_1} IN (
                SELECT id FROM {table_2} WHERE {condition_2} = %s
            )
        """, (value,))
        connection.commit()
        counts = cursor.rowcount
        print(counts, f"записей из таблицы {table_1} успешно удалены")
    except (Exception, Error) as errors:
        print("Ошибка при удалении записей", errors)


def delete_records_cycle(connection, cursor, table, condition, ids):
    """Удаление записей циклом из БД"""
    try:
        counts = 0
        for i in ids:
            cursor.execute(f"DELETE FROM {table} where {condition} = '{i}'")
            counts += cursor.rowcount
        connection.commit()
        print(counts, f"записей из таблицы {table} успешно удалены")
    except (Exception, Error) as errors:
        print("Ошибка при удалении записей", errors)


def get_id(cursor, column, table, condition, value):
    """Получение id, для удаления связанных записей из разных БД"""
    cursor.execute(f"SELECT {column} FROM {table} where {condition} = '{value}'")
    rows = cursor.fetchall()
    ids = []
    for i in rows:
        ids.append(i[0])
    return ids


def clear_db():
    """Очистка БД"""
    try:
        # Подключение к базе данных "metaship"
        connection_metaship = connect_to_database()
        cursor_metaship = connection_metaship.cursor()

        # Подключение к базе данных "customer-api"
        connection_customer_api = connect_to_database(database="customer-api")
        cursor_customer_api = connection_customer_api.cursor()

        # Подключение к базе данных "tracking-api"
        connection_tracking_api = connect_to_database(database="tracking-api")
        cursor_tracking_api = connection_tracking_api.cursor()

        # Выполнение SQL-запроса для получения shop_id, для отчистки БД customer-api
        shop_ids = get_id(cursor=cursor_metaship, column='id', table='customer.shop', condition='user_id',
                          value=Env.db_user_id)

        # Выполнение SQL-запроса для получения order_id, для отчистки БД tracking-api
        order_ids = get_id(cursor=cursor_metaship, column='id', table='"order"."order"', condition='user_id',
                           value=Env.db_user_id)

        # Выполнение SQL-запроса для получения connection_id
        connection_ids = []
        for shop_id in shop_ids:
            cursor_customer_api.execute(f"SELECT id FROM public.connection where shop_id = '{shop_id}'")
            customer_api_rows = cursor_customer_api.fetchall()
            for row in customer_api_rows:
                connection_ids.append(row[0])

        # Выполнение SQL-запроса для удаления магазинов
        delete_records(connection=connection_metaship, cursor=cursor_metaship, table='customer.shop',
                       condition='user_id',
                       value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления склада
        delete_records(connection=connection_metaship, cursor=cursor_metaship, table='customer.warehouse',
                       condition='user_id', value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления подключений
        delete_records(connection=connection_metaship, cursor=cursor_metaship, table='customer.credential',
                       condition='user_id', value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления черновиков
        delete_records(connection=connection_metaship, cursor=cursor_metaship, table='"order".draft',
                       condition='user_id', value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления связанных записей в таблице "order.order_document"
        delete_records_related(connection=connection_metaship, cursor=cursor_metaship, table_1='"order".order_document',
                               condition_1='order_id', table_2='"order"."order"', condition_2='user_id',
                               value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления заказов
        delete_records(connection=connection_metaship, cursor=cursor_metaship, table='"order"."order"',
                       condition='user_id', value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления патчей заказа
        delete_records(connection=connection_metaship, cursor=cursor_metaship, table='"order".order_patch',
                       condition='user_id', value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления связанных записей в таблице "order.order_parcel"
        delete_records_related(connection=connection_metaship, cursor=cursor_metaship, table_1='"order".order_parcel',
                               condition_1='parcel_id', table_2='"order".parcel', condition_2='user_id',
                               value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления партий
        delete_records(connection=connection_metaship, cursor=cursor_metaship, table='"order".parcel',
                       condition='user_id', value=Env.db_user_id)

        # Выполнение SQL-запроса для удаления данных из таблицы customer_api.public.configuration
        delete_records_cycle(connection=connection_customer_api, cursor=cursor_customer_api,
                             table='public.configuration',
                             condition='connection_id', ids=connection_ids)

        # Выполнение SQL-запроса для удаления данных из таблицы customer_api.public.connection
        delete_records_cycle(connection=connection_customer_api, cursor=cursor_customer_api, table='public.connection',
                             condition='shop_id', ids=shop_ids)

        # Выполнение SQL-запроса для удаления данных из таблицы tracking_api.public.order
        delete_records_cycle(connection=connection_tracking_api, cursor=cursor_tracking_api, table='public."order"',
                             condition='order_id', ids=order_ids)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection_metaship:
            cursor_metaship.close()
            connection_metaship.close()
            print("Соединение с базой данных 'metaship' закрыто")
        if connection_customer_api:
            cursor_customer_api.close()
            connection_customer_api.close()
            print("Соединение с базой данных 'customer-api' закрыто")
        if connection_tracking_api:
            cursor_tracking_api.close()
            connection_tracking_api.close()
            print("Соединение с базой данных 'tracking-api' закрыто")
