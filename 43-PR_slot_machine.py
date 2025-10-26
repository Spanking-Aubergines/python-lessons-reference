import random 


def roller(creds, session_creds, current_bet):

    icon_list = ["J", "Q", "K", "A", "JK"]
    icons = []
    
    for x in range (0,3):
        icons.append(random.choice(icon_list))

    if session_creds is None:
        session_creds = 0
        
    if int(current_bet) > session_creds:
        creds -= abs(session_creds - current_bet)
    elif current_bet <= float(session_creds):
        session_creds -= current_bet

    combination = tuple(icons)
    return combination, creds, session_creds

def check_calc_prize(combination, creds, session_creds, current_bet):
    combo_list = {("J","J","J"):1,
                  ("Q","Q","Q"):1.25,
                  ("K","K","K"):1.50,
                  ("A","A","A"):1.75,
                  ("JK","JK","JK"):2}

    if session_creds is None:
        session_creds = 0
            
    multiplier = combo_list.get(combination)

    if multiplier:
        session_creds += float(current_bet * multiplier)
   
    return session_creds



def add_credits(creds):

    amount_add = input("How many credits would you like to add: ")
    print("")
 
    
    if amount_add.isdigit():
        cred_add = int(amount_add)
        if cred_add > 0 :
            creds += cred_add
        else:
            print("\nInser a valid amount\n")

    return creds

def set_bet(current_bet):   
                                                                                                       
    while bet_pos_check == True:
        bet_amount = int(input("Set your bet value: "))
        if bet_amount <= 0:
            print("Bet can'r be less or equal to 0")
        else:
            return bet_amount


def cashout(creds, session_creds):
    creds = float(creds + session_creds)
    print(f"\nYou cashed out {session_creds}.\n",
          f"Now have a total of {creds} credits.")
    session_creds = 0
 
    return creds, session_creds

def main():
    creds = 1000
    session_creds = 0
    current_bet = 10
    combination = ()


    while True:
        print("**********Slot Machine**********\n",
                 "\n",
                f"Available credits : {creds}\n",
                f"   Earned Credits : {session_creds}\n",
                f"      Current bet : {current_bet}\n",

                f"\n        Last Spin : {combination}\n",

                 "\n",
                 "1: Spin\n",
                 "2: Set Bet\n",
                 "3: Add Credits\n",
                 "4: Cashout\n",
                 "5: Quit\n",
                 "\n")
        op = input("Choose an option: (1, 2, 3, 4, 5)  ")
        match str(op):
            case "1":
                if creds <= 0:
                    print("Not enough credits, please add more credits to play")
                    creds = add_credits(creds)
               
                elif current_bet == 0:
                    print("Set a betting value first")
                    current_bet= set_bet(current_bet)
               
                else:
                    combination, creds, session_creds = roller(creds, session_creds, current_bet)
                    session_creds = check_calc_prize(combination, creds, session_creds, current_bet) or session_creds

            case "2":
                current_bet= set_bet(current_bet)

            case "3":
                creds = add_credits(creds)
            case "4":
                creds, session_creds = cashout(creds, session_creds)
            case "5":
                break
            case _:
                print("Invalid option")

if __name__ == '__main__':
    main()