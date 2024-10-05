def start_game():
    print("Welcome to Escape the Dungeon!")
    print("You find yourself trapped in a dark dungeon.")
    print("Your goal is to find the exit and escape!")

    first_choice()

def first_choice():
    print("\nYou see two doors: one on the left and one on the right.")
    choice = input("Which door do you choose? (left/right): ").lower()

    if choice == "left":
        left_door()
    elif choice == "right":
        right_door()
    else:
        print("Invalid choice. Please choose left or right.")
        first_choice()

def left_door():
    print("\nYou enter a room filled with treasure!")
    print("However, a dragon guards the treasure.")
    choice = input("Do you want to (fight) the dragon or (flee) back? ").lower()

    if choice == "fight":
        print("You bravely fight the dragon and manage to defeat it!")
        print("You take some treasure and find a hidden passage to escape the dungeon. You win!")
    elif choice == "flee":
        print("You run back to the previous room.")
        first_choice()
    else:
        print("Invalid choice. Please choose fight or flee.")
        left_door()

def right_door():
    print("\nYou enter a room with a magical portal.")
    print("It leads to a dark forest. You can either (enter) the portal or (go back).")

    choice = input("What do you want to do? ").lower()

    if choice == "enter":
        print("You step through the portal and find yourself in the forest.")
        print("After exploring, you find a way out of the forest and escape the dungeon. You win!")
    elif choice == "go back":
        print("You return to the previous room.")
        first_choice()
    else:
        print("Invalid choice. Please choose enter or go back.")
        right_door()

# Start the game
if __name__ == "__main__":
    start_game()
