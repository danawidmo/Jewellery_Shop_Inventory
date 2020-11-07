class Designer:
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id =id

    def designer_detail(self):
        return f'Name: {self.name} Email: {self.email}'