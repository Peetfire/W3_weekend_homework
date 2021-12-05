from app import app
from flask import render_template, request, redirect
from models.shopping_list import *
from models.item import Item

@app.route('/shopping-list')
def index():
    return render_template('index.html', shopping_list=shopping_list, headings=headings, grand_totals=grand_totals)

@app.route('/shopping-list', methods=['POST'])
def add_task():
    item_name = request.form["item_name"]
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])
    new_item = Item(item_name, price, quantity)
    add_new_item(new_item)
    set_totals()
    return redirect('/shopping-list')

@app.route('/shopping-list/bought')
def bought():
    bought_list = get_bought_list(True)
    bought_price = get_total_price(bought_list)
    bought_items = get_total_items(bought_list)
    bought = get_total_bought(bought_list)
    bought_totals = [bought_price, bought_items, bought]
    return render_template('index.html', shopping_list=bought_list, headings=headings, grand_totals=bought_totals)

@app.route('/shopping-list/to-buy')
def to_buy():
    to_buy_list = get_bought_list(False)
    to_buy_price = get_total_price(to_buy_list)
    to_buy_items = get_total_items(to_buy_list)
    to_buy = get_total_bought(to_buy_list)
    bought_totals = [to_buy_price, to_buy_items, to_buy]
    return render_template('index.html', shopping_list=to_buy_list, headings=headings, grand_totals=bought_totals)    

@app.route('/shopping-list/bought', methods=['POST'])
def set_bought():
    item = request.form['bought_button']
    set_item_bought(item, True)
    set_totals()
    return redirect('/shopping-list')

@app.route('/shopping-list/uncheck', methods=['POST'])
def set_not_bought():
    item = request.form['bought_button']
    set_item_bought(item, False)
    set_totals()
    return redirect('/shopping-list')
    
@app.route('/shopping-list/delete', methods=['POST'])
def delete_item():
    item = request.form['delete_button']
    remove_item_by_name(item)
    set_totals()
    return redirect('/shopping-list')
    