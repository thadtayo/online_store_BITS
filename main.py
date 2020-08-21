from classes import Item, Customer, Store

# create Items for store
coke = Item('Coke', 2)
tv = Item('TV', 500)
hot_cheetos = Item('Hot Cheetos', 3)
chips = Item('Chips', 2)
pull_up_bar = Item('Pull Up Bar', 120)

# create an inventory for a particular store
li = []
# append all items
li.append(coke)
li.append(tv)
li.append(hot_cheetos)
li.append(chips)
li.append(pull_up_bar)

dora_store = Store('Dora', li)

# user interaction
customer_name = input('What is your name? ')
customer_email = input('What is your email? ')
customer = Customer(customer_name, customer_email)
yes_no = input('Would you like to input your credit card number now so you do not have to during checkout? (y/n)')
if yes_no == 'y':
    customer_credit_card_number = input('Enter credit card number here: ')
    customer.card_number = customer_credit_card_number


# Allow customers to add items to the cart (by name of item)

while True:
    # show customer all items the store has to offer
    print('Hey! Here is our selection of products by Dora!')
    for item in dora_store.inventory:
        print(item)

    # allow customers to add to cart

    potential_purchase_name = input('Type the name of the product you wish to put in your cart!')
    '''
    Want to do two things:
    - add this item to cart
    - remove item from inventory
    '''

    # check to see if a potential_purchase_name == any of the items' names
    found = False
    for item in dora_store.inventory:
        # if we found a match, add to shopping cart, remove from inventory
        if potential_purchase_name.lower() == item.name.lower():
            found = True
            # add to cart
            customer.add_item_to_cart(item)
            # remove item from inventory
            dora_store.remove_item_from_inventory(item)

    if not found:
        print('Not a valid item name!')

    print(customer.shopping_cart)

    validation = input('Do you want to keep shopping? (y/n)')
    if validation == 'n':
        break


print('You are now being directed to checkout...')

# Tell customer their total
total = customer.get_total()
print(f'Your total is ${total}.')

if customer.card_number == None:
    customer.card_number = input('Our system has detected you do not have a credit card. Please input your credit card number in order to checkout: ')

'''
At this point you process the payment and ship out the product... But we won't do that for this boot camp :) 

'''
print(f'You are all set! Thanks for shopping at {dora_store.name}')