import unittest
from models.designer import Designer
from models.product import Product

class TestDesigner(unittest.TestCase):

    def setUp(self):
        self.designer = Designer('Claire', 'claire@gmail.com','active', 2)
       
    def test_designer_has_name(self):
        self.assertEqual('Claire', self.designer.name)          
     
    def test_designer_has_email(self):
        self.assertEqual('claire@gmail.com', self.designer.email)

    def test_detail(self):
        self.assertEqual('Name: Claire Email: claire@gmail.com', self.designer.detail())
    
    def test_designer_has_id(self):
        self.assertEqual(2, self.designer.id)

    def test_status(self):
        self.assertEqual('active', self.designer.status)