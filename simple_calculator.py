
try:
    x = int(input("x: "))


    y = int(input("y: "))
except ValueError:
    print("Enter valid integer")
    exit()

operator = input("operator is: ")


if operator == "+":
    print ("Result is ", (x + y))
elif operator == "-":
    print ("Result is ", (x - y))
elif operator == "*":
    print ("Result is ", (x * y))
elif operator == "/":
    print ("Result is ", (x / y))
else:
    print("Invalid operator")