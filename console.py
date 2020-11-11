
from models.designer import Designer
from models.product import Product

import repositories.designer_repository as designer_repository
import repositories.product_repository as product_repository

designer_repository.delete_all()
product_repository.delete_all()

designer1 = Designer('Claire', 'claire@gmail.com','active', 1)
designer2 = Designer('Toni', 'toni@gmail.com','active', 2)

designer_repository.save(designer1)
designer_repository.save(designer2)


product1 = Product('Gold Ring', 'ring','Golden ring with garnet stone', 10, 100, 200, designer1, 1)
product2 = Product('Silver Ring', 'ring', 'Silver ring with amethyst stone', 8, 90, 180, designer2, 2) 

product_repository.save(product1)
product_repository.save(product2)

designer2.email = 'toni23@gmail.com'
designer_repository.update(designer2)

product1.quantity = 20
product_repository.update(product1)


