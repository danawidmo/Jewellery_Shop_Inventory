from flask import render_template, request, Blueprint, redirect
import repositories.designer_repository as designer_repository
import repositories.product_repository as product_repository
from models.designer import Designer


designer_blueprint = Blueprint('designers', __name__)


# INDEX
# Note the blueprint name is designer, the route is designers!
@designer_blueprint.route("/designers")
def designers():
    designers = designer_repository.select_all()
    return render_template('designers/index.html',designers=designers)

# SHOW
@designer_blueprint.route("/designers/<id>")
def show_designer(id):
    designer = designer_repository.select(id)
    products = product_repository.select_all_by_designer(id)
    return render_template('designers/show.html', designer=designer, products=products)

# EDIT
@designer_blueprint.route("/designers/<id>/edit")
def edit_designer(id):
    designer = designer_repository.select(id)
    return render_template('designers/edit.html', designer=designer)

# UPDATE

@designer_blueprint.route("/designers/<id>", methods = ['POST'])
def update_designer(id):
    designer_name = request.form['designer_name']
    email = request.form['email']
    status = request.form['status']
    designer = Designer(designer_name, email, status, id)
    designer_repository.update(designer)
    return redirect('/designers')

# CREATE
# GET
@designer_blueprint.route("/designers/new")
def new_designer():
    return render_template("designers/new.html")

# CREATE POST
@designer_blueprint.route("/designers/new", methods = ['POST'])
def create_designer():
    designer_name = request.form['designer_name']
    email = request.form['email']
    status = 'active'
    designer = Designer(designer_name, email, status)
    designer_repository.save(designer)
    return redirect('/designers')



