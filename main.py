import random

otp = random.randint(100000, 999999)
print("Your OTP is:", otp)

user_input = input("Enter the OTP: ").strip()

if user_input == str(otp):
    print("OTP verified successfully!")
else:
    print("Incorrect OTP.")
