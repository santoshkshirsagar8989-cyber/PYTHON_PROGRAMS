#for canteen order project
print ("Welcome to our canteen! Here is our menu:")
menu = {"Pizza", "Burger", "Pasta", "Salad", "Soda"}
prizes = {"Pizza": 199, "Burger": 80, "Pasta": 120, "Salad": 16, "Soda": 20}
print(menu)
print(prizes)
order = input ("enter item you want to order: ")
if order in menu:
    print("Your order is: ", order)
    print("The price of your order is: ", prizes[order])