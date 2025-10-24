import random

for i in range(5):
    print(random.random())
    print(random.randint(3,10))
member = ['John','david','Bob','Joe']
leader = random.choice(member)
print(leader)