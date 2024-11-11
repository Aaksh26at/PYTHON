menu = {
       "pizza" : 50,
       "pasta" : 60,
       "Burger" : 70,
       "Salad" : 80
}

print("Welcome to python Resturnat")
print("pizza: Rs40\npasta: Rs50\nBurger: Rs70\nSalad: Rs80")

order_total = 0
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
       order_total+=menu[item_1]
       print(f"Your item {item_1} has been added to the order")
else:
       print(f"The item {item_1} is not avaiable in the menu")
       

print(f"The order total is {order_total}")