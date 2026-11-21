import random


def generate_otp():
    return random.randint(100000, 999999)


otp = generate_otp()
print("Generated OTP:", otp)
entered = int(input("Enter OTP: "))

if entered == otp:
    print("OTP verified successfully")
else:
    print("Invalid OTP")
