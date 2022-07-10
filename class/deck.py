import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [] #initializes a card?

    def generate(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j)) #generates the value of the card and the symbol of it
    
    def draw(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards #Completely lost in this one

    def count(self):
        return len(self.cards)



# 3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.


'''def remove_nums(list):
  position = 2
  idx = 0
  len_list = (len(list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(list.pop(idx))
    len_list -= 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
remove_nums(nums)

def remove_third_in_list(list):
    lengthoflist = (len(list))
    while len(list) > 0: 
        position = 1
        for i in list:
            print(list.pop(i+position))
            position = (position + 2)%lengthoflist
            lengthoflist -=1
#how to do with a for loop? 
remove_third_in_list(nums)


#11. Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations.

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70


#12 permutations

list12 = [1, 2, 3] 
def permutations(num):
  result_perms = [[]]
  for n in num:
    new_perms = []
    for p in result_perms:
      for i in range(len(p)+1):
        new_perms.append(p[:i] + [n] + p[i:])
        result_perms = new_perms
  return result_perms
    
print(permutations(list12))

#help i don't get this one

#13 area of triangle

print('input base')
base = int(input())
print('input height')
height = int(input())
area = base*height/2

print('area:', area)

#14 Write a Python program to find common divisors between two numbers in a given pair. 

pair = [6, 12]

#The common divisors are 1, 2, 3, 6

def cd(x, y):
    i=1
    common_divisor = []
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            i=common_divisor
            common_divisor.append(i)
            i+=1
        else i+=1
    return common_divisor


print("greatest common divisors: ",cd(6, 12))
print("greatest common divisors: ",cd(2, 8))
print("greatest common divisors: ",cd(12, 24))

#15. Write a Python program to check whether three given lengths (integers) of three sides form a right triangle. Print "Yes" if the given sides form a right triangle otherwise print "No". 

def pythagorean(a, o, h):
    if a**2 + o**2 == h**2:
        return 'This is a right triangle'
    else:
        return 'This is not a right triangle'

print(pythagorean(3, 4, 5))'''

