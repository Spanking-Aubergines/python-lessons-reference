# 2d lists

# fruit =         ["apple","orange","banana","coconut"]
# vegetables =    ["celery","carrots","potatoes",]
# meats =         ["chicken","fish","turkey"]

# groceries = [fruits, vegetables, meats]

# groceries = [["apple","orange","banana","coconut"],
#              ["celery","carrots","potatoes",],
#              ["chicken","fish","turkey"]]

# print(groceries[0][0])

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

numpad=((" 1 "," 2 "," 3 "),
        (" 4 "," 5 "," 6 "),
        (" 7 "," 8 "," 9 "),
        (" * "," 0 "," # "))

for row in numpad:
    for key in row:
        print(key, end="")
    print()