# --- Import Modules ---

import json
import os
import time
import sys

# --- Command Functions  ---

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear') # Command to Clear the Command Line Interface

# --- Global Variables ---

file_path_config = os.path.join("config.json") # File Path of Root Config JSON-File

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

    def Start(self):
        while True:
            if self.username is None: # Check if User has Username
                try:
                    clear_console() # Clear the Command Line Interface

                    print(f"{Color.RED}{Color.BOLD}It seems like you do not have a username set up!{Color.RESET}") # State Problem
                    print(f"{Color.GREEN}{Color.DIM}{Color.ITALIC}To avoid errors while the game is running, please enter a username{Color.RESET}") # Reason Problem
                    self.username = str(input(f"{Color.YELLOW}\nPlease enter your desired username:\n>>> {Color.RESET}")) # Force Input
                
                    # Save Username to config.json in ROOT
                    config["user"]["username"] = self.username # Save config_username value to config
                    with open(file_path_config, "w", encoding="utf-8") as file: # Open config.json in Write-Mode
                        json.dump(config, file, ensure_ascii=False, indent=4) # Dump Username into config.json
                except TypeError: # Catch TypeError and show Error Message
                    clear_console() # Clear Command Line Interface
                    print(f"{Color.RED}{Color.BOLD}\nERROR: Username can only be a string (TypeError).{Color.RESET}") # Display Error Message
                else:
                    print(f"{Color.BLUE}{Color.BOLD}\nINFO: Username updated. Resuming with game...{Color.RESET}") # Display INFO Message
                    break
            elif self.currency is None and self.balance == 0: # Check if currency and balance are unset/standard
                try:
                    clear_console() # Clear Command Line Interface
                    print(f"{Color.YELLOW}{Color.BOLD}\nWARNING: It seems like you do not have a bank account.{Color.RESET}") # Display Warning Message

                    input_create_account = str(input(f"{Color.YELLOW}{Color.BOLD}Do you want to create a bank account? Type 'Yes' or 'No'\n{Color.BLUE}>>> {Color.RESET}")) # Force User Input

                    if input_create_account == "Yes":
                        try:
                            ask_currency = str(input(f"{self.username}, do you want to use US-Dollar (USD) or Euro (EUR) currency?\n>>> ")) # Ask for Currency with User Input

                            if ask_currency == "USD":
                                with open(file_path_config, "r", encoding="utf-8") as file: # Open config.json in READ-Mode
                                    config = json.load(file) # Load config.json as file in 'config'

                                config["bank_account"]["currency"] = "USD"

                                with open(file_path_config, "w", encoding="utf-8") as file: # Open config.json in WRITE-Mode
                                            json.dump(config, file, ensure_ascii=False, indent=4) # Dump Currency in config.json
                            elif ask_currency == "EUR":
                                with open(file_path_config, "r", encoding="utf-8") as file: # Open config.json in READ-Mode
                                    config = json.load(file) # Load config.json as file in 'config'

                                config["bank_account"]["currency"] = "EUR"

                                with open(file_path_config, "w", encoding="utf-8") as file: # Open config.json in WRITE-Mode
                                            json.dump(config, file, ensure_ascii=False, indent=4) # Dump Currency in config.json
                            else:
                                clear_console()
                                print(f"{Color.RED}{Color.BOLD}\nERROR: Currency can only be a string (TypeError){Color.RESET}")
                        except TypeError: # Catch TypeError
                            print(f"{Color.RED}{Color.BOLD}\nERROR: Currency can only be a string (TypeError)!{Color.RESET}") # Display Error Message
                except TypeError: # Catch TypeError and show Error Message
                    clear_console() # Clear Command Line Interface
                    print(f"{Color.RED}{Color.BOLD}\nERROR: Input can only be a string (TypeError).{Color.RESET}") # Display Error Message

    # --- Jobs ---
    
    def select_job(self):
        # Variables
        jobs_count = 3 # Current Count of all Jobs
        ask_msg = f"""
        \nHello, {self.username}! Welcome to the Job Center.
        \nHere, you can choose a job to earn money.
        \nEach job gives a different amount of money and takes either more or less time.
        \nThere are {jobs_count} jobs to choose from.""" # Start Message

        # Message and User Input
        print(ask_msg) # Show ask_msg variable
        input(f"\nChoose your job, {self.username}:\n>>>") # Show User Input for Selection of Job

        ...

    def UpdateConfig(self):
        if os.path.exists(file_path_config):
            with open(file_path_config, "r", encoding="utf-8") as file:
                config = json.load(file)
        else:
            config = {}

        if "bank_account" not in config:
            config["bank_account"] = {}
        if "user" not in config:
            config["user"] = {}

        config["user"]["username"] = self.username
        config["bank_account"]["currency"] = self.currency
        config["bank_account"]["balance"] = self.balance

        if os.path.dirname(file_path_config):
            os.makedirs(os.path.dirname(file_path_config), exist_ok=True)

        with open(file_path_config, "w", encoding="utf-8") as file:
            json.dump(config, file, ensure_ascii=False, indent=4)

    def CreateAccount(self):
        print("hello world")
    
    def AskCreateAccount(self):
        choice_create_account = None
        
        while choice_create_account == None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nIt seems like you don't own a bank account.")

            choice_create_account = input("\nDo you want to create a bank account? Yes or No?\n\n>>> ")

            if choice_create_account == "Yes" or choice_create_account == "yes":
                choice_create_account == True
                account.CreateAccount()
            elif choice_create_account == "No" or choice_create_account == "no":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nYou need to create a bank account to play the game.")
                time.sleep(3)
                choice_create_account == None
                return

# --- Start ---

with open(file_path_config, "r", encoding="utf-8") as file: # Open config.json in READ-Mode
    config = json.load(file) # Load config.json as file in 'config'

config_username = config["user"]["username"]
config_currency = config["bank_account"]["currency"]
config_balance = config["bank_account"]["balance"]

account = Main(config_username, config_currency, config_balance)


print("Hello World!")
