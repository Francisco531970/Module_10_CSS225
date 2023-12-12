# Francisco Sanchez
# 11/21/23

# Here I imported code from different files.
import notepad_module
import Chapter2


# This line of code requires the user to interact a bit more to continue the game.
def wait_for_enter():
    input("Press enter to continue...")


# This line of code starts the first puzzle.
def show_options():
    print("--------------------------------------------------------------")
    print("Let's get started with your first puzzle.")

    while True:
        user_input = input("Please enter '1' to start: ").strip().lower()
        # This code is the first puzzle.
        if user_input == '1':
            print("--------------------------------------------------------------")
            print("Your first puzzle is a simple one.")
            print("What is 20 + 11?")
            print("--------------------------------------------------------------")
            # In this part you can see the correct answer that the player has to enter to move on.
            answer = "31"
            correct = False
            # Here it asks for the player's response.
            while not correct:
                print("Enter your response here")
                code = input()
                # The line of code here is what the player will get if they input the correct answer.
                if answer == code:
                    print("--------------------------------------------------------------")
                    print("Excellent job, that's correct! Now, let me show you how to")
                    print("use the Notepad feature. This feature lets you view,")
                    print("add, delete, and exit your notes. Take a look.")
                    print("--------------------------------------------------------------")
                    notepad_module.main()  # Here is where I imported the notepad feature from another file.

                    correct = True
                else:  # This is the message the player gets if they input the wrong answer.
                    print("Oh no, that's incorrect; try again.")
            break


def second_puzzle():  # This is the start of the second puzzle.
    print("--------------------------------------------------------------")
    print("It's time to start your next puzzle; you get to choose where")
    print("to move around the room. Let's look at the options.")
    print("--------------------------------------------------------------")
    while True:  # Here the player gets options of what they want to do next.
        print("Options:")
        print("1. Look at the bookshelf.")
        print("2. Examine the file cabinet.")
        print("3. Investigate the safe.")
        print("4. Go back to the envelope.")
        print("--------------------------------------------------------------")

        choice = input("Enter the number of your choice (1-4): ")
        # Here you can see the code for the options and how they are connected.
        if choice == "1":
            look_at_bookshelf()
            break
        elif choice == "2":
            examine_file_cabinet()
            break
        elif choice == "3":
            investigate_safe()
            break
        elif choice == "4":
            go_back_to_envelope()
            break
        else:  # This line of code comes up when the player inputs the wrong thing and they have to try again.
            print("Invalid choice. Please enter a number between 1 and 4.")


def look_at_bookshelf():  # This section here is the story line for the bookshelf puzzle.
    print("--------------------------------------------------------------")
    print("You see a collection of books neatly arranged on the bookshelf.")
    print("Let's take a closer look.")
    print("--------------------------------------------------------------")
    wait_for_enter()
    print("--------------------------------------------------------------")
    print("That's weird; only one book has a title. Let's take a look.")
    print("--------------------------------------------------------------")
    wait_for_enter()
    print("--------------------------------------------------------------")
    print("The forgotten twelve")
    print("Could this mean something?")
    print("Would you like to add it to your notepad?")
    print("--------------------------------------------------------------")
    user_input = input("Y/N? ").strip().lower()  # Here the player gets asked if they want to write in their notepad.
    if user_input == 'y':  # If they select the yes option it brings out the notepad.
        notepad_module.main()
        while True:  # After the player exits the notepad these options come up again.
            print("--------------------------------------------------------------")
            print("Options:")
            print("1. Look at the bookshelf. (You're Here)")
            print("2. Examine the file cabinet.")
            print("3. Investigate the safe.")
            print("4. Go back to the envelope.")
            print("--------------------------------------------------------------")

            choice = input("Enter the number of your choice (1-4): ")
            # Here you can see the code for the options and how they are connected.
            if choice == "1":
                look_at_bookshelf()
                break
            elif choice == "2":
                examine_file_cabinet()
                break
            elif choice == "3":
                investigate_safe()
                break
            elif choice == "4":
                go_back_to_envelope()
                break
            else:  # This line of code comes up when the player inputs the wrong thing and they have to try again.
                print("Invalid choice. Please enter a number between 1 and 4.")
    elif user_input == 'n':  # This is the part that comes up if the player selects no.
        print("--------------------------------------------------------------")
        print("Okay, let's keep exploring then.")
        print("--------------------------------------------------------------")
        while True:  # After the player exits the notepad these options come up again.
            print("Options:")
            print("1. Look at the bookshelf. (You're Here)")
            print("2. Examine the file cabinet.")
            print("3. Investigate the safe.")
            print("4. Go back to the envelope.")
            print("--------------------------------------------------------------")

            choice = input("Enter the number of your choice (1-4): ")
            # Here you can see the code for the options and how they are connected.
            if choice == "1":
                look_at_bookshelf()
                break
            elif choice == "2":
                examine_file_cabinet()
                break
            elif choice == "3":
                investigate_safe()
                break
            elif choice == "4":
                go_back_to_envelope()
                break
            else:  # This line of code comes up when the player inputs the wrong thing and they have to try again.
                print("Invalid choice. Please enter a number between 1 and 4.")


