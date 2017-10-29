from time import sleep
from os import system
import msvcrt


def start_up_instructions():
    print("Input lines will end with a :")
    sleep(3)
    print("To advance with text, simply press enter")
    sleep(3)
    print("To submit an answer, also press enter")
    sleep(3)
    # Flush the buffer
    while msvcrt.kbhit():
        msvcrt.getch()
    input("Press enter to continue")
    system('cls')


def get_settings():
    try:
        openfile = open("user_settings.txt", "r")
        name = openfile.readline()
        if openfile.readline() == 'y':
            start_up_instructions()

    except FileNotFoundError:
        # Settings needs to be created
        start_up_instructions()
        input("\"Hey, this looks like your first time playing!\"")
        while True:
            input("\"So, do you want to tell me your name?\"")
            name = input("Name: ")
            input("Are you sure you wish to be called " + name + ". This can't be changed later")
            yes_or_no = input("Yes or no: ")
            if yes_or_no.lower() == "yes":
                input("Great! Let's get that saved for you!")
                openfile = open("user_settings.txt", "w")
                openfile.write(name + "\ny")
                openfile.close()
                break
