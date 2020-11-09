from flask import render_template, request, Blueprint
import repositories.designer_repository as designer_repository

designer_blueprint = Blueprint('designers', __name__)


# INDEX
# Note the blueprint name is designer, the route is designers!
@designer_blueprint.route("/designers")
def designers():
    designers = designer_repository.select_all()
    return render_template('designers/index.html',designers=designers)

# SHOW
@designer_blueprint.route("/designers/<id>")
def designer(id):
    designer = designer_repository.select(id)
    return render_template('designers/show.html', designer=designer)
