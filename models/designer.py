class Designer:
    def __init__(self, designer_name, email, status, id = None):
        self.designer_name = designer_name
        self.email = email
        self.status = status
        self.id =id

    def detail(self):
        return f'Name: {self.designer_name} Email: {self.email}'