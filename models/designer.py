class Designer:
    def __init__(self, name, email, id = None):
        self.name = name
        self.email = email
        self.id =id
        self.products = []

    def designer_detail(self):
        return f'Name: {self.name} Email: {self.email}'