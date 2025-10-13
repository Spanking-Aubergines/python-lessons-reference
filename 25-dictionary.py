# dictionary =  a collection of {key:value} pairs
                # ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(capitals.get("USA"))
# if a key is not present returns"none"
# this can be interacted

# if capitals.get("Russia"):
#     print("Capital exists")
# else:
#     print("capital doesnt exist")

# capitals.update({"Germany":"Berlin"}) # diff key and value - add to dictionary

# capitals.update({"USA":"Detroit"}) # existing key - change value

# capitals.pop("China") #remove key:value from list

# capitals.popitem() #removes last key

# capitals.clear()

# keys = capitals.keys() # prints only keys being keys an object like a collection

# for key in capitals.keys()
#     print(keys)

# values = capitals.values() # works the same way than .keys()
# for value in capitals.values():
#     print(value)

# returns an objec like a 2d tuple 
# items = capitals.items()
# for key, value in capitals.items():
    # print(f"{key}: {value}")