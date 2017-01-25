from flask import render_template, Blueprint, abort
from jinja2 import TemplateNotFound
from websocket_io import app

default_view = Blueprint('index', __name__)

@app.route('/', defaults = {'page': 'index'})
@app.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
