operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    print(round(num1 + num2, 3))
elif operator == "-":
    print(round(num1 - num2, 3))
elif operator == "*":
    print(round(num1*num2, 3))
elif operator == "/":
    print(round(num1 / num2, 3))
else:
    print("operator is not supported!!!")