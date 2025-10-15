import random

minimum = 1
maximum = 100
number  = random.randint(minimum,maximum)

while True:
    guess = int(input("Guess a number between 1 and 100"))

    if guess < minimum or guess > maximum:
        print("Number is out of range, try again")
    elif guess > number:
        print("too high, try again")
    elif guess < number:
        print("too low, try again")
    else:
       print(f"correct, the number was {number}")
       break