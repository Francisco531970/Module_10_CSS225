# Francisco Sanchez
# 11/14/23

import Chapter1


def wait_for_enter():
    input("Please press Enter to continue...")


# Games title (ANSI Shadow)
print("--------------------------------------------------------------")
print("████████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ ")
print("╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
print("   ██║   ██████╔╝███████║██████╔╝██████╔╝█████╗  ██║  ██║")
print("   ██║   ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██║  ██║")
print("   ██║   ██║  ██║██║  ██║██║     ██║     ███████╗██████╔╝")
print("   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═════╝ ")
print("--------------------------------------------------------------")

print("Welcome to Trapped; this game is a text-based escape room.")
print("My name is Francisco, and I'll be helping you along the way.")
print("I'll show you how to use a unique feature in my game that")
print("I'm proud of. For this game, I provided a notepad where")
print("you can write down your answers to each puzzle.")
print("The puzzle difficulty starts easy but increases as you proceed.")
print("Are you ready to get start!")
print("--------------------------------------------------------------")
wait_for_enter()
print("--------------------------------------------------------------")


if __name__ == "__main__":
    print("Welcome to Chapter 1!")
    print("This chapter has three puzzles and a safe that requires")
    print("a six-digit code.")
    print("--------------------------------------------------------------")
    wait_for_enter()

Chapter1.show_options()
Chapter1.second_puzzle()
