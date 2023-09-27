from Room import Room
from Item import Item


class Adventure:
    # init function
    # Lets initialize the entire world
    def __init__(self, name):
        self.name = name
        self.world = None
        self.playery = None
        self.playerx = None


    # Display a welcome screen for the user
    def welcome_screen(self):
        # Welcome screen
        print("Hello and welcome to " + self.name)
        print("This game will blow you away!!!!!!!!!!!!!!!!")
        print("********************************************")
        print()
        print("You just ran into a big mansion after running through a haunted forest.")
        print()

    # Do we need to clean anything up or do anything else when closing the game?
    def turn_off(self):
        print("Thanks for playing the game!")

    # Display the menu for the user.
    def display_menu(self):
        print("What do you want to do?")
        print("1. Go forward")
        print("2. Go backward")
        print("3. Go left")
        print("4. Go right")
        print("5. look")
        print("0. Quit game")

    # Ask user for input
    def fetch_input(self):
        ans = input("Please enter your choice: ")
        if ans.isdigit():							# True om ans är en siffra. False om det är någonting annat.
            if int(ans) >= 0 and int(ans) < 6:		# Kollar om ans är mellan 0 och 5
                return int(ans)
        return -1									# Returnera -1 om något av de övriga villkoren är falska.
                                                    # Så vet vi att något är fel om det returneras negativa tal från funktionen.

    def init_game(self):
        ###
        # Define environment

        sword = Item("Sword", "This is a wooden sword")
        chest = Item("Chest", "Big chest")
        lsword = Item("Light saber", "A weapon for a more civilized time")

        # Define room
        hallway = Room("Hallway")
        hallway.setDescription(
            "You are standing in a long hallway with chandelers hanging from the roof, and paintings all along the wall. You can see doors along the side, and one big door straight forward.")
        hallway.addItem(sword)
        hallway.addItem(chest)
        hallway.addItem(lsword)
        hallway.setInspect("the light saber has a purple tint to it.")

        banquet = Room("Banquet Hall")
        banquet.setDescription(
            "You are in a huge banquet hall, and are baffeled by the table in the middle surrounded by chairs")
        banquet.setInspect("Upon further investigation it looks like this hoom has not been used for hundreds of years")

        basement = Room("Basement")
        basement.setDescription("a damp and dark place.")
        basement.setInspect("Rats are crawling all around the place.")

        living_room = Room("living room")
        living_room.setDescription("A beautiful and cosy living room")
        living_room.setInspect("Everything is in blue and red")

        hallway.addDoor("right")
        hallway.addDoor("forward")
        banquet.addDoor("back")
        banquet.addDoor("right")
        basement.addDoor("left")
        basement.addDoor("back")
        living_room.addDoor("left")
        living_room.addDoor("forward")

        # Map structure.
        """
        banquet     basement

        hallway     living room
        """
        # Define map
        self.world = [[banquet, basement], [hallway, living_room]]
        # Where is the player currently in the world?=
        self.playerx = 0
        self.playery = 1

    # Let's start the game
    def run(self):
        ###############################
        # Main program

        self.welcome_screen()

        # Main loop/Gameloop
        run = True
        while run:
            # Display the room you are in.
            print("playery, playerx: " + str(self.playery) + " " + str(self.playerx))
            print(self.world[self.playery][self.playerx].toString())

            # Display main menu for user.
            self.display_menu()

            # Ask user for input
            choice = self.fetch_input()

            # Check user input
            if choice == -1:
                print("Sorry! Did not understand what you meant? Please give a number.")
                continue

            # Do something based on what the user asks for.
            # if the user enters something you don't understand, let him know.
            if choice == 0:
                run = False
            elif choice == 1:
                print("you are going forward")
                if self.playery > 0:
                    self.playery = self.playery - 1
                else:
                    print("There is no door there")
            elif choice == 2:
                print("you are going ")
                if self.playery < len(self.world):
                    self.playery = self.playery+1
                else:
                    print("There is no door there")
            elif choice == 3:
                print("you are going left")
                if self.playerx > 0:
                    self.playerx = self.playerx-1
                else:
                    print("There is no door there")
            elif choice == 4:
                print("you are going right")
                if self.playerx < len(self.world[self.playery]):
                    self.playerx = self.playerx + 1
                else:
                    print("There is no door there")
            elif choice == 5:
                self.world[self.playery][self.playerx].lookCloser()
            else:
                print("sorry, you asked for something i cannot do!")
