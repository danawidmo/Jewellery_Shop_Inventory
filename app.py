from flask import Flask, render_template

from controllers.designer_controller import designer_blueprint
from controllers.product_controller import product_blueprint

import repositories.product_repository as product_repository
import repositories.designer_repository as designer_repository


app = Flask(__name__)

app.register_blueprint(designer_blueprint)
app.register_blueprint(product_blueprint)


@app.route('/', methods=['GET', 'POST'])
def home():
    products = product_repository.select_all()
    designers = designer_repository.select_all()
    return render_template('index.html',products=products, designers=designers)

if __name__ == '__main__':
    app.run(debug=True)