# check whether a specified value is contained in a group of values.

'''
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))

def is_group_member(group_data, n):
 return n in group_data
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))

#Write a Python program to print the following string in a specific format (see the output). 
'''
Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

#Code:
print('''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are!''')


#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

first_name = input("Input your First Name : ")
last_name = input("Input your Last Name : ")
print ("Hello  " + first_name[::-1] + " " + last_name[::-1])

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 

'''Sample value of n is 5
Expected Result : 615'''

def sum_n(n):
    n1 = n
    n2 = n*10+n1
    n3 = n*100+n*10+n
    return n1+n2+n3

print(sum_n(5))



def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
nl=[]
for i in range(1500, 2701):
    if (i%7==0) and (i%5==0):
        nl.append(str(i))
print (','.join(nl))

#while loops
n = 1
while n < 5:
    print("Hello World")
    n = n+1


#Write a Python program to get the Fibonacci series between 0 to 50.




def max_fibonacci(n):
    x,y=0,1
    while y<n:
        print(y)
        x,y = y,x+y

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


'''
Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz
'''