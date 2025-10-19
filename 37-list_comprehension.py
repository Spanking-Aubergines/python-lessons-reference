# list comprehension = a concise way to create lists in Python
#                     compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]


# doubles = []

# for x in range (1,11):
#     doubles.append(x * 2)

# print(doubles)

# doubles = [x *2 for x in range(1,11)]

# print(doubles)

# triples = [x *3 for x in range(1,11)]

# print(triples)

# squares = [x * x for x in range(1,11)]

# print(squares)

# fruits = ["apple","orange","banana","coconut"]
# # fruits = [fruit.upper() for fruit in fruits]

# # fruits = [fruit.upper() for fruit in ["apple","orange","banana","coconut"]]

# fruits_chars = [fruit[0] for fruit in fruits]

# print (fruits_chars)

# numbers = [1 ,-2, 3, -4, 5, -6]
# positive_numbers = [num for num in numbers if num >= 0]
# negative_numbers = [num for num in numbers if num < 0]
# even_numbers = [num for num in numbers if num % 2 == 0]
# odd_numbers = [num for num in numbers if num % 2 == 1]

# print(positive_numbers)
# print(negative_numbers)
# print(odd_numbers)
# print(even_numbers)

grades = [85, 42,79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)