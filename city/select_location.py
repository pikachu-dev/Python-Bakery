# --- Import Modules ---

import time
import sys
import subprocess
import os

# --- Global Variables ---

vote_location = None
file_path_bank = os.path.join("city", "bank.py")
file_path_police = os.path.join("city", "police_station.py")
file_path_regstore = os.path.join("city", "supermarkets", "regular_store.py")
file_path_hcstore = os.path.join("city", "supermarkets", "healthcare_store.py")

# --- Story ---

def story():
    global file_path_bank, file_path_police, file_path_regstore, file_path_hcstore
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nYou enter the city and first of all open Google Maps.")
    time.sleep(2)
    print("On Google Maps you see these locations:")
    time.sleep(2)

    print("\n1. Bank")
    print("2. Police Station")
    print("3. Regular Supermarket")
    print("4. Healthcare Store")

    vote_location = input("\nType a number to go to the location.\n>>> ")

    if vote_location == "1":
        subprocess.run([sys.executable, file_path_bank])
        sys.exit()
    elif vote_location == "2":
        subprocess.run([sys.executable, file_path_police])
        sys.exit()
    elif vote_location == "3":
        subprocess.run([sys.executable, file_path_regstore])
        sys.exit()
    elif vote_location == "4":
        subprocess.run([sys.executable, file_path_hcstore])
        sys.exit()
    else:
        print("\nPlease enter a number to continue")
        story()

story()