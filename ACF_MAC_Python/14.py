#Python variables

print("hello world")

#integers 1, 2, 3, -1, -2, -3
#strings  'hello', "hello", '''hello'''
#characters 'h'
#booleans True, False  1 == 1, 1==2
#float 1.345678

x = 15 % 7
print(x)

#y = 'Hello World'
#z = 3.14159
#w = True
#e = '5'

'''

Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
    
    '''

print('''Twinkle, twinkle, little star,
	\n\tHow I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are''')

first_name = 'chris'
last_name = 'shen'

print(last_name + " " + first_name)

x1 = 'hello world'
x1 += ' Earth'
x2 = 2
x2 += 2
print(x1)
print(x2)

#Input: Shen Chris
#Output: nehS sirhC

print (last_name[::-1] + " " + first_name[::-1])


#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 

# n = 5
# 5 + 55 + 555 = 615

def sum_n(n):
    n1 = n #5
    n2 = n*10+n #55
    n3 = n*100+n*10+n #555
    return n1 + n2 + n3

#input 
#output (return)

print(sum_n(5))

#input 3 values, evaluate the sum of the three values, if the three values are equal to each other, 
#then times the sum of the three values by three

def sum_thrice(x, y, z):
    sum = x + y + z
  
    if x == y == z:
        sum = sum * 3
    return sum

print(sum_thrice(1, 2, 3)) #1 + 2 + 3 = 6
print(sum_thrice(3, 3, 3)) #(3+3+3) * 3 = 27
print(sum_thrice(10, 10, 10))