def examine_file_cabinet():  # This is the code for the file cabinet.
    print("--------------------------------------------------------------")
    print("It looks like the file cabinet is locked. You will need a")
    print("key to open it.... or kick it.")
    print("Which do you want to try?")
    print("--------------------------------------------------------------")
    while True:  # This code here allows the player to kick it or look around.
        print("Options:")
        print("1. Kick it.")
        print("2. Look for the key.")
        print("--------------------------------------------------------------")

        choice = input("Enter the number of your choice (1-2): ")

        if choice == "1":  # This is what happens when the player kicks it.
            print("--------------------------------------------------------------")
            print("Ouch, that most hurt, but hey, you got it opened! Wait,")
            print("before you open it, what is that thing next to the cabinet")
            print("poking out from underneath?")
            print("--------------------------------------------------------------")
            wait_for_enter()
            print("--------------------------------------------------------------")
            print("**You've found a key**")
            print("Huh, you didn't have to kick it after all. But that doesn't")
            print("matter now; let's open the cabinet and see what's inside.")
            print("--------------------------------------------------------------")
            wait_for_enter()
            print("--------------------------------------------------------------")
            print("**You've found a classified folder**")
            print("It is a classified folder. What could be inside of it?")
            print("--------------------------------------------------------------")
            wait_for_enter()
            print("--------------------------------------------------------------")
            print("[      ] E [         ]")
            print("L [       ][             ]")
            print("[             ] E [          ]")
            print("[    ] V [       ] E [     ]")
            print("[       ] N [       ][   ]")
            print("--------------------------------------------------------------")
            print("Strangely, most of the document looks redacted, but you can")
            print("make something out with the visible letters. Let's use your")
            print("notepad to write the notes down.")
            notepad_module.main()
            print("--------------------------------------------------------------")
            print("Okay, that's everything inside the file cabinet. Let's move")
            print("on to the next puzzle.")
            while True:  # After the player exits the notepad these options come up again.
                print("--------------------------------------------------------------")
                print("Options:")
                print("1. Look at the bookshelf.")
                print("2. Examine the file cabinet. (You're Here)")
                print("3. Investigate the safe.")
                print("4. Go back to the envelope.")
                print("--------------------------------------------------------------")

                choice = input("Enter the number of your choice (1-4): ")
                # Here you can see the code for the options and how they are connected.
                if choice == "1":
                    look_at_bookshelf()
                    break
                elif choice == "2":
                    examine_file_cabinet()
                    break
                elif choice == "3":
                    investigate_safe()
                    break
                elif choice == "4":
                    go_back_to_envelope()
                    break
                else:  # This line of code comes up when the player inputs the wrong thing and they have to try again.
                    print("Invalid choice. Please enter a number between 1 and 4.")
            break
        elif choice == "2":  # This is what comes up if the player looks for the key.
            print("--------------------------------------------------------------")
            print("Okay, let's take a look around. Let's check behind the")
            print("file cabinet.")
            print("--------------------------------------------------------------")
            wait_for_enter()
            print("--------------------------------------------------------------")
            print("What's that thing poking out from underneath? Go ahead")
            print("and grab it.")
            print("--------------------------------------------------------------")
            wait_for_enter()
            print("--------------------------------------------------------------")
            print("**You've found a key**")
            print("Nice! Let's go ahead and open up the file cabinet.")
            print("Give it a try.")
            print("--------------------------------------------------------------")
            wait_for_enter()
            print("--------------------------------------------------------------")
            print("**File Cabinet Unlocked**")
            print("Excellent, you got it opened! Let's see what's inside of it.")
            print("--------------------------------------------------------------")
            wait_for_enter()
            print("--------------------------------------------------------------")
            print("**You've found a classified folder**")
            print("Is that a folder? Could you give it a look? What's inside")
            print("of it?")
            print("--------------------------------------------------------------")
            print("[      ] E [         ]")
            print("L [       ][             ]")
            print("[             ] E [          ]")
            print("[    ] V [       ] E [     ]")
            print("[       ] N [       ][   ]")
            print("--------------------------------------------------------------")
            print("Strangely, most of the document looks redacted, but I think")
            print("you can make something out with the visible letters.")
            print("Let's use your notepad to write the notes down.")
            notepad_module.main()
            print("--------------------------------------------------------------")
            print("Okay, that's everything inside of the cabinet. Let's move")
            print("on to the next puzzle.")
            print("--------------------------------------------------------------")
            while True:  # After the player exits the notepad these options come up again.
                print("Options:")
                print("1. Look at the bookshelf.")
                print("2. Examine the file cabinet. (You're Here)")
                print("3. Investigate the safe.")
                print("4. Go back to the envelope.")
                print("--------------------------------------------------------------")

                choice = input("Enter the number of your choice (1-4): ")
                # Here you can see the code for the options and how they are connected.
                if choice == "1":
                    look_at_bookshelf()
                    break
                elif choice == "2":
                    examine_file_cabinet()
                    break
                elif choice == "3":
                    investigate_safe()
                    break
                elif choice == "4":
                    go_back_to_envelope()
                    break
                else:  # This line of code comes up when the player inputs the wrong thing and they have to try again.
                    print("Invalid choice. Please enter a number between 1 and 4.")
            break


