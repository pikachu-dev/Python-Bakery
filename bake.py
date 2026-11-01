# --- Imports ---

import json
import os
import time
import subprocess
import sys

# --- Global Variables ---

file_path_config = os.path.join("config.json")
file_path_pantry = os.path.join("pantry.json")
file_path_reg_supermarket = os.path.join("city", "supermarkets", "regular_store.py")
pantry_content = {
    "measuring_unit": "grams", 
    "granulated_suguar": 1000,
    "eggs": 6,
    "nutella": 750,
    "neutral_oil": 120,
    "whole_milk": 240,
    "pure_vanilla_extract": 10,
    "salt": 5,
    "all_purpose_flour": 180,
    "unsweetened_cocoa_powder": 75,
    "baking_powder": 7,
    "baking_soda": 7,
    "hot_coffee_or_water": 240,
    "milk_chocolate_chips": 170,
    "hazelnuts_finely_chopped": 120
}

# --- Functions ---

def tool_selection():
    ...

def start():
    print("\nAbout time, you finally arrived at your bakery. Took you long enough.")
    time.sleep(3)
    print("First, you have to grab a LARGE BOWL!")
    time.sleep(2)
    tool_selection()

def load_start():
    loop_load_start = 5

    while loop_load_start >= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Sarting.")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Sarting..")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Sarting...")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        loop_load_start -= 1

    start()

def check_pantry():
    global file_path_pantry, pantry_content, file_path_reg_supermarket

    with open(file_path_pantry, "r", encoding="utf-8") as file:
        pantry = json.load(file)

    if pantry == pantry_content:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nYour pantry contains all of the ingredients.")
        time.sleep(2)
        load_start()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nIt seems like your pantry does not contain the ingredients you need to bake the cake...")
        time.sleep(4)
        print("You gotta go to the supermarket, duh. We'll move you, please hold the line...")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        subprocess.run([sys.executable, file_path_reg_supermarket])
        sys.exit()    

# --- Start Functions ---

check_pantry()