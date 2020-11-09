from flask import render_template, request, Blueprint
import repositories.designer_repository as designer_repository

designer_blueprint = Blueprint('designers', __name__)


# INDEX
# Note the blueprint name is designer, the route is designers!
@designer_blueprint.route("/designers")
def designers():
    designers = designer_repository.select_all()
    return render_template('designers/index.html',designers=designers)




# line 10 in index.html <a href='designers/{{designer.id}}'>