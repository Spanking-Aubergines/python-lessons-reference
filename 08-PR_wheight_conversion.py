# wheight converter


unit = str(input("Chose the conversion: 1-(kg-lbs) 2-(lbs-kg)"))
weight= float(input("Type the weight: "))


if unit == "1":
    print(f"{weight}Kg is ",round((weight*2.205),2),"Lbs")
elif unit == "2":
    print(f"{weight}Lbs is ",round((weight/2.205),2),"Kg")
