inventory = int(input("How many items are there in the inventory? "))

while inventory>=0: 
    if inventory != 0:
        items = 0
        print("We have %i items in the inventory."%inventory)
        items = int(input("How many would you like to buy? "))
        inventory -=items
        if inventory>0:
            print("Now we have %i left."%inventory)
    elif inventory == 0:
        print("All Out!")
        break