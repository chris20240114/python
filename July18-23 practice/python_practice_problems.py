#1. Write a Python function student_data () which will print the id of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.
    
#import keyboard 
'''
def student_data(**kwargs): 
    if 'student_id' in kwargs:
        student_id = {kwargs['student_id']}
        print(f"\nstudent ID: " + str(student_id))
    if 'student_class' in kwargs:
        print(f"\nStudent Class: {kwargs['student_class']}")
    if 'student_name' in kwargs:
        print(f"\nstudent name: {kwargs['student_name']}")
        

student_data(student_id = 'FN1', student_class = 'History', student_name = 'John')


class Student(object):
    def __init__(self, id, name):
        self.student_id = id
        self.student_name = name
#Original attributes and their values of the Student class:
def original_attribute(self):
    for attr, value in Student.__dict__.items():
        if not attr.startswith('_'):
            print(f'{attr} -> {value}')
#After adding the student_class, attributes and their values with the said class:
Student.student_class  = 'V'
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
#After removing the student_name, attributes and their values from the said class:
del Student.student_name
#delattr(Student, 'student_name')
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
#adding student number
Student.student_number = '1'
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} = {value}')
'''
'''
if keyboard.read_key() == "a": 
    print ('You pressed "a".')
'''

#3. Write a Python program to reverse a string. Go to the editor
'''
Sample String : "1234abcd"
Expected Output : "dcba4321" 
'''

from xml.etree.ElementTree import PI


def reverse_string(x):
    y= ''.join(list(reversed(x)))
    return y
print(reverse_string('123456789'))

#or

def reverse_string1(x):
    return (x[::-1])

print(reverse_string1('123456789'))

#4. Write a Python program to calculate the sum of a list of numbers with recursion 

def sum(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + sum(x[1:])
print(sum([1, 3, 5, 7]))

#5. 1. Write a Python program to convert degree to radian. Go to the editor
#Note : The radian is the standard unit of angular measure, used in many areas of mathematics. An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle; one radian is just under 57.3 degrees (when the arc length is equal to the radius).

#π rad = 180 degrees
#π/180 rad = 1 degree
#180/π = 1 rad

PI=22/7
DEGREES = 180
def degree_to_radian(x):
    y= x*PI/DEGREES
    return y 

print(degree_to_radian(20))

#6. 