

'''
This document is about string manipulation.
including: 
-different ways to represent strings in python
-string indexing and slicing
-in, not in operators
-inserting strings to strings
-string methods

@author: Matt
@Date: 

'''


def printPart(n):
    print("_"*10 + 'part ' + str(n) + "_"*10)


# different ways to represent strings in python
printPart(1)
doubleQuote = "between double quote is a string"

singleQuote = 'between single quote is a string'

usingDoubleQuote = "you may have 'single quote' inside a double quote"

usingtripleQuote = '''you can use "double quote" and 'single quote' in triple quote

you can also use triple quote for multiple lines of string

like 
this''' 

singleQuoteSkip = 'however you can have \'single quote\' in single quote with "\\" mark'

print(
    doubleQuote + '\n' + singleQuote + '\n' + usingDoubleQuote + '\n' + usingtripleQuote+ '\n' +
    singleQuoteSkip
)


# string indexing and slicing
printPart(2)
thisString = 'Hello, my name is Chaos'

# replace does not modify the string object
# it creates a new string with the value replaced
print(thisString.replace('H', 'i'))

print(thisString[0])
print(thisString[:9])
print(thisString[7:9])
print(thisString[9:])


# in, not in operators
printPart(3)

if 'na' in thisString:
    print('there is \'na\' in thisString')

if 'ca' not in thisString:
    print('there is no \'ca\' in thisString')


# inserting strings to strings
printPart(4)

print(
    ' with formatting:\n %s \n %s \n %s \n %s \n %s' % 
    (doubleQuote, singleQuote, usingDoubleQuote , usingtripleQuote, singleQuoteSkip)
)

# string methods
# https://www.w3schools.com/spython/python_ref_string.asp
printPart(5)

