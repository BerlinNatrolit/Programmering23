# Class describing an item
class Item:

    def __init__(self, name, description, baseDamage):
        self.name = name
        self.description = description
        self.baseDamage = baseDamage
        self.dotDamage = 0;
        self.dotTime=0;

    #return name of item
    def getName(self):
        return self.name

    #Return description of item
    def getDescription(self):
        return self.description
    
    def getDamage(self):
        totalDamage = self.baseDamage+self.dotDamage*self.dotTime
        return totalDamage
    
    def setDamage(self, newDamage):
        self.baseDamage = newDamage
        
    def setDot(self, newDotDamage, newDotTime):
        self.dotDamage = newDotDamage
        self.dotTime = newDotTime
        
    def criticalHit(self):
        return self.getDamage()*2

    #Return string representation of item
    def ToString(self):
        return name + "\n" + description