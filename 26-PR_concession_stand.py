# concession stand program

menu={"pizza": 3.00,
      "nachos": 4.50,
      "popcorn": 6.00,
      "fries": 2.50,
      "chips": 1.00,
      "pretzel": 3.50,
      "soda": 3.00,
      "lemonade":4.25}

cart = []
quant = []
total = 0


print("------------MENU------------")
for key, value in menu.items():
    print(f"{key.capitalize():10}   :   {value:.2f}€")
print("------------////------------")

while True:
    food= str(input("What food do you want? (C - Checkout | Q - Quit)"))
    food = food.lower()
    if food.upper()== "C":
        print("") 
        print("----------CHECKOUT---------")
        for item in cart:
            inx = cart.index(item)
            print(f"{item.capitalize():10}   :   {quant[inx]}")
            total += menu.get(item)
        print("")     
        print(f"TOTAL:     {total:.2f}")
    elif food.upper()== "Q":
        break
    elif menu.get(food) is None:
        print("")
        print(f"{food.capitalize()} is not available on the list. Choose from the list below")
        print("") 
        print("------------MENU------------")
        for key, value in menu.items():
            print(f"{key.capitalize():10}   :   {value:.2f}€")
        print("------------////------------")
        print("")
    elif menu.get(food) is not None:
        quantity = int(input(f"You chose {food}, how many would you like?:   ").lower())
        cart.append(food)
        quant.append(quantity)
        print("") 
        print("------------MENU------------")
        for key, value in menu.items():
            print(f"{key.capitalize():10}   :   {value:.2f}€")
        print("")     
        print("------------CART------------")
        for item in cart:
            inx = cart.index(item)
            print(f"{item.capitalize():10}   :   {quant[inx]}")
            # total += menu.get(item)

        

    

#     total = total + menu.get(value ) * quant[item]
#     print("")

#     print("")
#     print("")
#     print ("")        