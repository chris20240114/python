#Bubblesort

def ascending_bubblesort(arraylist):
    num_swaps = 0
    for i in range(len(arraylist)):
        for j in range((len(arraylist)-1)):
            if (arraylist[j])>(arraylist[j+1]):
                arraylist[j], arraylist[j+1] = arraylist[j+1], arraylist[j]
                num_swaps +=1
    print("Array is sorted in %i swaps"%num_swaps)
    print("First element: %i"%arraylist[0])
    print("Last element: %i"%arraylist[len(arraylist)-1])
    return arraylist

def descending_bubblesort(arraylist):
    num_swaps = 0
    for i in range(len(arraylist)):
        for j in range((len(arraylist)-1)):
            if (arraylist[j])<(arraylist[j+1]):
                arraylist[j], arraylist[j+1] = arraylist[j+1], arraylist[j]
                num_swaps+=1
    print("Array is sorted in %i swaps"%num_swaps)
    print("First element: %i"%arraylist[0])
    print("Last element: %i"%arraylist[len(arraylist)-1])
    return arraylist
list1 = [1, 3, 5, 6, 8, 4, 12]

print("Sorted array: ", ascending_bubblesort(list1))
print("")
print("Sorted array: ", descending_bubblesort(list1))