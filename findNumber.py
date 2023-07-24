import sys

numbers = [1, 3, 5, 7, 9, 0, 8]

num = int(input("Number: "))


if num in numbers:
    print("Found")
    sys.exit(0)
   
else:
    print("not found")
    sys.exit(1)

