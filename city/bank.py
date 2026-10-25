# --- Import Modules ---

import time
import json
import os
import subprocess
import sys

# --- Bank Account Variables ---

username = None
currency = None
balance = 0

# --- Other Variables ---

file_path_config = os.path.join("config.json")
file_path_wallet = os.path.join("personal", "wallet.json")
vote_create_new_bank_account = None
file_path_select_location = os.path.join("city", "select_location.py")
loop_clean_dishes = 0
job_payout = 0
is_greeted_job = False
vote_ask_continue = None
vote_ask_work = None

# --- Functions ---

def update_account():
    global file_path_config, username, currency, balance
    
    if os.path.exists(file_path_config):
        with open(file_path_config, "r", encoding="utf-8") as file:
            config = json.load(file)
    else:
        config = {}

    if "bank_account" not in config:
        config["bank_account"] = {}
    if "user" not in config:
        config["user"] = {}

    config["user"]["username"] = username
    config["bank_account"]["currency"] = currency
    config["bank_account"]["balance"] = balance

    if os.path.dirname(file_path_config):
        os.makedirs(os.path.dirname(file_path_config), exist_ok=True)

    with open(file_path_config, "w", encoding="utf-8") as file:
        json.dump(config, file, ensure_ascii=False, indent=4)

def cleaner_job():
    global is_greeted_job

    def ask_continue():
        global currency, vote_ask_continue
        print("\nType a number to do the action:")
        print(f"1. Clean a dish for 10 {currency}")
        print("2. Check current account balance")
        print("3. Exit the bank")

        vote_ask_continue = input("\n>>> ")

        if vote_ask_continue == "1":
            clean_dishes()
        elif vote_ask_continue == "2":
            check_account_balance()
        elif vote_ask_continue == "3":
            subprocess.run([sys.executable, file_path_select_location])
            sys.exit()    

    def check_account_balance():
        global balance
        print(f"Your account balance is: {balance}")
        time.sleep(2)
        ask_continue()

    def clean_dishes():
        global loop_clean_dishes, balance
        while loop_clean_dishes < 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cleaning one plate.")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cleaning one plate..")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cleaning one plate...")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            loop_clean_dishes += 1
        balance += 10
        loop_clean_dishes = 0
        update_account()
        print(f"You earned 10 {currency}! Saved to wallet.")
        time.sleep(1.5)
        ask_continue()

    def greeting():
        global username, currency, is_greeted_job
        print(f"\nWelcome, {username}!")
        time.sleep(1)
        print("You were upgraded from homeless to dish cleaner!")
        time.sleep(1)
        print(f"For every dish you clean, you get 10 {currency}. Have fun!")
        is_greeted_job = True
        ask_continue()

    if is_greeted_job == False:
        greeting()
    elif is_greeted_job == True:
        ask_continue()

def create_account():
    global username, currency, balance, file_path_config

    balance = 0
    update_account()

    print("Created a new bank account!")
    print(f"""
        Username: {username},
        Currency: {currency},
        Account Balance: {balance}
    """)

    if balance < 1000:
        print(f"\nBy the way, you only have {balance} {currency} on your account.")
        time.sleep(2)
        vote_work = input("Do you want to work to get some money? Yes or No.\n>>> ")

        if vote_work == "Yes" or vote_work == "yes":
            print("Perfect! You will be immediately hired as a dish cleaner!")
            print("One moment, please...")
            time.sleep(5)
            cleaner_job()
        elif vote_work == "No" or vote_work == "no":
            print("Sorry, bud. You are being forced to work as a dish cleaner.")
            cleaner_job()

# --- Story --- 

def story():
    global vote_ask_work, username, currency, balance, file_path_config

    # Load config (empty if the file doesn't exist yet)
    if os.path.exists(file_path_config):
        with open(file_path_config, "r", encoding="utf-8") as file:
            config = json.load(file)
    else:
        config = {}

    bank_account = config.get("bank_account", {})
    user_section = config.get("user", {})

    username = user_section.get("username")
    currency = bank_account.get("currency")
    balance = bank_account.get("balance", 0)

    # A bank account only exists if a currency has been chosen
    has_account = currency is not None

    if has_account and balance < 1000:
        print("It seems like you already have a bank account.")
        time.sleep(1)
        vote_ask_work = input("Wanna work instead? Yes or No.\n>>> ")

        if vote_ask_work == "Yes" or vote_ask_work == "yes":
            cleaner_job()
            return
        elif vote_ask_work == "No" or vote_ask_work == "no":
            subprocess.run([sys.executable, file_path_select_location])
            sys.exit()

    if has_account:
        cleaner_job()
        return

    vote_create_new_bank_account = input("\nDo you want to create a new bank account? Yes or No\n>>> ")

    if vote_create_new_bank_account == "Yes" or vote_create_new_bank_account == "yes":
        print("Alright, let's create the bank account, we need some details.")

        # Only ask for the username if there is none yet
        if username is None:
            username = input("What's your username?\n>>> ")

        # Always ask for the currency until it is valid
        currency = None
        while currency not in ["EUR", "USD"]:
            currency = input("What currency do you want to use? EUR or USD?\n>>> ")
            if currency not in ["EUR", "USD"]:
                print("Invalid currency. Please choose either EUR or USD.")

        create_account()
    elif vote_create_new_bank_account == "No" or vote_create_new_bank_account == "no":
        print("You need a bank account in this game to play it, duh.")
        time.sleep(1.5)
        print("I will ask you again...")
        story()
    else:
        story()

story()