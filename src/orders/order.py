from datetime import date, timedelta


class Order:
    """Заказ химчистки: клиент, изделие, услуги, статус."""

    ACCEPTED = "принят"
    IN_WORK = "в работе"
    READY = "готов"
    ISSUED = "выдан"

    def __init__(self, order_id, client, item):
        self.order_id = order_id
        self.client = client
        self.item = item
        self.services = []
        self.status = Order.ACCEPTED
        self.discount = 0
        self.is_urgent = False

    def add_service(self, service):
        """Добавить услугу в заказ."""
        self.services.append(service)

    def apply_discount(self, percent):
        """Применить накопительную скидку клиента."""
        if 0 < percent <= 50:
            self.discount = percent
        return self.total_cost()

    def total_cost(self):
        """Стоимость заказа с учётом срочности и скидки."""
        total = sum(s.base_price for s in self.services)
        if self.is_urgent:
            total = int(total * 1.3)
        return int(total * (1 - self.discount / 100))

    def set_status(self, new_status):
        """Смена статуса только по допустимым переходам."""
        allowed = {
            Order.ACCEPTED: [Order.IN_WORK],
            Order.IN_WORK: [Order.READY],
            Order.READY: [Order.ISSUED],
        }
        if new_status not in allowed.get(self.status, []):
            raise ValueError(
                f"Недопустимый переход статуса: {self.status} -> {new_status}")
        self.status = new_status
