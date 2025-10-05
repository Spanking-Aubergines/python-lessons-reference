
num1 = str(input(" Type the first number: "))
num2 = str(input(" Type the second number: "))
operator = str(input("Define the operation (+ , - , / , *)"))

if num1.isdigit():
    num1 = int(num1)
else:
    num1 = float(num1)

if num2.isdigit():
    num2 = int(num2)
else:
    num2 = float(num2)

if operator == "+":
    print(f"{num1} + {num2} = ",round((num1+num2),3))
elif operator == "-":
    print(f"{num1} - {num2} = ",round((num1-num2),3))
elif operator == "/":
    print(f"{num1} / {num2} = ",round((num1/num2),3))
elif operator == "*":
    print(f"{num1} * {num2} = ",round((num1*num2),3))
else:
    print("Choose an operation retard. (+ , - , / , *)")
