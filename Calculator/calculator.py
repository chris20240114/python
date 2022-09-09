import math
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 800, 280, 800)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)
layout = QHBoxLayout()
layout1 = QVBoxLayout()

layout.addWidget(QPushButton("Addition"))
layout1.addWidget(QPushButton("Subtraction"))
layout.addWidget(QPushButton("Multiplication"))
layout1.addWidget(QPushButton("Division"))


window.setLayout(layout1)
window.show()
sys.exit(app.exec())


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    i=1
    if y >0:
        if y > 1:
            while i < y:
                x *= x
                i+=1
                a=x 
        elif y==1:
            a=x
        elif y%1 != 0:

                return a
def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def fibRec(n):
        if(n == 1 or n ==2): return 1
        return fibRec(n-1) + fibRec(n-2) 

print (fibRec(6))
print("Hello".rjust(10))

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    userchoice = input("Enter choice(1/2/3/4/5/factorial/sqrt): ")

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
    if userchoice in ('factorial', 'sqrt'):
        value1 = float(input("Enter first number: "))

        if userchoice == 'factorial':
            print(str(factorial(value1)))
        elif userchoice == 'sqrt':
            print(str(square_root(value1)))
    continue_using = input("would you like to continue? Enter y/n")
    if continue_using == 'y' or continue_using == 'yes':
        continue
    else: 
        break

app = QApplication([])
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)
