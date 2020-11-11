from db.run_sql import run_sql
from models.designer import Designer
from models.product import Product

def save(designer):
    sql = "INSERT INTO designers (name, email, status) VALUES (%s, %s, %s) RETURNING *" 
    values = [designer.name, designer.email, designer.status]
    results = run_sql(sql, values)
    id = results[0]['id']
    designer.id =id
    return designer


def select_all():
    designers =[]
    sql = "SELECT * from designers"
    results = run_sql(sql)

    for row in results:
        designer = Designer(row['name'], row['email'], row['status'], row['id'])
        designers.append(designer)
    return designers


def select(id):
    designer = None
    sql = "SELECT * FROM designers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
  
    if result is not None:
        designer = Designer(result['name'], result['email'], result['status'],result['id'])
    return designer

def delete_all():
    sql = "DELETE FROM designers"
    run_sql(sql)

def update(designer):
    sql = "UPDATE designers SET (name, email, status)=(%s, %s, %s) WHERE id = %s"
    values = [designer.name, designer.email, designer.status, designer.id]
    run_sql(sql,values)

    