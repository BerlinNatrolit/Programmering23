# Define a room
description = "very big room with chandeler hanging from the roof, and paintings all along the wall."
doors = ["north", "south", "east"]


# Welcome screen
print("Hello and welcome to Jimmys Berlin adventure")
print("********************************************")
print()

#Main loop/Gameloop
run = True
while run:
    # Print room
    print("You are standing in a " + description)
    print("There are doors to your:  ")
    
    # Format and print out all the directions that are available in the room.
    directions = ""
    for direction in doors:
        directions = directions + ", " + direction
    directions = directions[2:]
    print(directions)
    
    # Print menu
    print("What do you want to do?")
    print("1. Go north")
    print("2. Go south")
    print("3. Go west")
    print("4. Go east")
    print("5. look")
    print("0. Quit game")
    
    # Ask user for input
    choice = input("Please enter your choice: ")
    
    #Sanitize user input
    if not choice.isnumeric():
        print("Sorry! Did not understand what you meant? Please give a number.")
        continue
    
    # Do something based on what the user asks for.
    # if the user enters something you dont understand, let him know.
    choice = int(choice)
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
        print("you are looking really hard, but cant find anything new")
    else:
        print("sorry, you asked for something i cannot do!")