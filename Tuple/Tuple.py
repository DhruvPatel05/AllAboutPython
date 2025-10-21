number = (1,2,3,4)
print(number[0])
# number[0] = 10
# we can not modify the tuple
coordinates = (1,2,3)
value = coordinates[0] * coordinates[1] * coordinates[2]
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
value1 = x*y*z
print(value1)
# unpacking
a,b,c = coordinates
value2 = a*b*c
print(value2)
