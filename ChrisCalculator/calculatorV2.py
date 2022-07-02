import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x**y
    
    # i = 1
    # a = 0
    # if y > 0:
    #     if y > 1:
    #         while i < y:
    #             x *= x
    #             i+=1
    #             a=x 
    #     elif y==1:
    #         a=x
    #     elif y%1 != 0:
    #         pass
    
    # return a
    

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def fibRec(n):
        if(n == 1 or n ==2): return 1
        return fibRec(n-1) + fibRec(n-2) 

print('''Select operation
1.Add"
2.Subtract
3.Multiply
4.Divide
5. 
exit: to exit''')


holder = True

while holder:
    # take input from the user
    print('Enter choice(1/2/3/4/5/factorial/sqrt): ')
    userchoice = input()

    # check if choice is one of the four options
    if userchoice in ('1', '2', '3', '4', '5'):
        value1 = float(input("Enter first number: "))
        value2 = float(input("Enter second number: "))

        if userchoice == '1':
            print(add(value1, value2))

        elif userchoice == '2':
            print(subtract(value1, value2))

        elif userchoice == '3':
            print(multiply(value1, value2).rjust(10))

        elif userchoice == '4':
            print(str(divide(value1, value2)).rjust(10))
        elif userchoice == '5':
            print(str(exponent(value1, value2)).rjust(10))
    elif userchoice in ('factorial', 'sqrt'):
        value1 = float(input("Enter first number: "))

        if userchoice == 'factorial':
            print(str(factorial(value1)))
        elif userchoice == 'sqrt':
            print(str(square_root(value1)))
    
    elif userchoice == 'exit':
        holder = False
    else:
        print('invalid input')