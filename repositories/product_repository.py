from db.run_sql import run_sql
from models.product import Product
import repositories.designer_repository as designer_repository


def save(product):
    sql = "INSERT INTO products (name, type, description, quantity, cost, price, designer_id) VALUES (%s, %s, %s, %s, %s,%s, %s) RETURNING *"

    values =[product.name, product.type, product.description, product.quantity, product.cost, product.price, product.designer.id]

    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = 'SELECT * FROM products ORDER by id'
    results = run_sql(sql)

    for row in results:
    
        designer = designer_repository.select(row['designer_id'])
        product = Product(row['name'], row['type'], row['description'],row['quantity'], row['cost'], row['price'], designer, row['id'] )
        products.append(product)
    return products

def select_all_by_designer(designer_id):
    products = []

    sql = "SELECT * FROM products WHERE designer_id = %s"
    value = [designer_id]
    results = run_sql(sql, value)

    for row in results:

        designer = designer_repository.select(row['designer_id'])
        product = Product(row['name'], row['type'], row['description'],row['quantity'], row['cost'], row['price'], designer, row['id'] )
        products.append(product)
    return products


def select_all_by_type(type):
    products = []

    sql = "SELECT * FROM products WHERE type = %s"
    value = [type]
    results = run_sql(sql, value)

    for row in results:

        designer = designer_repository.select(row['designer_id'])
        product = Product(row['name'], row['type'], row['description'],row['quantity'], row['cost'], row['price'], designer, row['id'] )
        products.append(product)

    return products

def select_types():
    types =[]
    sql = "SELECT type FROM products GROUP by type"
    results =run_sql(sql)
    
    for result in results:
        type = result['type']
        types.append(type)

    return types

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    value =[id]
    result = run_sql(sql, value)[0]
    
    if result is not None:
        designer = designer_repository.select(result['designer_id'])
        product = Product(result['name'], result['type'], result['description'], result['quantity'], result['cost'], result['price'], designer, result['id'])
    return product

def update(product):
    sql = "UPDATE products SET (name, type, description, quantity, cost, price, designer_id)=(%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values =[product.name, product.type, product.description, product.quantity, product.cost, product.price, product.designer.id, product.id]
    run_sql(sql, values)
