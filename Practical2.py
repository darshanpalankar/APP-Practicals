import re

print("Performed By 42 & 47")
def valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern,email))

def phone_number(no):
    pattern = r"^\d{10}$"
    return bool(re.match(pattern,no))

def password(pass1):
    pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
    return bool(re.match(pattern,pass1))

mail = input("Enter the email : ")
number = input("Enter the number : ")
pass1 = input("Enter a password :")

if valid_email(mail):
    print("\nvalid Email ID")
else:
    print("\nEnter Valid Email ID")
  
if phone_number(number):
    print("\nvalid Phone Number")
else:
    print("\nEnter Valid Phone Number")

if password(pass1):
    print("\nvalid Password")
else:
    print("\nEnter Valid Password")