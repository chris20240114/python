from operator import indexOf
from os import remove
from typing import Dict


print(7/2)

print(7//2)

print(7**3)

Chris = "Chris"
print(Chris)

print(Chris.lower())

Chris+=('topher')
print(Chris)

Chris=Chris.replace("er", "e/")
print(Chris)

x=[1, 'ex', 3.82]
x.append(x[0]+x[2])
print(x)

for i in x:
    if isinstance(i, str):
        x.remove(i)

print(x)

Dict = {}
for i in range(len(x)):
    pair = {i:x[i]}
    Dict.update(pair)

print(Dict)

Dict.pop(2)
print(Dict)

x.clear()
print(x)

for i in range(61,85):
    if i%2 != 0:
        x.append(i)
print(x)

x.clear()

for i in range(61, 85, 2):
    x.append(i)

print(x)

#hi

print('''''')