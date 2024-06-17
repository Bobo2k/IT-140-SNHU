'''pip install pyfiglet'''

import sys
from pyfiglet import Figlet
f = Figlet(font= "rounded")



def main():
    # Prints intro to the game
    intro()
    # Initializes map of rooms and current room
    rooms, current_room = valid_rooms()
    # Initializes an empty list
    inventory = inventory_manager()
    # Calls gameloop with these variables as parameters
    gameloop(rooms, current_room, inventory)


def gameloop(rooms, current_room, inventory):
    while True:
        # Prints current room and inventory in each iteration of loop
        print("Currently in:", current_room)
        print("Inventory:", inventory, "\n")
        print("--------------------------------")

        #shows available directions
        available_directions = ", ".join([direction for direction in rooms[current_room] if direction != 'item'])
        print(f"Available Directions: {available_directions}")

        # if item is in room, print discovered item
        if rooms[current_room].get("item"):
            print("You have discovered", rooms[current_room]["item"], "\n")
            
        # Gather user input for direction or get 'item' , call lower method
        user_action = input("Please enter direction or get 'item': ").lower()
        print()
        # if user input is valid in the current room
        if user_action in rooms[current_room]:
            # if user goes to roof
            if rooms[current_room][user_action] == "roof":
                # refuse access if inventory is not sufficient
                if len(inventory) != 6:
                    print("Roof is still locked, find missing items")
                else:
                    #Game is over
                    sys.exit(
                        f.renderText(f"The thief {rooms['roof']['villian']} has been found and stopped ! Great Job !"
                    ))
            # switch rooms for user 
            else:
                current_room = rooms[current_room][user_action]
        # checks if user wants to get 'item'
        elif (
            #validates that item is valid
            user_action.startswith("get ")
            and user_action[4:] == rooms[current_room]["item"]
        ):
            #removes item and adds to inventory
            item = rooms[current_room].pop("item")
            inventory.append(item)
            print(f"{item} added to inventory!")
        #user wishes to quit game
        elif user_action == "quit":
            sys.exit("Quitting Game!")
        #user action is invalid input
        else:
            print("Invalid Move")


# Function returns starting room and available rooms
def valid_rooms():
    current_room = "lobby"
    rooms = {
        "lobby": {"east": "lobby office", "item": None},
        "lobby office": {"south": "stairway", "west": "lobby", "item": "lockpick"},
        "stairway": {
            "north": "lobby office",
            "south": "1st floor lobby",
            "item": "mask",
        },
        "1st floor lobby": {
            "north": "stairway",
            "west": "security room",
            "east": "ball room",
            "south": "elevator",
            "item": "flashlight",
        },
        "security room": {"east": "1st floor lobby", "item": "backpack"},
        "elevator": {"north": "security room", "south": "roof", "item": "wallet"},
        "ball room": {"west": "1st floor lobby", "item": "crowbar"},
        "roof": {"villian": "Duke the thief"},
    }
    return rooms, current_room

#returns empty list
def inventory_manager():
    return []

# function returns the beginning of the game
def intro():
    script = """\nWelcome to Investigator: Find the Perp
Try to navigate through the rooms and collect items to find the burgular
Type get 'item' to add to inventory
Type 'quit' to exit game.\n"""
    return print(script)

#calls main function 
if __name__ == "__main__":
    main()
