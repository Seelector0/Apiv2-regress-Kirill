from utils.api.api_delivery_service import DeliveryServiceApi
from utils.api.api_order import OrderApi
from utils.api.api_parcelr import ParcelApi
from utils.checking import Checking
import allure
import pytest


@allure.epic("№3_Подключение Почты России")
class TestDeliveryService:

    @allure.title("Создание подключения POST")
    def test_post_connection(self, access_token, connection, shop):
        result_post_connections = connection[0]
        Checking.check_status_code(result=result_post_connections, status_code=201)
        Checking.check_json_required_keys(result=result_post_connections, required_key=['id', 'type', 'url', 'status'])
        Checking.check_json_value(result=result_post_connections, key_name='type', expected_value='Delivery')
        Checking.check_json_value(result=result_post_connections, key_name='status', expected_value=201)
        Checking.check_json_search_regexp_in_value(result=result_post_connections.json().get('url'),
                                                   check_value=shop[1],
                                                   regexp_pattern=r'\/shops\/(.+)\/delivery_services\/.*')

    @allure.title("Получение настроек службы доставки GET")
    def test_get_connection(self, access_token, shop):
        result_get_connections = DeliveryServiceApi.get_delivery_service_code(shop_id=shop[1], headers=access_token,
                                                                              code='RussianPost')
        Checking.check_status_code(result=result_get_connections, status_code=200)
        Checking.check_json_required_keys(result=result_get_connections, required_key=['code', 'name', 'hasAggregation',
                                                                                       'credentials'])
        Checking.check_json_value(result=result_get_connections, key_name='code', expected_value='RussianPost')
        Checking.check_json_value(result=result_get_connections, key_name='name', expected_value='Почта России')
        Checking.check_json_value(result=result_get_connections, key_name='hasAggregation', expected_value=True)
        Checking.check_json_value_nested(result=result_get_connections, key_tuple=('credentials', 'data', 'type'),
                                         expected_value="integration")

    @allure.title("Получение настроек всех служб доставки GET")
    def test_get_all_connection(self, access_token, shop):
        result_get_all_connections = DeliveryServiceApi.get_delivery_service(shop_id=shop[1], headers=access_token)
        Checking.check_status_code(result=result_get_all_connections, status_code=200)
        Checking.check_json_required_keys_array(result=result_get_all_connections, required_key=['code', 'name',
                                                                                                 'hasAggregation', 'id',
                                                                                                 'active', 'visibility',
                                                                                                 'type', 'moderation'])

    @allure.title("Редактирование полей службы доставки PATCH")
    def test_patch_connection(self, access_token, shop):
        result_patch_connections = DeliveryServiceApi.patch_delivery_service_code(shop_id=shop[1], code='RussianPost',
                                                                                  headers=access_token)
        Checking.check_status_code(result=result_patch_connections, status_code=200)
        Checking.check_json_required_keys(result=result_patch_connections,
                                          required_key=['code', 'name', 'hasAggregation',
                                                        'credentials'])

        Checking.check_json_value_nested(result=result_patch_connections, key_tuple=('credentials', 'visibility'),
                                         expected_value=False)

        Checking.check_json_value_nested(result=result_patch_connections,
                                         key_tuple=('credentials', 'settings', 'tariffs', 'restrict'),
                                         expected_value=None)

        Checking.check_json_value_nested(result=result_patch_connections,
                                         key_tuple=('credentials', 'settings', 'tariffs', 'exclude'),
                                         expected_value=['14', '25'])

    @allure.title("Обновление службы доставки PUT")
    def test_put_connection(self, access_token, shop):
        result_put_connections = DeliveryServiceApi.put_delivery_service(shop_id=shop[1], code='RussianPost',
                                                                         headers=access_token)
        Checking.check_status_code(result=result_put_connections, status_code=409)

    @allure.title("Удаление службы доставки DELETE")
    def test_delete_connection(self, access_token, shop):
        result_delete_connections = DeliveryServiceApi.delete_delivery_service(shop_id=shop[1], code='RussianPost',
                                                                               headers=access_token)
        Checking.check_status_code(result=result_delete_connections, status_code=409)

    @allure.title("Деактивация службы доставки POST")
    def test_deactivate_connection(self, access_token, shop):
        result_deactivate_connections = DeliveryServiceApi.delivery_service_deactivate(shop_id=shop[1],
                                                                                       code='RussianPost',
                                                                                       headers=access_token)
        Checking.check_status_code(result=result_deactivate_connections, status_code=204)

    @allure.title("Активация службы доставки POST")
    def test_activate_connection(self, access_token, shop):
        result_activate_connections = DeliveryServiceApi.delivery_service_activate(shop_id=shop[1], code='RussianPost',
                                                                                   headers=access_token)
        Checking.check_status_code(result=result_activate_connections, status_code=204)


