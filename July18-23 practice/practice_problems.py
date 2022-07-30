# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
list1=[]
for i in range(1500, 2701):
    if (i%7==0) and (i%5==0):
        list1.append(i)
print(list1)


#2. Write a Python program to check the validity of password input by users.
'''Validation :

    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.''' 

from random import random, randrange
import re
from turtle import right

def Validation(x):
    Capital_Letter=False
    Lowercase_letter=False
    Number=False
    Special_Char=False
    Minimum=False
    Maximum=False

    
    if re.search("[A-Z]", x):
        Capital_Letter=True
    
    if re.search("[a-z]", x):
        Lowercase_letter=True

    if re.search("[0-9]", x):
        Number=True 
    if re.search("[$#@]", x):
        Special_Char=True
    
    if (len(x)<=16 and len(x)>=6):
        Minimum=True
        Maximum=True

    if Capital_Letter and Lowercase_letter and Number and Special_Char and Minimum and Maximum:
        print('password meets requirements')
    else:
        print('invalid password')
    return x

Validation(x=input("Input Password"))

#3. Write a Python program to create a Balanced Binary Search Tree (BST) using an array (given) elements where array elements are sorted in ascending order.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

def sorted_array(nums): 
    if not nums:
        return None
    mid_value = len(nums)//2
    node = TreeNode(nums[mid_value])
    node.left = sorted_array(nums[:mid_value])
    node.right = sorted_array(nums[mid_value+1:])
    return node

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   
    
result = sorted_array([1, 2, 3, 4, 5, 6, 7])
preOrder(result)

#4. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

'''
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True 
'''

'''x=True
List_Of_5_And_19 = []

while x:
    randomNumber = (randrange[0:100])
    List_Of_5_And_19.append(randomNumber)
    if (List_Of_5_And_19.count(19)) == 3:
        List_Of_5_And_19.pop(19)
    if (List_Of_5_And_19.count(5)) >= 3 and (List_Of_5_And_19.count(19)) == 2:
        x=False
        break
print(List_Of_5_And_19)'''

def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3
nums = [19,19,15,5,3,5,5,2]
print("Original list:")
print(nums)
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))
nums = [19,15,15,5,3,3,5,2]
print("\nOriginal list:")
print(nums)
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))
nums = [19,19,5,5,5,5,5]
print("\nOriginal list:")
print(nums)
print("Check two occurrences of nineteen and at least three occurrences of five in the said list:")
print(test(nums))

with open(r"/Users/christopher/Downloads/Document36.txt", 'r') as fp:
    linecount = len(fp.readlines())

interview = open("/Users/christopher/Downloads/Document36.txt", "r")