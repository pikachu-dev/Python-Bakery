# --- Import Modules ---

import json
import os
import time
import subprocess
import sys

# --- Command Functions ---

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear') # Command to Clear the Command Line Interface

# --- Global Variables ---

file_path_config = os.path.join('config.json') # File Path of Root Config JSON-File
file_path_select_location = os.path.join('city', 'select_location.py') # File Path of Location Selection

# --- Classes ---

class Color:
    # Styles
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    # Colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"

class Main:
    # --- Initialization of Main-Class ---
    def __init__(self, username, currency, balance):
        self.username = username
        self.currency = currency
        self.balance = balance
        self.is_greeted_job = False

    def update_bank_account(self): # Update the Bank Account in config.json with new data
        if os.path.exists(file_path_config):
            with open(file_path_config, 'r', encoding='utf-8') as file:
                config = json.load(file)
        else:
            config = {}

        if 'bank_account' not in config:
            config['bank_account'] = {}
        if 'user' not in config:
            config['user'] = {}

        config['user']['username'] = self.username
        config['bank_account']['currency'] = self.currency
        config['bank_account']['balance'] = self.balance

        with open(file_path_config, 'w', encoding='utf-8') as file:
            json.dump(config, file, ensure_ascii=False, indent=4)

    # --- Bank Account ---

    def AskCreateAccount(self): # Ask User to Create a Bank Account
        while True:
            clear_console()
            print(f"{Color.YELLOW}{Color.BOLD}\nWARNING: It seems like you don't own a bank account.{Color.RESET}")
            print("Apparently, even being broke requires paperwork these days.")

            choice_create_account = input("\nDo you want to create a bank account? Yes or No?\n>>> ").strip().lower()

            if choice_create_account == 'yes':
                self.CreateAccount()
                return
            elif choice_create_account == 'no':
                print("\nYou need a bank account to play this game, duh.")
                time.sleep(1.5)
                print("Your opinion has been carefully ignored. I'll ask again.")
                time.sleep(1.5)
            else:
                print(f"{Color.RED}ERROR: Please type Yes or No. It's not rocket science.{Color.RESET}")
                time.sleep(1.5)

    def CreateAccount(self): # Create a New Bank Account
        print("\nAlright, let's create your bank account. The bank needs your life story. Just kidding.")
        time.sleep(1)

        if self.username is None or not str(self.username).strip():
            self.ask_username()

        while self.currency not in ['EUR', 'USD']:
            self.currency = input(f"\n{self.username}, do you want to use US-Dollar (USD) or Euro (EUR)?\n>>> ").strip().upper()

            if self.currency not in ['EUR', 'USD']:
                print(f"{Color.RED}ERROR: Invalid currency. Choose EUR or USD, not monopoly money.{Color.RESET}")

        self.balance = 0
        self.update_bank_account() # Save the New Bank Account

        print(f"{Color.GREEN}{Color.BOLD}\nYour bank account has been created!{Color.RESET}")
        print(f"""
        Username: {self.username}
        Currency: {self.currency}
        Account Balance: {self.balance}
        """)
        time.sleep(1)
        print(f"By the way, you only have {self.balance} {self.currency}. Congratulations on your financial independence.")
        time.sleep(1)
        self.ask_work() # Ask User if they want to Work

    def ask_username(self): # Ask User for Username if Missing
        while self.username is None or not str(self.username).strip():
            print(f"{Color.YELLOW}{Color.BOLD}\nWARNING: You don't have a username set up!{Color.RESET}")
            self.username = input("Please enter your desired username:\n>>> ").strip()

            if not self.username:
                print(f"{Color.RED}ERROR: An invisible username? Very funny. Try again.{Color.RESET}")

        self.update_bank_account()
        print(f"{Color.BLUE}{Color.BOLD}\nINFO: Username updated. The bureaucracy is pleased.{Color.RESET}")
        time.sleep(1)

    def check_account_balance(self): # Check Current Account Balance
        print(f"\nYour account balance is: {self.balance} {self.currency}")

        if self.balance == 0:
            print("Even the ATM is disappointed in you.")
        elif self.balance < 1000:
            print("Your bank account is alive. Barely, but alive.")
        else:
            print("Someone's getting rich from washing dishes. The economy makes no sense.")

        time.sleep(2)

    # --- Jobs ---

    def ask_work(self): # Ask User if they want to Work
        while True:
            vote_ask_work = input("\nDo you want to work to get some money? Yes or No?\n>>> ").strip().lower()

            if vote_ask_work == 'yes':
                print("Perfect! You have been hired immediately. No interview, no dignity.")
                time.sleep(1.5)
                self.select_job()
                return
            elif vote_ask_work == 'no':
                print("Sorry, bud. Your application to remain unemployed has been rejected.")
                time.sleep(1.5)
                self.select_job()
                return
            else:
                print(f"{Color.RED}ERROR: Type Yes or No. HR is losing patience.{Color.RESET}")

    def select_job(self): # Show Available Jobs
        if self.is_greeted_job is False:
            print(f"\nWelcome, {self.username}! You were upgraded from homeless to dish cleaner!")
            time.sleep(1)
            print(f"For every cleaning shift, you earn 10 {self.currency}. That's five plates. Have fun!")
            time.sleep(1)
            self.is_greeted_job = True

        while True:
            print(f"\n{Color.BOLD}Welcome to the Job Center. We have exactly one terrible job available.{Color.RESET}")
            print(f"1. Clean dishes for 10 {self.currency}")
            print("2. Check current account balance")
            print("3. Exit the bank")

            vote_ask_continue = input("\nType a number to do the action:\n>>> ").strip()

            if vote_ask_continue == '1':
                self.clean_dishes()
            elif vote_ask_continue == '2':
                self.check_account_balance()
            elif vote_ask_continue == '3':
                self.exit_bank()
                return
            else:
                print(f"{Color.RED}ERROR: Invalid option. Even the dishes understand numbers.{Color.RESET}")

    def clean_dishes(self): # Clean Five Plates and Earn Money
        loop_clean_dishes = 0

        while loop_clean_dishes < 5:
            clear_console()
            print("Cleaning one plate.")
            time.sleep(0.5)
            clear_console()
            print("Cleaning one plate..")
            time.sleep(0.5)
            clear_console()
            print("Cleaning one plate...")
            time.sleep(0.5)
            clear_console()
            loop_clean_dishes += 1

        self.balance += 10 # Add Job Payout to Bank Account
        self.update_bank_account() # Save New Balance to config.json
        print(f"{Color.GREEN}You earned 10 {self.currency}! Saved to your bank account.{Color.RESET}")
        print("Five plates later, your financial empire has grown by ten whole units. Incredible.")
        time.sleep(1.5)

    # --- Navigation ---

    def exit_bank(self): # Return to City Selection
        print("\nYou leave the bank. The dishes will miss you. The employees won't.")
        time.sleep(1.5)
        subprocess.run([sys.executable, file_path_select_location])
        sys.exit()

    def Start(self): # Start Bank Story
        if self.username is None or not str(self.username).strip():
            self.ask_username()

        if self.currency is None: # Check if User has a Bank Account
            self.AskCreateAccount()
            return

        if self.balance < 1000:
            print("\nIt seems like you already have a bank account.")
            time.sleep(1)
            self.ask_existing_work()
        else:
            print(f"\nWelcome back, {self.username}. You're actually doing pretty well.")
            self.select_job()

    def ask_existing_work(self): # Ask Existing Account Owner if they want to Work
        while True:
            vote_ask_work = input("\nWanna work instead? Yes or No?\n>>> ").strip().lower()

            if vote_ask_work == 'yes':
                self.select_job()
                return
            elif vote_ask_work == 'no':
                print("Understandable. The dishes can wash themselves. Probably.")
                self.exit_bank()
                return
            else:
                print(f"{Color.RED}ERROR: Please type Yes or No.{Color.RESET}")

# --- Start ---

if __name__ == '__main__':
    if os.path.exists(file_path_config):
        with open(file_path_config, 'r', encoding='utf-8') as file:
            config = json.load(file)
    else:
        config = {}

    config_username = config.get('user', {}).get('username')
    config_currency = config.get('bank_account', {}).get('currency')
    config_balance = config.get('bank_account', {}).get('balance', 0)

    account = Main(config_username, config_currency, config_balance)
    account.Start()
