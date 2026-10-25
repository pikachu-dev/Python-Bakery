import json
import os
import subprocess
import time
import sys

# --- Global Variables ---

file_path_pantry = os.path.join("pantry.json")
file_path_config = os.path.join("config.json")
file_path_bank = os.path.join("city", "bank.py")
file_path_select_location = os.path.join("city", "select_location.py")
loop_aisle_way = 5
loop_checkout_way = 5
items_price = 56

# --- Functions ---

def load_config():
    global file_path_config

    with open(file_path_config, "r", encoding="utf-8") as file:
        return json.load(file)

def add_ingredients_pantry():
    global file_path_pantry
    
    recipe_ingredients = {
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

    with open(file_path_pantry, "w", encoding="utf-8") as file:
        json.dump(recipe_ingredients, file, ensure_ascii=False, indent=4)

    print("The ingredients have been added to your pantry.")

def buy_ingredients():
    global file_path_bank, items_price

    config = load_config()

    account_balance = config["bank_account"]["balance"]
    currency = config["bank_account"]["currency"]

    if account_balance - items_price >= 56:
        print(f"You bought 15 items for {items_price} {currency}!")
        add_ingredients_pantry()
    else:
        print(f"Sorry, bud. You don't have enough money. Go to the bank and get a job. Items cost {items_price} {currency}.")
        time.sleep(2)
        print("Wait... I'ma just force you to go to the bank real quick...")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        subprocess.run([sys.executable, file_path_bank])
        sys.exit()

def aisle_way():
    global loop_aisle_way, loop_checkout_way, items_price

    while loop_aisle_way > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You make your way through the aisles.")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You make your way through the aisles..")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You make your way through the aisles...")
        time.sleep(1.5)
        loop_aisle_way -= 1

    while loop_checkout_way > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You head to the checkout.")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("YYou head to the checkout..")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You head to the checkout...")
        time.sleep(1.5)
        loop_checkout_way -= 1

    print("\nYou: Hello, ma'am. I would like to buy these precious items here. Would that be acceptable, your honor?")
    time.sleep(3)
    print("\nCashier: Better kneel in front of your superiors, or else you won't get your items.")
    time.sleep(2)
    print("\nYou kneel in front of the cashier, to honor her.")
    time.sleep(2)
    print("\nCashier: Good. Looks like you can handle manners.")
    time.sleep(2)

    config = load_config()

    currency = config["bank_account"]["currency"]

    print(f"\nCashier: That would be {items_price} {currency}.")
    time.sleep(2)
    print("\nYou hand over the money...")
    time.sleep(2)
    buy_ingredients()

def greeting():
    global file_path_select_location

    config = load_config()

    account_balance = config["bank_account"]["balance"]

    if account_balance <= 50:
        print("Suddenly, an employee approaches you...")
        time.sleep(2)
        print("The employee reaches for your wallet without your consent and looks in.")
        time.sleep(3)
        print("\nEmployee: You don't even have money, duh. We're an expensive store. GET OUTTA HERE!")
        time.sleep(3)
        print("\nThe employee kicks you out of his store. You should go to the bank and work.")
        time.sleep(3)

        os.system('cls' if os.name == 'nt' else 'clear')
        subprocess.run([sys.executable, file_path_select_location])
    else:
        print("An employee approaches you with a friendly demeanor...")
        time.sleep(2)
        print("Employee: Hi, buddy! You seem to have money, huh? You're welcome in my store!")
        time.sleep(3)
        print("\nYou look at the shopping list of yours...")
        time.sleep(3)
        print("\nYou: Oh hell nah... 15 items? Damn, this gonna be a looong journey...")
        time.sleep(3)

        aisle_way()

greeting()