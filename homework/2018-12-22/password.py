import re
password = input("Enter you password: ")
if re.match(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&+=;*])[A-Za-z0-9@#$%^&+=;*]{8,}', password):
    print("Valid password")
else:
    print("Password not valid")