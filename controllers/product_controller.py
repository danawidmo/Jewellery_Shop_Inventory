from flask import render_template, request, Blueprint
from models.product import Product
import repositories.product_repository as product_repository

product_blueprint = Blueprint('product', __name__)


# INDEX
# Currently this is defined in app.py could be redirecting here instead

# SHOW
@product_blueprint.route("/products/<id>")
def product(id):
    product = product_repository.select(id)
    return render_template('/products/show.html', product=product)