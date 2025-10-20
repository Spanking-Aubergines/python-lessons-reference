
# note the need to use "global var" for the global var to be used inside a funtion

balance = 1000


def show_balance():
    print(f"Your account has {balance}€")
    print()

def deposit():
    global balance
    dep = float(input("How much would you like to deposit: "))
    balance = balance + dep
    print (f"Your balance is now {balance}.\n")

def withdraw():
    global balance
    amount = float(input("How much would you like to withdraw: "))
    if amount > balance:
        print(f"The amount {amount} is higher than the available balance")
    elif amount == 0:
            print(f"No amount was withdrawn.")
    else:
        balance = balance - amount
        print(f"Withdrawn {amount}.")
        print (f"Your balance is now {balance}.\n")

def main():
    while True:
        print("**********MEGA-BANK**********\n",
                "1: Show balance\n",
                "2: Deposit\n",
                "3: Withdraw\n",
                "Q: Quit\n")

        op = input("Choose an option: ")
        match op:
            case "1" | "S" | "s":
                show_balance()
            case "2" | "D" | "d":
                deposit()
            case "3" | "W" | "w":
                withdraw()
            case "q" | "Q":
                print("Goodbye!")
                break
            case _:
                print("Invalid option")

if __name__ == '__main__':
    main()