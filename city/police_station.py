# --- Import Modules ---

import time
import os
import subprocess
import sys

# --- Global Variables ---

loop_search = 5
option_navigate = None
loop_prison = 5
file_path_sl = os.path.join("city", "select_location.py")

# --- Functions ---

def prison():
    global loop_prison, file_path_sl
    os.system('cls' if os.name == 'nt' else 'clear')

    print("After what seemed like hours, you wake up in a small, dark prison cell.")
    time.sleep(2)
    print("\nYou: What the hell? Where am I? Did that guy prison me?")
    time.sleep(2)

    while loop_prison >= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Serve your sentence.")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Serve your sentence..")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Serve your sentence...")
        time.sleep(0.5)
        loop_prison -= 1

    print("Your prison sentence is over. You are being released into the city, little troublemaker.")
    time.sleep(2)

    subprocess.run([sys.executable, file_path_sl])
    sys.exit()

def steal_gun():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("You make your way to the armory.")
    time.sleep(2)
    print("A guard approaches you...")
    time.sleep(3)
    print("\n Guard: WHAT THE HELL DO YOU THINK YOU'RE DOING HERE, HUH?")
    time.sleep(3)
    print("\nBefore you can speak, he grabs you by the collar and gives you a headbutt.")
    time.sleep(3)
    print("You lost your vision temporarily...")
    prison()

def navigate_loc():
    global option_navigate, file_path_sl

    os.system('cls' if os.name == 'nt' else 'clear')
    print("You see quite a few places in the police station... wanna explore them or cause trouble?")
    time.sleep(2)
    print("\nType a number to navigate:")
    print("\n1. Exit the police station")
    print("2. Try to steal a gun")

    option_navigate = input("\n>>> ")

    if option_navigate == "1":
        subprocess.run([sys.executable, file_path_sl])
        sys.exit()
    elif option_navigate == "2":
        steal_gun()
    else:
        print("Please type in a number to continue.")
        return navigate_loc()

def enter_loc():
    global loop_search
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You enter the police station. A guard approaches you.")
    time.sleep(2)
    print("\nGuard: Hello, mind if we search you?")
    time.sleep(2)
    print("\nYou: Actually, yeah, I do mind-")
    time.sleep(2)
    print("\nGuard: HE HAS A GUN!")
    time.sleep(1.5)
    print("\nYou: WAIT, NO?!")
    time.sleep(1.5)
    print("\nSuddenly, several armed guards approach you and tackle you.")
    time.sleep(2)

    while loop_search >= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You are being searched.")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You are being searched..")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You are being searched...")
        time.sleep(0.5)
        loop_search -= 1

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nThe police found your toy pistol.")
    time.sleep(2)
    print("\nGuard: Damn, you scared the hell out of us.")
    time.sleep(2)
    print("\nYou: I can explain...")
    time.sleep(2)
    print("\nGuard: Nuh-uh, better not talk about this. We've talked about this.")
    time.sleep(2)
    print("\nYou: What do you mean we talked about this?")
    time.sleep(2)
    print("\nGuard: Shut up, you know exactly what I mean.")
    time.sleep(2.5)
    print("\nThe Guard lets you go. You are now free to navigate through the police station.")
    time.sleep(4)
    navigate_loc()

enter_loc()