class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self, discount):
        if discount < 0 or discount > 1:
            raise ValueError("Discount must be between 0 and 1")
        self.price *= (1 - discount)


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def get_total_inventory_value(self):
        return sum(p.calculate_total_price() for p in self.products)

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

