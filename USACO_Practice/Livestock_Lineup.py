#use re.search() to get the constraints in each argument, and then put them into a tuple. Iterate through all the constraint
#arguments and then append into a list. Iterate through the list, and using a nested for loop, return the first and second
#constraint in the tuple. Append the tuples into an empty list if they are not already in the list. If one of the tuple
#is already in the list, then check the corresponding index in the list, and check in the index +1 and -1 are constraints.
#If not, append in alphabetical order; if yes, then append to the index+ or - 1 that is not a constraint. If both index and +1
#and -1 are constraints, then return to the user that the constraint given has no real solutions. 


import re
def milking(CowNum, *argv):
    #Declaring the list of cows
    COWS = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
    ordered_cows = {"Bessie":1, "Buttercup":2, "Belinda":3, "Beatrice":4, "Bella":5, "Blue":6, "Betsy":7, "Sue":8}
    ordered_cows1 = [[] for _ in range(len(COWS))]
    COWS = sorted([

        'Bessie',

        'Buttercup'

        'Belinda',

        'Beatrice',

        'Bella',

        'Blue',

        'Betsy',

        'Sue'

    ])

    cow_inds = {c: i for i, c in enumerate(COWS)}
    neighbors = [[] for _ in range(len(COWS))]
    #Getting the first and last cow name of each constraint
    if len(argv)<=8:
        for arg in argv:
            constraint1 = (arg)
            x = (re.search(" must", arg))
            x = x.span()
            x = int(x[0])
            constraint1 = (constraint1[:x])
            constraint2 = (arg)
            y = (re.search("beside ", constraint2))
            y = y.span()
            y = int(y[1])
            constraint2 = constraint2[y:]
            constraint_tuple = (constraint1, constraint2)
            print(constraint_tuple)
            #Checking if the cow is already in the list
            inlist1 = False
            inlist2 = False
            con2pos = 0
            neighbors[constraint1].append(constraint2)
            neighbors[constraint2].append(constraint1)
            for i in range(len(ordered_cows)):
                if constraint1 == ordered_cows[i]:
                    inlist1=True
                elif constraint2 == ordered_cows[i]:
                    inlist2=True
                    con1pos = i
            if inlist1 != True:
                pass
            if inlist2 != True:
                ordered_cows.append(constraint2)
            if not(ordered_cows[con2pos+1] == constraint1 or ordered_cows[con2pos-1] == constraint1):
                pass
        print(neighbors)


    #For too many constraints
    else:
        print("You have too many constraints!")
    
    #Final step
    # for i in range(len(cows)):
    #     print(cows[i])
milking(1, "Buttercup must be milked beside Bella", "Blue must be milked beside Bella", "Sue must be milked beside Beatrice")
