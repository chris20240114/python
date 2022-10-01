import math
# '''pounds = float(input("Enter your weight in Pounds"))
# kg = pounds * 0.453592
# print("my weight is ",kg, "kg")'''

# x = input("What meal would you be having? (Enter: breakfast/lunch/dinner): ")

# if x == 'breakfast' or x == 'Breakfast':
#     print("How about some avocado on toast?")
# elif x == 'lunch' or x == 'Lunch':
#     print("How about some fish and chips?")
# elif x == 'dinner' or x == 'Dinner':
#     print("How about some fried chicken?")
# else:
#     print("Please enter breakfast, lunch, or dinner!")

for i in range(1,7):
    for j in range(1,7):
        print(str(i)+","+str(j))

rows=int(input("Rows: "))
columns=int(input("Columns = "))
character=input("Character: ")
character1 = character
for j in range(columns-1):
    character+=character1
for i in range(rows):
    print(character)


rows=int(input("Rows: "))
character=input("Character: ")
character1 = character
for c in range(rows):
    print(character)
    character+=character1