# from mimesis import Address
# from random import randint
#
# print(Address('ru').address())
# print(randint(100, 9999))
import re

# jsons = {
#     "name": 'Shop Int PUT',
#     "uri": '345345',
#     "phone": "534553",
#     "sender": "Тестов Тест Тестович"
# }
# print(jsons.get('uri'))


# def check_json_value(field_name: tuple, expected_value: tuple):
#     check_info = jsons.get(tuple)
#     print(check_info)
#     assert tuple(check_info) == tuple(expected_value)
#     print(f'{field_name} верен!!!')
#
#
# check_json_value(field_name=('uri', 'name'), expected_value=('345345', 'Shop Int PUT'))


# def check_if_response_value_match_regexp_as_expected(target: str, regexp_pattern: str, check_value):
#     with allure.step(f"TEST: Response value {target} matchs regexp {regexp_pattern}"):
#
#         try:
#             result = re.search(regexp_pattern, target)
#             assert check_value == result.group(1)
#
#         except (AttributeError, AssertionError) as error:
#             Api.LOGGER.error("Checking that response value {} match regexp check_value {}: FAILED\n"
#                              .format(check_value,
#                                      result.group(1)))
#             raise AssertionError(
#                 f"TEST FAILED: Response value {target} matchs regexp {regexp_pattern}. Reason: {error}")
#
# CheckCases.check_if_response_value_match_regexp_as_expected(target=result_json['url'],
#                                                                     regexp_pattern=r'\/warehouses\/(.+)$',
#                                                                     check_value=self.WAREHOUSE_ID)



#
# result = re.search('(\/v2\/customer\/warehouses\/)(.+)$', '/v2/customer/warehouses/4932d0ca-096c-4464-8fb8-eef509d9f86b')
# print(result)
# print(f'\033[1m vcx')


# import psycopg2
# from psycopg2 import Error
#
#
# def clear_db(shop_id='null', warehouse_id='null'):
#     try:
#         # Подключение к базе данных
#         connection = psycopg2.connect(user="metaship",
#                                       password="ohiXahfPbWVeSfF7uMsBYjWD",
#                                       host="localhost",
#                                       port="5432",
#                                       database="metaship")
#
#         # # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()
#
#         # Выполнение SQL-запроса для удаления магазинов
#         cursor.execute(f"Delete from customer.shop where id NOT IN ({shop_id})")
#         connection.commit()
#         count = cursor.rowcount
#         print(count, "Запись о магазинах успешно удалена")
#
#         # Выполнение SQL-запроса для удаления склада
#         cursor.execute(f"DELETE FROM customer.warehouse where id != {warehouse_id}")
#         connection.commit()
#         count = cursor.rowcount
#         print(count, "Запись о складах успешно удалена")
#
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#             print("Соединение с PostgreSQL закрыто")
#
# # Указать магазин и склад, который не нужно удалять
# shop_id = f"'0aa93846-8b8c-4393-8897-40ed9d74c8dc', '5b0291e4-70de-4684-94e2-6a1ab8a3b802'"
# # warehouse_id = f"'25281a75-15f1-451b-baeb-46ca6eb7c7cc'"
#
# clear_db(shop_id=shop_id)
