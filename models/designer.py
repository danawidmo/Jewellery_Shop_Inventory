class Designer:
    def __init__(self, name, email, status, id = None):
        self.name = name
        self.email = email
        self.status = status
        self.id =id

    def detail(self):
        return f'Name: {self.name} Email: {self.email}'