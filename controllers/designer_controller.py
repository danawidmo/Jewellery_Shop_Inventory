from flask import render_template, request, Blueprint, redirect
import repositories.designer_repository as designer_repository
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
    return render_template('designers/show.html', designer=designer)

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
    designer = Designer(designer_name, email, id)
    designer_repository.update(designer)
    return redirect('/designers')