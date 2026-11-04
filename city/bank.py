# --- Import Modules ---

import json
import os
import time
import sys

# --- Global Variables ---

file_path_config = os.path.join("config.json")

# --- Classes ---

class BankAccount:
    def __init__(self, username, currency, balance):
        self.username = username
        self.currency = currency
        self.balance = balance
    
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

with open(file_path_config, "r", encoding="utf-8") as file:
    config = json.load(file)

usrname = config["user"]["username"]


account = BankAccount()
account.AskCreateAccount()