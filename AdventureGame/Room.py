class Room:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.doors = []
        self.description = ""
        self.inspect = ""
    
    def setDescription(self, description):
        self.description = description
    
    def addItem(self, item):
        self.items.append(item)
    
    def addDoor(self, door):
        self.doors.append(door)
        
    def setInspect(self, inspect):
        self.inspect = inspect
        
    def toString(self):
        response = ""
        response = self.description + "\n"
        response = response + "Items you see scattered around the room: \n"
        
        for item in self.items:
            response = response + item + "\n"
        response = response + "\n"
        
        
        #print doors
        response = response + "There are doors to your: "
        # Format and print out all the directions that are available in the room.
        directions = ""
        for direction in self.doors:
            directions = directions + ", " + direction
        directions = directions[2:]
        response = response + directions + "\n\n"
        
        return response
    
    def lookCloser(self):
        print(self.inspect)
