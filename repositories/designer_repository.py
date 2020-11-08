from db.run_sql import run_sql
from models.designer import Designer
from models.product import Product

def save(designer):
    sql = "INSERT INTO designers (designer_name, email) VALUES (%s, %s) RETURNING *" 
    values = [designer.designer_name, designer.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    designer.id =id
    return designer