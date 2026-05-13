k = input("Enter something: ")

if k.isdigit():
    print("The input is a Number.")
elif k.isalpha() and len(k) == 1:
    print("The input is a Character.")
else:
    print("The input is a String or Special Character.")
