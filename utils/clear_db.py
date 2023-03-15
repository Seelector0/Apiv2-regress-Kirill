import psycopg2
from psycopg2 import Error

from environment import Env


def clear_db(shop_id='null', warehouse_id='null'):
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=Env.db_user,
                                      password=Env.db_password,
                                      host=Env.db_host
                                      )

        # # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Выполнение SQL-запроса для удаления магазинов
        cursor.execute(f"Delete from customer.shop where id = {shop_id}")
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись о магазинах успешно удалена")

        # Выполнение SQL-запроса для удаления склада
        cursor.execute(f"DELETE FROM customer.warehouse where id = {warehouse_id}")
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись о складах успешно удалена")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
