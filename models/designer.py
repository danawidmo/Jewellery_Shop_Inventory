class Designer:
    def __init__(self, designer_name, email, id = None):
        self.designer_name = designer_name
        self.email = email
        self.id =id

    def designer_detail(self):
        return f'Name: {self.designer_name} Email: {self.email}'