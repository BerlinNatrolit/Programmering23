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
    
    # return the total damage with current DoT:s (Damage over time)
    # Total damage is weapon base damage as well as all dot-damage.
    def getDamage(self):
        totalDamage = self.baseDamage+self.dotDamage*self.dotTime
        return totalDamage
    
    # Set a new damage on the weapon
    def setDamage(self, newDamage):
        self.baseDamage = newDamage
     
    # Add a DoT to the weapon
    def setDot(self, newDotDamage, newDotTime):
        self.dotDamage = newDotDamage
        self.dotTime = newDotTime
    
    # Critical hits double the total damage.
    def criticalHit(self):
        return self.getDamage()*2

    #Return string representation of item
    def ToString(self):
        return name + "\n" + description