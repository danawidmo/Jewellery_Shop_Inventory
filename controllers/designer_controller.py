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
    if id == 'new':
        return render_template("designers/new.html")
    else:
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
    name = request.form['name']
    email = request.form['email']
    status = request.form['status']
    designer = Designer(name, email, status, id)
    designer_repository.update(designer)
    return redirect('/designers')

# CREATE POST
@designer_blueprint.route("/designers/new", methods = ['POST'])
def create_designer():
    name = request.form['name']
    email = request.form['email']
    status = 'active'
    designer = Designer(name, email, status)
    designer_repository.save(designer)
    return redirect('/designers')



