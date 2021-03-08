import random


# in this case "for" is easier, because we know the numbers we want to obtain
for val in range(0,10):
    print(random.randint(1,10))

sum = 0
for val in range(0,10):
    sum = sum + random.randint(1,10)

print(f"the sum of 10 random numbers is {sum}")







