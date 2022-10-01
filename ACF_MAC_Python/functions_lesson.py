import math
#factorial with for loop
def factorial1(num):
    factorial = 1
    if num < 0:
        print("factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
    print(math.factorial(num))
factorial1(5)



#Factorial with while loop
def factorial(num):
    fact = 1
    while(num!=0):
        fact *= num
        num = num - 1
    print("Factorial is",fact)

num = int(input("Enter number "))
factorial(num)



#Uppercase text
def response(text):
    z = text.upper()
    print(z)

text = input("Enter String: ")  # pythonlobby
response(text)

#consanants
def count(val):
    vowel = 0
    consonant = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            consonant +=1
        else:
            consonant +=1

    print("Count of vowels is ",vowel)
    print("Count of consonant is ",consonant)
