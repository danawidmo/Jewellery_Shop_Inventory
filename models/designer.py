class Designer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def designer_detail(self):
        return f'Name: {self.name} Email: {self.email}'