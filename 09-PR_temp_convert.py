# wheight converter


unit = str(input("Chose the conversion: 1-(c-f) 2-(f-c)"))
temp= float(input("Type the tmep: "))


if unit == "1":
    print(f"{temp}C is ",round(((9*temp)/5+32),2),"F")
elif unit == "2":
    print(f"{temp}F is ",round(((tepm-32)*5/9),2),"C")
