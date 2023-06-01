from utils.api.api_order import OrderApi


def checking_state_order(order_id, headers):
    counter = 0
    result = OrderApi.get_orders(order_id, headers)
    while result.json()["state"] in ["created", "registered", "external-processing"] and counter < 50:
        result = OrderApi.get_orders(order_id, headers)
        counter += 1
    # Проверяем, был ли достигнут максимальный счетчик циклов и закончились ли возможные статусы заказа
    if counter >= 50 and result.json()["state"] in ["created", "registered", "external-processing"]:
        raise AssertionError("Ошибка: Статус заказа не изменился")

