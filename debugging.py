# from mimesis import Address
# from random import randint
#
# print(Address('ru').address())
# print(randint(100, 9999))


jsons = {
    "name": 'Shop Int PUT',
    "uri": '345345',
    "phone": "534553",
    "sender": "Тестов Тест Тестович"
}
print(jsons.get('uri'))


# def check_json_value(field_name: tuple, expected_value: tuple):
#     check_info = jsons.get(tuple)
#     print(check_info)
#     assert tuple(check_info) == tuple(expected_value)
#     print(f'{field_name} верен!!!')
#
#
# check_json_value(field_name=('uri', 'name'), expected_value=('345345', 'Shop Int PUT'))
