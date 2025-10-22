def greet_user():
    print("Hi there!")
    print("Welcome aboard")
print("Starting function")
greet_user()
print("Ending function")

def introduce_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print("Welcome on flight")


introduce_user("James","smith")
introduce_user(last_name="patel",first_name="Dhruv")

def square(number):
    # return number * number
    print(number*number)
print(square(10))
