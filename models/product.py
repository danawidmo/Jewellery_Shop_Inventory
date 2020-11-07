class Product:
    def __init__(self,name, description, quantity, cost, price, designer, id = None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.cost = cost
        self.price = price
        self.designer = designer
        self.id = id