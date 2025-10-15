# function = block of reusable code
                # place () after the function


# the args received must be in order of use
# def happy_birthday(name, age):
#     print(f"happy birthday to {name}")
#     print(f"you are {age} old")
#     print("happy birthday")
#     print()

# # happy_birthday()
# # happy_birthday()

# # the sent args must be in order of use
# happy_birthday("Joe",30)
# happy_birthday("Steve",40)

# reutrn = used to end a function
            # sends result back to the caller

# def add(x,y):
#     z = x + y
#     return z

# print(add(1,2))

def create_name (first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name =  create_name("spanking","aubergine")

print(full_name)