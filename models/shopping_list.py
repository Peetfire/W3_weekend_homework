from models.item import Item

item1 = Item("Butter", 1.50, 2)
item2 = Item("Cheese", 2.50, 3)
item3 = Item("Milk", 1.49, 1)
item4 = Item("Bread", 1.79, 1)
item5 = Item("eggs", 1.15, 1)
item6 = Item("Apples", 1.99, 2)

shopping_list = [item1, item2, item3, item4, item5, item6]
headings = ["Item name", "Price", "Quantity", "Bought?"]

def add_new_item(item):
    shopping_list.append(item)

def remove_item_by_name(name):
    for item in shopping_list:
        if item.item_name == name:
            shopping_list.remove(item)

def set_item_bought(name, status):
    for item in shopping_list:
        if item.item_name == name:
            item.bought = status

def get_total_price(item_list):
    return sum([item.price * item.quantity for item in item_list])

def get_total_items(item_list):
    return sum([item.quantity for item in item_list])

def get_total_bought(item_list):
    return sum([item.quantity for item in item_list if item.bought])

total_price = get_total_price(shopping_list)
total_items = get_total_items(shopping_list)
total_bought = get_total_bought(shopping_list)
grand_totals = [total_price, total_items, total_bought]

def set_totals():
    total_price = get_total_price(shopping_list)
    total_items = get_total_items(shopping_list)
    total_bought = get_total_bought(shopping_list)
    grand_totals.clear()
    grand_totals.append(total_price)
    grand_totals.append(total_items)
    grand_totals.append(total_bought)

