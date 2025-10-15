import random

# print unicode special chars
# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"# "│         │"# "│    ●    │"# "│         │"# "└─────────┘"
# "┌─────────┐"# "│    ●    │"# "│         │"# "│    ●    │"# "└─────────┘"
# "┌─────────┐"# "│    ●    │"# "│    ●    │"# "│    ●    │"# "└─────────┘"
# "┌─────────┐"# "│  ●   ●  │"# "│         │"# "│  ●   ●  │"# "└─────────┘"
# "┌─────────┐"# "│  ●   ●  │"# "│    ●    │"# "│  ●   ●  │"# "└─────────┘"
# "┌─────────┐"# "│ ●     ● │"# "│ ●     ● │"# "│ ●     ● │"# "└─────────┘"

dice_art = {1:( "┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),
            2:( "┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),
            3:( "┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4:( "┌─────────┐",
                "│  ●   ●  │",  
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5:( "┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6:( "┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘" )}

num_dice = int(input("How many die do you wish to roll?:  "))
list_roll = []
total = 0

for die in range(num_dice):
    list_roll.append(random.randint(1,6))
    total += list_roll[die]
   
# for die in range(num_dice):
#     for line in dice_art.get(list_roll[die]):
#         print(line)

for line in range (5):
    for die in list_roll:
        print(dice_art.get(die)[line],end="")
    print()


print(f"The total is {total}")