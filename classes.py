'''
Houses all classes for online store.
'''
import os

# name of product, price, description for Item
class Item:
    def __init__(self, name, price, description=None):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'This is item: {self.name}, it costs ${self.price}, and description: {self.description}'


class Customer:
    def __init__(self, name,  email, card_number=None, eye_color=None, age=None, dob=None):
        self.name = name
        self.card_number = card_number
        self.email = email
        self.eye_color = eye_color
        self.age = age
        self.dob = dob
        self.shopping_cart = []

    '''
    Add item to cart
    Remove item from cart
    Clear the entire cart
    Get total for cart
    '''
    def add_item_to_cart(self, item):
        self.shopping_cart.append(item)

    def remove_item_from_cart(self, item_name):
        for item in self.shopping_cart:
            # if item's name inside shopping cart is equal to the item name given by user: delete
            if item.name == item_name:
                self.shopping_cart.remove(item)

    def get_total(self):
        total = 0
        for item in self.shopping_cart:
            # for every item in shopping cart, add their price to total
            total += item.price
        return total

    def __str__(self):
        return f'Customer name is {self.name}!'

class Store:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    
    def remove_item_from_inventory(self, item):
        self.inventory.remove(item)

    def __str__(self):
        return f'Store name is {self.name}!'