
from models.designer import Designer
from models.product import Product

import repositories.designer_repository as designer_repository
import repositories.product_repository as product_repository

designer1 = Designer('Claire', 'claire@gmail.com', 1)
designer2 = Designer('Toni', 'toni@gmail.com', 2)

designer_repository.save(designer1)
designer_repository.save(designer2)


product1 = Product('Gold Ring', 'Golden ring with garnet stone', 10, 100, 200, designer1.id, 1)
product2 = Product('Silver Ring', 'Silver ring with amethyst stone', 8, 90, 180, designer2.id, 2) 

product_repository.save(product1)
product_repository.save(product2)


