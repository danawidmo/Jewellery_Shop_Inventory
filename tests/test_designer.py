import unittest
from models.designer import Designer
from models.product import Product

class TestDesigner(unittest.TestCase):

    def setUp(self):
        self.designer = Designer('Claire', 'claire@gmail.com',2)
       
    def test_designer_has_designer_name(self):
        self.assertEqual('Claire', self.designer.designer_name)          
     
    def test_designer_has_email(self):
        self.assertEqual('claire@gmail.com', self.designer.email)

    def test_designer_detail(self):
        self.assertEqual('Name: Claire Email: claire@gmail.com', self.designer.designer_detail())
    
    def test_designer_has_id(self):
        self.assertEqual(2, self.designer.id)

