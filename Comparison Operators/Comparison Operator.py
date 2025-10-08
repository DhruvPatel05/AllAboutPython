temperature = 35

# Assignment operator = , Comparison operator == != > <

if temperature > 30:
    print("It's a Hot day")
else:
    print("It's not a Hot day")

name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")
