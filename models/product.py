class Product:
    def __init__(self, sku, name, stock, category, minimum, price, supplier):
        self.sku = sku
        self.name = name
        self.stock = stock
        self.category = category
        self.minimum = minimum
        self.price = price
        self.supplier = supplier

    def describe(self):
        return f"{self.sku} - {self.name} ({self.category})"
