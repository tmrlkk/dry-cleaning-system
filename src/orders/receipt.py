from datetime import datetime


class Receipt:
    """Квитанция к заказу: печатная форма для клиента."""

    def __init__(self, order):
        self.order = order
        self.printed_at = datetime.now()

    def render(self):
        """Собрать текст квитанции."""
        lines = [
            "=== КВИТАНЦИЯ ХИМЧИСТКИ ===",
            f"Заказ №{self.order.order_id}",
            f"Клиент: {self.order.client.name}, тел. {self.order.client.phone}",
            f"Изделие: {self.order.item}",
            "Услуги:",
        ]
        for s in self.order.services:
            lines.append(f"  - {s.name} ({s.category}): {s.base_price} руб.")
        lines.append(f"Скидка: {self.order.discount}%")
        lines.append(f"Срочно: {'да' if self.order.is_urgent else 'нет'}")
        lines.append(f"ИТОГО: {self.order.total_cost()} руб.")
        return "\n".join(lines)
