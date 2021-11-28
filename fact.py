def fact(n):
    return 1 if n in [0, 1] else n * fact(n - 1)

if __name__ == "__main__":
    for i in range(10):
        print(fact(i))
    