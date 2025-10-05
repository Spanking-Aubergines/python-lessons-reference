# validade user input
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = str(input("Type your username: "))

if len(username) > 12:
    print(f"The {username} is invalid")
elif not username.find(" ")== -1:
    print(f"The {username} is invalid")
elif not username.isalpha():
    print(f"the {username} is invalid")
else:
    print(f"The {username} is valid")