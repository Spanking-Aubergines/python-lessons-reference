
# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))


# while name == "":
#     print("You did not enter your name")
#     name = str(input("Enter your name: "))
# else:
#     print(f"Your name is {name}")

# while age < 0:
#     print("You did not enter your age")
#     age = int(input("Enter your age"))
# else:
#     print(f"Your are {age} years old")


# food = str(input("Enter a food you like (q to quit): "))

# while not food=="q":
#     print(f"You like {food}")
#     food = str(input("Enter another food you like (q to quit): "))

# print("Bye")

num = float(input("Enter a number between 1 and 10 (q to quit): "))

while num < 0 or num >10:
    print(f"{num} is not valid")
    num = float(input("Enter a number between 1 and 10 (q to quit): "))

print(f"Your number is {num}")