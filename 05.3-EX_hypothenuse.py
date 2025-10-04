import math

# sqrt(pow(a,2) +pow(b,2)

height = float(input("Enter the height: "))
lenght = float(input("Enter the lenght: "))
hypo = math.sqrt(pow(height,2)+pow(lenght,2))
print(f"The hpothenuse of a triangle with {height}cm height and {lenght}cm lenght, is {round(hypo, 2)}cm")
1