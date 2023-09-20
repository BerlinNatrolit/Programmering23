# Class that defines a room
class Room:
    
    # Constructor or init method. This is run automatically when you create an object of type Room
    def __init__(self, name):			# Self is used to reference your own objects. E.g. name
        self.name = name				# The class itself name is assigned name send to the init function.
        self.items = []					# define a couple of variables.
        self.doors = []
        self.description = ""
        self.inspect = ""
    
    # Add a description of the room.
    def setDescription(self, description):	# A method. A function that is within a class.
        self.description = description
    
    # add an item to the room
    def addItem(self, item):
        self.items.append(item)
    
    # When we have doors in the room we are assigning them to this.
    def addDoor(self, door):
        self.doors.append(door)
        
    # Set a description if we are looking close at the room
    def setInspect(self, inspect):
        self.inspect = inspect
        
    # Lets define a function that creates and returns a description of the room
    def toString(self):
        # Description of room
        response = ""
        response = self.description + "\n"
        response = response + "Items you see scattered around the room: \n"
        
        # Add all the items
        for item in self.items:
            response = response + item + "\n"
        response = response + "\n"
        
        # Print all the doors
        response = response + "There are doors to your: "
        # Format and print out all the directions that are available in the room.
        directions = ""
        for direction in self.doors:
            directions = directions + ", " + direction
        directions = directions[2:]
        response = response + directions + "\n\n"
        
        return response
    
    # print out detailed information about room.
    def lookCloser(self):
        print(self.inspect)
