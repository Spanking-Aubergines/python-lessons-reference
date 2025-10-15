# *args       = allows to pass multiple non-key arguments  ---> pac into a tuple
# **kwargs    = allow to pass multiple keyword-arguments    -->pack into a dictionary
#             * unpacking operator

# def add(a, b):
#     return a+b

# print(add(1, 2))

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg:
#     return total

# print(add(1, 2,3,4,5,6))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Alberto","machado,Assis")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} ; {value}")

print_address(street="123 street",
              city="Helsinky",
              country="Phoenicia",
              zip="31233-322",
              apt="100")