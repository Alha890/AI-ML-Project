password = input("Enter password: ")
has_letter = False
has_number = False
for ch in password:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_number = True
if len(password) >= 8 and has_letter and has_number:
    print("Valid Password")
else:
    print("Invalid Password")