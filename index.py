# Project: Text-Based Adventure Game
# Description: A text-based adventure game where players navigate through different rooms and interact with objects.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = []

    def add_object(self, obj):
        """Adds an object to the room."""
        self.objects.append(obj)

    def display(self):
        """Displays the room details."""
        print(f"\n{self.name}\n{self.description}\nObjects in the room: {', '.join(self.objects)}")

    def find_object(self, obj_name):
        """Checks if an object is present in the room."""
        return obj_name in self.objects


class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        """Moves the player to a new room."""
        new_room = getattr(self.current_room, direction, None)
        if new_room:
            self.current_room = new_room
            self.current_room.display()
        else:
            print("You can't go that way!")

    def search(self, obj_name):
        """Searches for an object in the current room."""
        if self.current_room.find_object(obj_name):
            print(f"You found {obj_name}!")
        else:
            print(f"{obj_name} not found in this room.")

    def use_object(self, obj_name):
        """Uses an object in the current room."""
        if self.current_room.find_object(obj_name):
            print(f"You used {obj_name}!")
        else:
            print(f"{obj_name} not found in this room.")


# Example usage
kitchen = Room("Kitchen", "You are in a small kitchen. There is a table in the center.")
living_room = Room("Living Room", "You are in a cozy living room. There is a sofa and a TV.")
bedroom = Room("Bedroom", "You are in a comfortable bedroom. There is a bed and a wardrobe.")

# Prompt the user to enter objects present in each room
objects = input("Enter objects in the kitchen (separated by commas): ").split(",")
kitchen.objects = [obj.strip() for obj in objects]

objects = input("Enter objects in the living room (separated by commas): ").split(",")
living_room.objects = [obj.strip() for obj in objects]

objects = input("Enter objects in the bedroom (separated by commas): ").split(",")
bedroom.objects = [obj.strip() for obj in objects]

# Connect rooms
kitchen.east = living_room
living_room.west = kitchen
living_room.upstairs = bedroom
bedroom.downstairs = living_room

# Create player and start the game
player = Player(kitchen)
player.current_room.display()

while True:
    print("\n---- Actions ----")
    print("1. Move")
    print("2. Search")
    print("3. Use")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        direction = input("Enter the direction (east, west, upstairs, downstairs): ")
        player.move(direction)

    elif choice == "2":
        obj_name = input("Enter the object name to search: ")
        player.search(obj_name)

    elif choice == "3":
        obj_name = input("Enter the object name to use: ")
        player.use_object(obj_name)

    elif choice == "4":
        print("Exiting the game...")
        break

    else:
        print("Invalid choice. Please try again.")
