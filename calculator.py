def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))
    print("square root of x is", square_root(x))

def square(n):
    return n * n

def square_root(n):
    return n ** 0.5


if __name__ == "__main__":
    main()