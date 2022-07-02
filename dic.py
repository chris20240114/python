'''
This is about dictionary
'''



# empty dictionary
dic1 = {}
dic1 = dict()

# assign values
dic1 = {1:'a', 2: 'b', 'name': 'alphabet'}
print(dic1)
dic1[1] = 'f'
print(dic1)

# get the keys in a list
print(dic1.keys())



# get values in a list
print(dic1.values())


# get each individual pairs as tuple
print(dic1.items())


# checking if key or value is in dic
if 2 in dic1.keys():
    print('dic1 has a key 2')
if 1 in dic1:
    print('dic1 has a key 1')
if 'f' in dic1:
    print('dic1 has a key 1')
else:
    print('dic1 does not have key \'f\'')


if 'b' in dic1.values():
    print('dic1 has a value \'b\'')

# using get() to check if a key exists before accessing it
if dic1.get(2, 0):
    print('dic1 has a key 2')

#dic1[9] = 'ppop'
if dic1.get(9, 0):
    print('dic1 has key 9 with value ' +  dic1.get(9,0))
else:
    print('dic1 does not have a key 9')


# add new key-value pair to the dic
dic1.setdefault('color', 'crimson')
print(dic1)
dic1[4] = 'd'
print(dic1)


# accessing element
print(dic1['name'])
print(dic1['color'])

# removing element
print(dic1)
# pop() will remove key value pair with the given key
# pop() will return the value
print(dic1.pop(2))
# popitem() removes the first one in the dict
# popitem() will return the tuple
print(dic1.popitem())
print(dic1)

dic1.clear()



