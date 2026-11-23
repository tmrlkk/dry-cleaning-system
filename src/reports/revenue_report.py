from collections import defaultdict


class RevenueReport:
    """Сводка выручки по периодам и категориям услуг."""

    def __init__(self):
        self._issued_orders = []   # только выданные заказы считаются выручкой

    def register_issued(self, order):
        if order.status != order.ISSUED:
            raise ValueError("Выручка учитывается только по выданным заказам")
        self._issued_orders.append(order)

    def by_category(self):
        """Сумма выручки по каждой категории услуг."""
        totals = defaultdict(int)
        for order in self._issued_orders:
            for s in order.services:
                totals[s.category] += s.base_price
        return dict(totals)

    def total(self):
        return sum(o.total_cost() for o in self._issued_orders)
