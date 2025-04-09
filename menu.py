import utils.session
menu ={
    'pizza':40,
    'burger':50,
    'pasta':60,
    'salad':70,
    'coffee':80,
}


print("welcome to python restarynt")
print("pizza: Rs4\npasta: Rs50\n Burger:Rs60\nsalad:Rs70\ncoffee:Rs80")

order_total = 0

while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {order_total} Rs")
