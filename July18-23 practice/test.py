from ast import Not
from importlib import machinery
from multiprocessing.resource_sharer import stop
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

print(round(1.4))

print(not(1 != 2) == False)

spam = 1
spam += 1
print(spam)


name = 'Marry'
name2 = 'Barry'

if name == 'Marry':
    print(name)
if name2 == 'Barry':
    print(name2)
else:
    print('wrong one')



#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate 
#message to the user.

#Write a Python program to get the Fibonacci series between 0 to 50.

'''
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
'''

x = 1
y = 2
x, y = y, y+2

print(x)
print(y)

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')
while ' ':
    print (1)




