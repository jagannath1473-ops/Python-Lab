a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
if b == 0:
    print("Division and remainder are undefined for zero")
else:
    print("Division =", a / b)
    print("Remainder =", a % b)
