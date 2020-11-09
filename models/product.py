from models.designer import Designer


class Product:
    def __init__(self,  product_name, description, quantity, cost, price, designer_id, id = None,):
        self.id = id
        self.product_name = product_name
        self.description = description
        self.quantity = quantity
        self.cost = cost
        self.price = price
        self.designer_id = designer_id