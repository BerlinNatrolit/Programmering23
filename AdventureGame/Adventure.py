from Room import Room

# Display a welcome screen for the user
def welcomeScreen():
    # Welcome screen
    print("Hello and welcome to Jimmys Berlin adventure")
    print("This game will blow you away!!!!!!!!!!!!!!!!")
    print("********************************************")
    print()
    print("You just ran into a big mansion after running through a haunted forest.")
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


# Ask user for input
def fetchInput():
    ans = input("Please enter your choice: ")
    if ans.isdigit():							# True om ans är en siffra. False om det är någonting annat.
        if int(ans) >= 0 and int(ans) < 6:		# Kollar om ans är mellan 0 och 5
            return int(ans)
    return -1									# Returnera -1 om något av de övriga villkoren är falska. 
                                                # Så vet vi att något är fel om det returneras negativa tal från funktionen.

# Define a room
hallway = Room("Hallway")
hallway.setDescription("You are standing in a long hallway with chandelers hanging from the roof, and paintings all along the wall. You can see doors along the side, and one big door straight forward.")
hallway.addDoor("left")
hallway.addDoor("right")
hallway.addDoor("forward")
hallway.addDoor("back")
hallway.addItem("Sword")
hallway.addItem("Bottle")
hallway.addItem("Chest")
hallway.addItem("Light saber - A weapon for a more civilized time")
hallway.setInspect("the light saber has a purple tint to it.")

banquet = Room("Banquet Hall")
banquet.setDescription("You are in a huge banquet hall, and are baffeled by the table in the middle surrounded by chairs")
banquet.addDoor("back")
banquet.setInspect("Upon further investigation it looks like this hoom has not been used for hundreds of years")

###############################
# Main program

welcomeScreen()

#Main loop/Gameloop
run = True
while run:
    # Display the room you are in.
    print(banquet.toString())
    #displayRoom(description1, doors1, items1)
    
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
        banquet.lookCloser()
    else:
        print("sorry, you asked for something i cannot do!")