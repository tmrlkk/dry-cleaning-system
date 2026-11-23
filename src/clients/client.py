class Client:
    """Клиент химчистки: контактные данные и накопительная скидка."""

    DISCOUNT_LEVELS = [(10000, 10), (30000, 20), (60000, 30)]  # (сумма, %)

    def __init__(self, client_id, name, phone):
        self.client_id = client_id
        self.name = name
        self.phone = phone
        self.total_spent = 0          # накопленная сумма расходов
        self.orders = []              # история заказов

    def register_order(self, order):
        """Привязать заказ к клиенту и пересчитать накопления."""
        self.orders.append(order)
        self.total_spent += order.total_cost()

    def current_discount(self):
        """Накопительная скидка по сумме прошлых заказов."""
        discount = 0
        for threshold, percent in self.DISCOUNT_LEVELS:
            if self.total_spent >= threshold:
                discount = percent
        return discount
