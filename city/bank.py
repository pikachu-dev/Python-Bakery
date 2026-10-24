# --- Import Modules ---

import time
import json
import os
import subprocess
import sys

# --- Bank Account Variables ---

first_name = None
last_name = None
currency = None
account_balance = 0

# --- Other Variables ---

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
    global file_path_wallet, first_name, last_name, currency, account_balance
    update_account_data = {
        "first_name": first_name,
        "last_name": last_name,
        "currency": currency,
        "account_balance": account_balance
    }

    os.makedirs(os.path.dirname(file_path_wallet), exist_ok=True)

    with open(file_path_wallet, "w", encoding="utf-8") as file:
        json.dump(update_account_data, file, ensure_ascii=False, indent=4)

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
        global account_balance
        print(f"Your account balance is: {account_balance}")
        time.sleep(2)
        ask_continue()

    def clean_dishes():
        global loop_clean_dishes, account_balance
        while loop_clean_dishes < 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cleaning one plate.")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cleaning one plate..")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cleaning one plate...")
            os.system('cls' if os.name == 'nt' else 'clear')
            loop_clean_dishes += 1
        account_balance += 10
        loop_clean_dishes = 0
        update_account()
        print(f"You earned 10 {currency}! Saved to wallet.")
        time.sleep(1.5)
        ask_continue()

    def greeting():
        global first_name, currency, is_greeted_job
        print(f"\nWelcome, {first_name}!")
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
    global first_name, last_name, currency, account_balance, file_path_wallet
    
    empty_bank_account_create = {
        "first_name": first_name,
        "last_name": last_name,
        "currency": currency,
        "account_balance": account_balance
    }

    os.makedirs(os.path.dirname(file_path_wallet), exist_ok=True)
    with open(file_path_wallet, "w", encoding="utf-8") as file:
        json.dump(empty_bank_account_create, file, ensure_ascii=False, indent=4)

    print("Created a new bank account!")
    print(f"""
    First Name: {first_name},
    Last Name: {last_name},
    Currency: {currency},
    Account Balance: {account_balance}
    """)

    if account_balance < 1000:
        print(f"\nBy the way, you only have {account_balance} {currency} on your account.")
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
    global vote_ask_work, first_name, last_name, currency, account_balance

    if not os.path.exists(file_path_wallet):
        os.makedirs(os.path.dirname(file_path_wallet), exist_ok=True)
        empty_bank_account_create = {
            "first_name": None,
            "last_name": None,
            "currency": None,
            "account_balance": 0
        }
        with open(file_path_wallet, "w", encoding="utf-8") as file:
            json.dump(empty_bank_account_create, file, ensure_ascii=False, indent=4)

    with open(file_path_wallet, "r", encoding="utf-8") as file:
        bank_account = json.load(file)

    first_name = bank_account["first_name"]
    last_name = bank_account["last_name"]
    currency = bank_account["currency"]
    account_balance = bank_account["account_balance"]

    if bank_account["first_name"] is not None and bank_account["account_balance"] < 1000:
        print("It seems like you already have a bank account.")
        time.sleep(1)
        vote_ask_work = input("Wanna work instead? Yes or No.\n>>> ")

        if vote_ask_work == "Yes" or vote_ask_work == "yes":
            cleaner_job()
            return
        elif vote_ask_work == "No" or vote_ask_work == "no":
            subprocess.run([sys.executable, file_path_select_location])
            sys.exit()

    if bank_account["first_name"] is not None:
        cleaner_job()
        return

    vote_create_new_bank_account = input("\nDo you want to create a new bank account? Yes or No\n>>> ")

    if vote_create_new_bank_account == "Yes" or vote_create_new_bank_account == "yes":
        print("Alright, let's create the bank account, we need some details.")
        first_name = input("What's your first name?\n>>> ")
        last_name = input("What's your last name?\n>>> ")
        currency = input("What currency do you want to use?\n>>> ")
        create_account()
    elif vote_create_new_bank_account == "No" or vote_create_new_bank_account == "no":
        print("You need a bank account in this game to play it, duh.")
        time.sleep(1.5)
        print("I will ask you again...")
        story()
    else:
        story()

story()