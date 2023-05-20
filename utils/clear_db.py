from psycopg2 import Error
from environment import Env
import psycopg2


def clear_db():
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(user=Env.db_user,
                                      password=Env.db_password,
                                      host=Env.db_host
                                      )

        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Выполнение SQL-запроса для удаления магазинов
        cursor.execute(f"Delete from customer.shop where user_id = '{Env.db_user_id}'")
        connection.commit()
        count = cursor.rowcount
        print(count, "Запись о магазинах успешно удалена")

        # Выполнение SQL-запроса для удаления склада
        cursor.execute(f"DELETE FROM customer.warehouse where user_id = '{Env.db_user_id}'")
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



