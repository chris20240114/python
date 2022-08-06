import random
import os

print("Select a random element from a list:")
List1 = [1, 2, 3, 4, 5]
print(random.choice(List1))
print(random.choice(List1))
print(random.choice(List1))

print("Select a random element from a set:")
Set = set([1, 2, 3, 4, 5])
print(random.choice(tuple(Set)))
print(random.choice(tuple(Set)))
print(random.choice(tuple(Set)))

print("Select a random value from a dictionary:")
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
key = random.choice(list(dictionary))
print(dictionary[key])
key = random.choice(list(dictionary))
print(dictionary[key])
key = random.choice(list(dictionary))
print(dictionary[key]) 