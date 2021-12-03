from app import app
from flask import render_template, request
from models.shopping_list import *
from models.item import Item

@app.route('/shopping-list')
def index():
    return render_template('index.html', title="Home", shopping_list=shopping_list, headings=headings)