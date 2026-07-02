from datetime import datetime


class Movement:
    def __init__(self, sku, type, quantity, date=None):
        self.sku = sku
        self.type = type          # "venda" ou "recebimento"
        self.quantity = quantity
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "sku": self.sku,
            "type": self.type,
            "quantity": self.quantity,
            "date": self.date
        }