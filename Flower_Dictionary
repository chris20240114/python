from ast import Pass
from pkgutil import extend_path
from typing import Optional

flowerdictionary = {}
class flower_finder(object):
    def __init__(self, flowername, color, info):
        self.flowername = flowername
        self.color = color
        self.info = info

    def printinfo(self):
        print(self.color)
        print(self.info)

    def getinfo(self):
        return "color: "+self.color, "flower info: "+self.info
    
    def flower_dict_append(self):
        flowerdictionary[self.flowername] = self.getinfo()
        #print(flowerdictionary)
    def search(self, flowername):
        temp = str(flowerdictionary[flowername])
        temp = temp.replace('\'', '')
        temp = temp.replace('(', '')
        temp = temp.replace(')', '')
        temp = temp.replace(', ', '\n')
        print('')
        print(temp)
        print('')

search_object = flower_finder("Enter the flower you would like to search for: ", "search", "This object is used to search for flowers")
r = flower_finder("rose", "red", "This flower is often used as a symbol of love")
#r.printinfo()
r.flower_dict_append()
search_object.search(str(input("Enter flower name: ")))
