# collection = single variable used to store multiple values
    # List = []  ordered and changeable. Duplicates OK
    # set  = {}  unordered and immutable. Add/Remove OK. NO duplicates
    # Tuple = () ordered, unchageable, duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits)

fruits = ["apple", "orange", "banana", "coconut"]

# list methods
# print (dir(fruits))
# print (help(fruits))

# print (fruits[0])
# print (fruits[:3])
# print (fruits[::2])
# print (fruits[::-1])

# fruits[0] = "pinapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruit.reverse() reverses in insertion order for reverse alphabetical order first sort
# fruits.clear()
# print (index("apple"))

for x in fruits:
    print(x)