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




result = re.search('(\/v2\/customer\/warehouses\/)(.+)$', '/v2/customer/warehouses/4932d0ca-096c-4464-8fb8-eef509d9f86b')
print(result)
print(f'\033[1m vcx')