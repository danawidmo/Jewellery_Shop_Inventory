from models.designer import Designer


class Product:
    def __init__(self,  product_name, type, description, quantity, cost, price, designer, id = None):
        self.id = id
        self.product_name = product_name
        self.type = type
        self.description = description
        self.quantity = quantity
        self.cost = cost
        self.price = price
        self.designer = designer



    def low_stock(self):
        low_quantity= 5
        if self.quantity <= low_quantity and self.quantity > 0:
            return True
        else:
            return False

    def out_of_stock(self):
        if self.quantity <= 0:
            return True
        else:
            return False

    def calculate_markup(self):
        markup = self.price - self.cost
        return markup