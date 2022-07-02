def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    userchoice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if userchoice in ('1', '2', '3', '4'):
        value1 = float(input("Enter first number: "))
        value2 = float(input("Enter second number: "))

        if userchoice == '1':
            print(add(value1, value2))

        elif userchoice == '2':
            print(subtract(value1, value2))

        elif userchoice == '3':
            print(multiply(value1, value2))

        elif userchoice == '4':
            print(divide(value1, value2))