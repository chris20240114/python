import math
'''pounds = float(input("Enter your weight in Pounds"))
kg = pounds * 0.453592
print("my weight is ",kg, "kg")'''

x = input("What meal would you be having? (Enter: breakfast/lunch/dinner): ")

if x == 'breakfast' or x == 'Breakfast':
    print("How about some avocado on toast?")
elif x == 'lunch' or x == 'Lunch':
    print("How about some fish and chips?")
elif x == 'dinner' or x == 'Dinner':
    print("How about some fried chicken?")
else:
    print("Please enter breakfast, lunch, or dinner!")