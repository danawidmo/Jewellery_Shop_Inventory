from flask import render_template, request, Blueprint


designer_blueprint = Blueprint('designer', __name__)


# line 10 in index.html <a href='designers/{{designer.id}}'>