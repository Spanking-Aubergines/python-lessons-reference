
item = input("what item was chosen?: ")
quantity = int(input("how many?: "))
price = float(input("price per unit?: "))

print(f"{quantity} item chosen: {item} = Total ",(quantity * price),"€")