from flask import render_template, request, Blueprint
from models.product import Product

product_blueprint = Blueprint('product', __name__)