def investigate_safe():  # This is the code for the safe.
    print("--------------------------------------------------------------")
    print("Welcome to the safe. To unlock it, a six-digit code is needed.")
    print("You can return to the other puzzles if you still need to")
    print("gather the six-digit code. What do you want to do?")
    print("--------------------------------------------------------------")
    while True:  # Here the code asks the player to choose one.
        print("Options:")
        print("1. Enter 6 digit code")
        print("2. Go back to exploring")
        print("--------------------------------------------------------------")

        choice = input("Enter the number of your choice (1-2): ")

        if choice == '1':  # Here is the code for the six-digit password.
            print("--------------------------------------------------------------")
            print("!!Input the six-digit code like this 00-00-00!!")
            print("--------------------------------------------------------------")
            answer = "31-12-11"
            correct = False

            while not correct:
                print("What is your response? ")
                code = input()

                if answer == code:  # This comes up when the player inputs the code correctly.
                    print("--------------------------------------------------------------")
                    print("Congrats! You've finished Chapter 1 of Trapped.")
                    print("Are you ready to unlock the next door?")
                    print("--------------------------------------------------------------")
                    wait_for_enter()
                    print("--------------------------------------------------------------")
                    Chapter2.welcome_page()  # Here is where chapter 2 is imported and starts from.

                    correct = True
                else:
                    print("Oh no that's incorrect, try again.")
            break
        elif choice == '2':  # Here it just allows the player to go back if they don't have all the digits for the code.
            while True:
                print("--------------------------------------------------------------")
                print("Options:")
                print("1. Look at the bookshelf.")
                print("2. Examine the file cabinet.")
                print("3. Investigate the safe. (You're Here)")
                print("4. Go back to the envelope.")
                print("--------------------------------------------------------------")

                choice = input("Enter the number of your choice (1-4): ")
                # Here you can see the code for the options and how they are connected.
                if choice == "1":
                    look_at_bookshelf()
                    break
                elif choice == "2":
                    examine_file_cabinet()
                    break
                elif choice == "3":
                    investigate_safe()
                    break
                elif choice == "4":
                    go_back_to_envelope()
                    break
                else:  # This line of code comes up when the player inputs the wrong thing and they have to try again.
                    print("Invalid choice. Please enter a number between 1 and 4.")
            break


def go_back_to_envelope():  # Here the player is allowed to go back to the first puzzle.
    print("--------------------------------------------------------------")
    print("You go back to the envelope with the first puzzle.")
    print("20 + 11")
    print("--------------------------------------------------------------")
    wait_for_enter()
    print("--------------------------------------------------------------")
    while True:  # After that they have to choose where to go next.
        print("Options:")
        print("1. Look at the bookshelf.")
        print("2. Examine the file cabinet.")
        print("3. Investigate the safe.")
        print("4. Go back to the envelope. (You're Here)")
        print("--------------------------------------------------------------")

        choice = input("Enter the number of your choice (1-4): ")
        # Here you can see the code for the options and how they are connected.
        if choice == "1":
            look_at_bookshelf()
            break
        elif choice == "2":
            examine_file_cabinet()
            break
        elif choice == "3":
            investigate_safe()
            break
        elif choice == "4":
            go_back_to_envelope()
            break
        else:  # This line of code comes up when the player inputs the wrong thing and they have to try again.
            print("Invalid choice. Please enter a number between 1 and 4.")


# This code right here makes sure the game runs until it reaches the end.
if __name__ == "__main__":
    second_puzzle()
