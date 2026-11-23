class Service:
    """Услуга химчистки: наименование, категория, базовая цена."""

    def __init__(self, service_id, name, category, base_price):
        self.service_id = service_id
        self.name = name
        self.category = category      # например: "стирка", "химчистка", "глажка"
        self.base_price = base_price  # базовая цена в рублях

    def __repr__(self):
        return f"Service({self.service_id}, {self.name!r}, {self.base_price} руб.)"


class PriceList:
    """Справочник услуг — прайс-лист организации."""

    def __init__(self):
        self._services = {}

    def add(self, service):
        self._services[service.service_id] = service

    def get(self, service_id):
        if service_id not in self._services:
            raise KeyError(f"Услуга {service_id} не найдена в прайс-листе")
        return self._services[service_id]

    def all(self):
        return list(self._services.values())
