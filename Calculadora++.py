
num1 = float(input("Enter a number: "))
op = input("Enter opeator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "x":
    print(num1 * num2)
elif op == "/":
    while (num2 == 0):
        num2 = float(input("Enter a valid second number: "))
    print(num1 / num2)

else:
    print("Elefante")