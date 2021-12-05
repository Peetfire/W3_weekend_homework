from app import app
from flask import render_template, request, redirect
from models.shopping_list import *
from models.item import Item

@app.route('/shopping-list')
def index():
    return render_template('index.html', title="Home", shopping_list=shopping_list, headings=headings)

@app.route('/shopping-list', methods=['POST'])
def add_task():
    item_name = request.form["item_name"]
    price = request.form["price"]
    quantity = request.form["quantity"]
    new_item = Item(item_name, price, quantity)
    add_new_item(new_item)
    request.close()
    return redirect('/shopping-list')