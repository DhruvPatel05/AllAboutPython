try:
    Age = int(input("Enter your Age: "))
    income = 200000
    risk = income/Age
    print(Age)
except ZeroDivisionError:
    print("Age can not be zero.")
except ValueError:
    print("You didn't enter a number.")

