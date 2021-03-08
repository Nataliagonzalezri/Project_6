import random

a = [1,2,3]
a.append(7)
print(a)
a.remove(3)
print(a)
a.pop(1)
#pop takes out by position. Remove removes the value (when I know the value)
print(a)

# here we add an empty list, to "clean" "a".
a = []
for element in range(1,10):
    a.append(random.randint(1,100))
print(a)

del a[::2]
print(a)

while a:
    print(a.pop(0))
