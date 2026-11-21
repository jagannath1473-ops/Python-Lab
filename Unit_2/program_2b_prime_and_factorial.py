n = int(input("Enter a number: "))

# Prime check
prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break
print(n, "is prime" if prime else "is not prime")

# Factorial
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial =", factorial)
