print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/): ")

if operator == "+":
    print("Result =", a + b)
elif operator == "-":
    print("Result =", a - b)
elif operator == "*":
    print("Result =", a * b)
elif operator == "/":
    print("Cannot divide by zero" if b == 0 else f"Result = {a / b}")
else:
    print("Invalid operator")

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
if length < 0 or breadth < 0:
    print("Rectangle dimensions cannot be negative")
else:
    print("Area of rectangle =", length * breadth)
