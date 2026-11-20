terms = int(input("Enter number of terms: "))

if terms < 0:
    print("Number of terms cannot be negative")
else:
    first, second = 0, 1
    print("Fibonacci series:")
    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second
    print()