@allure.epic("№4_Заказы Почты России")
class TestOrder:
    order_ids = {}
    @allure.title("Создание заказа POST")
    @pytest.mark.parametrize("payment_type", ["Paid", "PayOnDelivery"])
    def test_post_order(self, access_token, shop, warehouse, payment_type):
        result_post_order = OrderApi.create_order(shop_id=shop[1], warehouse_id=warehouse[1], headers=access_token,
                                                  payment_type=payment_type, delivery_type='PostOffice')

        order_id = result_post_order.json()["id"]
        TestOrder.order_ids[payment_type] = order_id  # Сохранение id заказа в словаре
        Checking.check_status_code(result=result_post_order, status_code=202)
        Checking.check_json_required_keys(result=result_post_order, required_key=['id', 'type', 'url', 'status'])
        Checking.check_json_value(result=result_post_order, key_name='type', expected_value='Order')
        Checking.check_json_value(result=result_post_order, key_name='status', expected_value=201)
        Checking.check_json_search_regexp_in_value(result=result_post_order.json().get('url'),
                                                   check_value=result_post_order.json().get('id'),
                                                   regexp_pattern=r'\/orders\/(.+)$')

    def test_get_all_orders(self, access_token):
        result_get_all_orders = OrderApi.get_orders_all(headers=access_token)
        Checking.check_status_code(result=result_get_all_orders, status_code=200)
        Checking.check_unique_ids(result=result_get_all_orders, id_key='id')
        Checking.check_json_required_keys_array(result=result_get_all_orders,
                                                required_key=['id', 'number', 'addressTo', 'data', 'parcel', 'status',
                                                              'statusReason', 'state', 'stateMessage', 'created'])

    @pytest.mark.parametrize("payment_type", ["Paid", "PayOnDelivery"])
    def test_get_order(self, access_token, payment_type):
        order_id = TestOrder.order_ids.get(payment_type)  # Получение сохраненного id заказа
        Checking.checking_state_order(order_id=order_id, headers=access_token)
        result_get_order = OrderApi.get_orders(order_id=order_id, headers=access_token, x_trace_id="Get_order_test")
        Checking.check_status_code(result=result_get_order, status_code=2002)
        Checking.check_json_required_keys(result=result_get_order, required_key=['id', 'number', 'addressTo', 'data',
                                                                                 'parcel', 'status', 'statusReason',
                                                                                 'state', 'stateMessage', 'created'])
        Checking.check_json_value(result=result_get_order, key_name='id', expected_value=order_id)
        Checking.check_response_body_key_not_empty(result=result_get_order, key='data')
        Checking.check_json_value_nested(result=result_get_order, key_tuple=('data', 'request', 'payment', 'type'),
                                         expected_value="Paid")
        Checking.check_json_value(result=result_get_order, key_name='status', expected_value='created')


@allure.epic("№5_Заказы Почты России")
class TestParcel:
    @pytest.mark.parametrize("payment_type", ["Paid", "PayOnDelivery"])
    def test_create_new_parcel(self, access_token, shop, warehouse, payment_type):
        order_id = TestOrder.order_ids.get(payment_type)
        result_post_parcel = ParcelApi.create_parcel(order_id=order_id, headers=access_token)
        Checking.check_status_code(result=result_post_parcel, status_code=207)

# def test_create_new_parcel_2(new_parcel, access_token):
#     print(new_parcel)
#     print(new_parcel.json().get('id'))
#
# def test_create_new_order3(new_order, access_token):
#     print(new_order)
#     print(new_order.json().get('id'))


# def test_create_new_order(new_order, access_token):
#     # result_post_warehouse = new_warehouse
#     # warehouse_id = result_post_warehouse.json().get('id')
#     # result_post_shop = new_shop
#     # shop_id = result_post_shop.json().get('id')
#     # result_post_order = OrderApi.create_order(shop_id=new_shop, warehouse_id=new_warehouse, headers=access_token)
#     # order_id = result_post_order.json().get('id')
#     print(new_order)
#     print(new_order.json().get('id'))
#     # print(warehouse_id)
#     # print(shop_id)
#     # clear_db(shop_id=f"'{shop_id}'", warehouse_id=f"'{warehouse_id}'")


# def test_create_new_order3(new_order, access_token):
#     print(new_order)
#     print(new_order.json().get('id'))
