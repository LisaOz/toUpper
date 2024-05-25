
A = []
while True:
    x = input()
    if x == "":
        break
    A.append(x)

n = len(A)
print("the list's length is", n)
x = A.pop()
print(len(A))


def matryoshka(n):

    if n == 1:
        print("Matryoshechka")
    else:
        print("Verh n=", n)
        matryoshka(n-1)
        print("niz n=", n)

n = int(input("Number: "))
matryoshka(n)