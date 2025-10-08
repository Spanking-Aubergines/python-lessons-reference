# for loops = execute a block of code a fixed number of times
#               You can iterate over a range, string, sequence, etc.

# for x in range (1, 11):
#     print(x)

# for x in reversed(range (1, 11, 2)):
#     print(x)

# for x in reversed(range (1, 11, 3)):
#     print(x)

# wordspell = "example"

# for x in wordspell:
#     print(x)


# for x in range(1, 12):
#     if x == 13:
#         continue
#     else:
#         print(x)


for x in range(1, 12):
    if x == 13:
        break
    else:
        print(x)
