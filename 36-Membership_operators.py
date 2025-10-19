# membership operators = used to test wgeter a value or varuable is found in a sequence
#                         (string, list, tuple, set or dictionary)
                        # return a boolean
#                         1. in
#                         2. not in

# word = "apple"

# letter = str(input("Guess a lettr in a secret word: "))

# if letter.lower() in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# students = {"spongebob","patrick","sandy"}

# student =  str(input("Enter the name of a student: "))

# if student in students:
#     print(f"{student} is present on the student list")
# else:
#     print(f"{student} is not present on the student list")

# grades = {"sandy": "a",
#          "spongebob": "c",
#          "patrick": "d"}

# student =  str(input("Enter the name of a student: "))

# if student in grades:
#     print(f"{student}'s grande is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "email@emaildomain.com"

if "@" in email and "." in email:
    print("It is a valid email")
else:
    print("Invalid email")
    