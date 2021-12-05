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

def set_item_bought(name):
    for item in shopping_list:
        if item.item_name == name:
            item.bought = True

def get_total_price():
    return sum([item.price * item.quantity for item in shopping_list])

def get_total_items():
    return sum([item.quantity for item in shopping_list])

def get_total_bought():
    return sum([item.quantity for item in shopping_list if item.bought])

set_item_bought("Butter")
total_price = get_total_price()
total_items = get_total_items()
total_bought = get_total_bought()
totals = [total_price, total_items, total_bought]

