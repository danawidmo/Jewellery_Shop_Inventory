from flask import render_template, request, Blueprint, redirect
from models.product import Product
import repositories.product_repository as product_repository
import repositories.designer_repository as designer_repository

product_blueprint = Blueprint('product', __name__)


# INDEX
# Currently this is defined in app.py could be redirecting here instead

# SHOW
@product_blueprint.route("/products/<id>")
def product(id):
    product = product_repository.select(id)
    return render_template('/products/show.html', product=product)

# CREATE
# GET
@product_blueprint.route("/new")
def new_product():
    designers = designer_repository.select_all()
    return render_template("/products/new.html", designers=designers)

# CREATE 
# POST
@product_blueprint.route("/new", methods = ['POST'])
def create_product():
    product_name = request.form['product_name']
    type = request.form['type']
    description =request.form['description']
    quantity = request.form['quantity']
    cost = request.form['cost']
    price = request.form['price']
    designer_id = request.form['designer']
    designer = designer_repository.select(designer_id)
    product = Product(product_name, type, description, quantity, cost, price, designer)
    product_repository.save(product)
    return redirect('/')

# EDIT
@product_blueprint.route("/products/<id>/edit")
def edit_product(id):
    product = product_repository.select(id)
    designers = designer_repository.select_all()
    return render_template('/products/edit.html', product=product, designers=designers)

# UPDATE
@product_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    product_name = request.form['product_name']
    type = request.form['type']
    description =request.form['description']
    quantity = request.form['quantity']
    cost = request.form['cost']
    price = request.form['price']
    designer_id = request.form['designer']
    designer = designer_repository.select(designer_id)
    product = Product(product_name, type, description, quantity, cost, price, designer, id)
    product_repository.update(product)
    return redirect('/')