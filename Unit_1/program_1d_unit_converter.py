print("UNIT CONVERTER")
print("1. Kilometres to Metres")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter choice: "))

if choice == 1:
    kilometres = float(input("Enter kilometres: "))
    print("Metres =", kilometres * 1000)
elif choice == 2:
    celsius = float(input("Enter Celsius: "))
    print("Fahrenheit =", (celsius * 9 / 5) + 32)
else:
    print("Invalid choice")
