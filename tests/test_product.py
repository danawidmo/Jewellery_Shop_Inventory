import unittest
from models.product import Product
from models.designer import Designer

class TestProduct(unittest.TestCase):
    def setUp(self):

        self.designer = Designer('Dana', 'dana@gmail.com', 1)
        self.product = Product('Gold Ring', 'Golden ring with garnet stone', 10, 100, 200, self.designer, 3)
        self.product2 = Product('Silver Ring', 'Silver ring with garnet stone', 4, 100, 200, self.designer, 3)
        self.product3 = Product('Bronze Ring', 'Bronze ring with garnet stone', 0, 100, 200, self.designer, 3)

    def test_product_has_product_name(self):
        self.assertEqual('Gold Ring', self.product.product_name)

    def test_product_has_description(self):
        self.assertEqual('Golden ring with garnet stone', self.product.description)

    def test_product_has_quantity(self):
        self.assertEqual(10, self.product.quantity)

    def test_product_has_cost(self):
        self.assertEqual(100, self.product.cost)

    def test_product_has_price(self):
        self.assertEqual(200, self.product.price)

    def test_product_has_designer(self):
        self.assertEqual(1, self.product.designer.id)

    def test_product_has_id(self):
        self.assertEqual(3, self.product.id)

    def test_low_stock(self):
        self.assertEqual(True, self.product2.low_stock())

    def test_low_stock_is_0(self):
        self.assertEqual(False, self.product3.low_stock())