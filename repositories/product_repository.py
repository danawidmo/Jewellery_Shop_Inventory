from db.run_sql import run_sql
from models.product import Product
import repositories.designer_repository as designer_repository


def save(product):
    sql = "INSERT INTO products (product_name, description, quantity, cost, price, designer_id) VALUES (%s, %s, %s, %s,%s, %s) RETURNING *"

    values =[product.product_name, product.description, product.quantity, product.cost, product.price, product.designer_id]

    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = 'SELECT * FROM products'
    results = run_sql(sql)

    for row in results:
    
        designer = designer_repository.select(row['designer_id'])
        product = Product(row['product_name'], row['description'],row['quantity'], row['cost'], row['price'], designer.id, )
        products.append(product)
    return products

def delete_all():
    sql = "DELETE FROM designers"
    run_sql(sql)