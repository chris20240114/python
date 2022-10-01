flowerdictionary = {"default flower":"flower_info"}
class flower_finder(object):
    def __init__(self, flowername, color, info):
        self.flowername = flowername
        self.color = color
        self.info = info

    def printinfo(self):
        print(self.color)
        print(self.info)

    def getinfo(self):
        return "Color: "+self.color+"\nFlower info: "+self.info
    
    def flower_dict_append(self):
        flowerdictionary[self.flowername] = self.getinfo()
        print("The flower has been added to the dictionary!")

    def flower_dict_delete(self):
        if self.flowername in flowerdictionary:
            print("The flower has been removed from the dictionary!")
        else:
            print("You can't delete something not in the dictionary!")
        flowerdictionary.pop(self.flowername, 'not_found')

    def search(self, flowername):
        item_in = False
        for i in flowerdictionary:
            if flowername == i:
                print(flowerdictionary[i])
                # temp = str(flowerdictionary[i])
                # temp = temp.replace('\'', '')
                # temp = temp.replace('(', '')
                # temp = temp.replace(')', '')
                # temp = temp.replace(', ', '\n')
                # print("\n" + temp)
                # print('')
                item_in = True
                continue
        if item_in == False:
            print("Flower not found!")

r = flower_finder("rose", "red", "This flower is often used as a symbol of love")
r.flower_dict_append()
delete_object = flower_finder((str(input("Enter flower you would like to delete: "))), "delete", "This object is used to delete flowers in the dictionary")
delete_object.flower_dict_delete()
search_object = flower_finder("Enter the flower you would like to search for: ", "search", "This object is used to search for flowers")
#r.printinfo()
search_object.search(str(input("Enter flower name: ")))

testdict = {'a': 'A', 'b':'B', 'c':'C'}