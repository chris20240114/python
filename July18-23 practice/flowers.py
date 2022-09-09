from typing import Optional

class flower_finder(object):
    def __init__(self, flowername, color, info):
        self.flowername = flowername
        self.color = color
        self.info = info
        flower_dictionary = {}
        flower_dictionary.update((self.flowername)(self.info))

    def getinfo(self):
        print(self.color, self.info)
        return self.color, self.info

r = flower_finder("rose", "red", "This flower is often used as a symbol of love and romanticism")
print(repr(r.getinfo))
