customer = {
    'first_name': 'John',
    'last_name': 'Smith',
    'email': 'john@asu.edu',
    'age': 22,
    'is_verified': True
}
print(customer["first_name"])
print(customer["last_name"])
print(customer.get('birthdate','Jan 1 1990'))
customer['first_name'] = 'Jack'
print(customer['first_name'])
