import unittest
from models.designer import Designer
from models.product import Product

class TestDesigner(unittest.TestCase):

    def setUp(self):
        self.designer = Designer('Claire', 'claire@gmail.com',2)
        self.product1 = Product('Gold Ring', 'Golden ring with garnet stone', 10, 100, 200, self.designer, 3)
        self.product2 = Product('Silver Ring', 'Silver ring with amethyst stone', 8, 90, 180, self.designer, 1) 
        self.designer.products = [self.product1, self.product2] 

    def test_designer_has_name(self):
        self.assertEqual('Claire', self.designer.name)          
     
    def test_designer_has_email(self):
        self.assertEqual('claire@gmail.com', self.designer.email)

    def test_designer_detail(self):
        self.assertEqual('Name: Claire Email: claire@gmail.com', self.designer.designer_detail())
    
    def test_designer_has_id(self):
        self.assertEqual(2, self.designer.id)

    def test_designer_has_products(self):
        self.assertEqual(2, len(self.designer.products))
