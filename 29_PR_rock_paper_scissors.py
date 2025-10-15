import random

choices = ["r","p","s"]


while True:
    
    guess = str(input("Choose Rock, Paper or Scissors (r, p, s | q to quit)"))
    choice = random.choice(choices)
    if guess == "q":
        break
    elif guess == choice:
        print("draw")
        choice = random.choice(choices)
    elif guess == "r" and choice == "s" :
        print("win")
    elif guess == "p" and choice == "r":
        print("win")
    elif guess == "s" and choice == "p":
        print("win")
    else:
       print(f"loose")