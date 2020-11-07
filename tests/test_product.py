import unittest
from models.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):

        self.product = Product('Gold Ring', 'Golden ring with garnet stone', 10, 100, 200 )

    def test_product_has_name(self):
        self.assertEqual('Gold Ring', self.product.name)

    def test_product_has_description(self):
        self.assertEqual('Golden ring with garnet stone', self.product.description)

    def test_product_has_quantity(self):
        self.assertEqual(10, self.product.quantity)

    def test_product_has_cost(self):
        self.assertEqual(100, self.product.cost)

    def test_product_has_price(self):
        self.assertEqual(200, self.product.price)