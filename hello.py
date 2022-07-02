import sys

print("hello world")


for i in range(8):
    print(i)


list0 = [1, 2, 3, 4]
list1 = [2,4,6,8]

print('list0: '+' '.join(str(e) for e in list0))

# for loop using range
# here i is a int representing index
for index in range( len(list0) ):
    # 8 % 2 = 0 = false
    # 9 % 2 = 1 = true
    if ( list0[index] % 2 ):
        print(list0[index])


# here i is int but represent list0 elements
for listItem in list0:
    if (listItem % 2):
        print(listItem)


# not 0 means true
if (3):
    print('yes can use other than 1 for true')


print('end of for')

""" function with the same effect as 
    the for loop above
"""
"""
    argument name is local
"""

def findOdd(list):
    r = ''
    for i in range(len(list)):
        if (list[i] % 2): # find odd
            # convert int to string with str(int)
            r+=(str(list[i]) + ' ')
    
    if (len(r) == 0):
        print('no odd number found')
        return 0
    else:    
        print(r)
        return 1

def findOdd():
    return 0

findOdd(list0)
findOdd(list1)

if (findOdd(list0)):
    print('there are some odd numbers in list0')
