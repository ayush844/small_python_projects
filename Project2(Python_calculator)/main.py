# Python calculator


operator = input("Enter an operator (+ - * /)")

num1 = float(input("Enter 1rst number"))
num2 = float(input("Enter 2rst number"))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print("wrong operator")