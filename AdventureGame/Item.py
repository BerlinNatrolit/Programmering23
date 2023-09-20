# Class describing an item
class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    #return name of item
    def getName(self):
        return self.name

    #Return description of item
    def getDescription(self):
        return self.description

    #Return string representation of item
    def ToString(self):
        return name + "\n" + description