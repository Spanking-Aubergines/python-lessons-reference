

foods = []
prices = []
quants = []
total = 0

while True:
    food = str(input ("Enter a food to buy (q to quit): "))
    if food.upper() == "Q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: €"))
        quant = int(input(f"Enter the amount of a {food}:"))
        foods.append(food)
        prices.append(price)
        quants.append(quant)

print("-------YOUR CART-------")
for idx in range (len(foods)):
    print(f"{quants[idx]:>}   {foods[idx]:<}   {prices[idx]:^}")
    total = total + (prices[idx] * quants[idx])

print("")
print(f"Total = {total}")