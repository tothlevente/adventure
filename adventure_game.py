def adventure_game():
    print("You awaken in a dark room. You don't remember how you got here.")
    print("What do you do?")
    print("1. Search for a light switch.")
    print("2. Shout for help.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("You find the light switch and turn on the light.")
        print(
            "The room is small and bare. You see a door to the north and a window to the east."
        )
        print("What do you do?")
        print("1. Go through the door.")
        print("2. Look out the window.")

        choice2 = input("Enter your choice (1 or 2): ")

        if choice2 == "1":
            print("You open the door and find yourself in a long, dimly lit hallway...")
            # The story continues here...
            print(
                "At the end of the hallway, you reach another door. You open it and enter a spacious room."
            )
            print("In the middle of the room, there is a table with a key on it.")
            print("What do you do?")
            print("1. Take the key.")
            print("2. Look around the room.")

            choice3 = input("Enter your choice (1 or 2): ")

            if choice3 == "1":
                print("You take the key and go back to the hallway.")
                print("You reach the door that you thought was a dead end.")
                print("You open it with the key and enter a secret passage.")
                print("Congratulations, you found the way out!")
            elif choice3 == "2":
                print(
                    "You look around the room carefully, but you don't find anything interesting."
                )
                print(
                    "You go back to the hallway and to the door where you found the key."
                )
                print("You decide to take the key and open the door.")
                print("You enter a secret passage.")
                print("Congratulations, you found the way out!")
            else:
                print("Invalid choice.")

        elif choice2 == "2":
            print(
                "You look out the window and see a dense forest stretching as far as the eye can see."
            )
            print(
                "You decide not to climb out the window and instead go back to the door."
            )
            # The story continues here...
        else:
            print("Invalid choice.")

    elif choice == "2":
        print("You shout for help, but no one answers. The silence is deafening.")
        print("You feel more and more uneasy. You notice a small table in the corner.")
        print("What do you do?")
        print("1. Examine the table.")
        print("2. Try the door again.")

        choice3 = input("Enter your choice (1 or 2): ")

        if choice3 == "1":
            print("On the table, you find a dusty old key...")
            # The story continues here...
        elif choice3 == "2":
            print("You rattle the doorknob again, but it's still locked tight.")
            # The story continues here...
        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")


adventure_game()
