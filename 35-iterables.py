# iterable =  an object/collection than canr eturn its elements one at a time,
#             allowing it to be iterated over in a loop


# numbers = [1,2,3,4,5]
# numbers = (1,2,3,4,5)

# for number in numbers:
#     print(number)

my_dictionary = {"A":1, "B": 2, "C": 3}

# for key in my_dictionary:
#     print(key)

# for value in my_dictionary.values():
#     print(value)

for key, value in my_dictionary.items():
    print(key, value)

# for number in reversed(numbers):
#     print(number, end="") 