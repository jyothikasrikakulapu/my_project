operation=input("Enter operation: ")
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("NO operations performed")