from db.run_sql import run_sql
from models.designer import Designer
from models.product import Product


def save(product):
    sql = "INSERT INTO products (product_name, description, quantity, cost, price, designer_id) VALUES (%s, %s, %s, %s,%s, %s) RETURNING *"

    values =[product.product_name, product.description, product.quantity, product.cost, product.price, product.designer_id]

    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

