from flask import Flask, render_template
from routes.operaciones_bp import *

import os

app = Flask(__name__)
app._static_folder = os.path.abspath("templates/static/")


app.register_blueprint(operaciones_bp, url_prefix='/operaciones')


@app.route('/')
def index():
    return render_template('layouts/index.html')


if __name__ == '__main__':
    # app.debug = True
    app.run()
