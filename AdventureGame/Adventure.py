# Display a welcome screen for the user
def welcomeScreen():
    # Welcome screen
    print("Hello and welcome to Jimmys Berlin adventure")
    print("This game will blow you away!!!!!!!!!!!!!!!!")
    print("********************************************")
    print()
    print("You just ran into a big mansion after running through a haunted forest."
    print()

# Print out a nicely formatted description and view of the room.
def displayRoom(description, doors, items):
    # Print description
    print(description)
    
    # Print out items
    print("Items you see scattered around the room: ")
    # Format and print out all the directions that are available in the room.
    for item in items:
        print(item)
    print()
    
    #print doors
    print("There are doors to your: ", end="")
    # Format and print out all the directions that are available in the room.
    directions = ""
    for direction in doors:
        directions = directions + ", " + direction
    directions = directions[2:]
    print(directions)
    print()
    
# Display the menu for the user.
def displayMenu():
    print("What do you want to do?")
    print("1. Go north")
    print("2. Go south")
    print("3. Go west")
    print("4. Go east")
    print("5. look")
    print("0. Quit game")

def lookingCloser(closer):
    print("When you are looking closer in the room, you can see:")
    print(closer)

# Ask user for input
def fetchInput():
    ans = input("Please enter your choice: ")
    if ans.isdigit():							# True om ans är en siffra. False om det är någonting annat.
        if int(ans) >= 0 and int(ans) < 6:		# Kollar om ans är mellan 0 och 5
            return int(ans)
    return -1									# Returnera -1 om något av de övriga villkoren är falska. 
                                                # Så vet vi att något är fel om det returneras negativa tal från funktionen.

# Define a room
description1 = "You are standing in a long hallway with chandelers hanging from the roof, and paintings all along the wall. You can see doors along the side, and one big door straight forward."
doors1 = ["left", "right", "forward", "back"]
items1 = ["Sword", "Bottle", "Chest", "Light saber - A weapong for a more civilized time"]
closer1 = "the light saber has a purple tint to it."

###############################
# Main program

welcomeScreen()

#Main loop/Gameloop
run = True
while run:
    # Display the room you are in.
    displayRoom(description1, doors1, items1)
    
    # Display main menu for user.
    displayMenu()
    
    # Ask user for input
    choice = fetchInput()
    
    #Check user input
    if choice == -1:
        print("Sorry! Did not understand what you meant? Please give a number.")
        continue
    
    # Do something based on what the user asks for.
    # if the user enters something you dont understand, let him know.
    if choice == 0:
        run = False
    elif choice == 1:
        print("you are going north")
    elif choice == 2:
        print("you are going south")
    elif choice == 3:
        print("you are going east")
    elif choice == 4:
        print("you are going west")
    elif choice == 5:
        lookingCloser(closer1)
    else:
        print("sorry, you asked for something i cannot do!")