# indexing: accessing elements of a strin. start position is 0
# start inculsive, end exclusive
# [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])

# intervalos
# print(credit_number[0:4])
# print(credit_number[5:9])

# from index to end
# print(credit_number[5:])

# revert index
# print(credit_number[-1])

# in steps, every second character
# print(credit_number[::2])

last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")