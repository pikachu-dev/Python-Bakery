import os
import time
import sys
import subprocess
import json

vote_welcome_help = None
no_counter_vhc = 0
file_path_config = os.path.join("config.json")

def story_start():
    ... # Story unfinished

def welcome():
    global file_path_config

    with open(file_path_config, "r", encoding="utf-8") as f:
        config = json.load(f)

    username = config["user"]["username"]

    print(f"Hello, {username}!")
    time.sleep(1)
    print("I'm Pikachu-Dev, and I built this game.")
    time.sleep(3)
    print("Actually, I was only bored and I wanted to bake a cake in Python.")
    time.sleep(3)
    print("The cake I want to bake is a Chocolate Nutella Cake!!")
    time.sleep(2)
    print("But wait... I'm bad at making cakes... can you help me?")
    time.sleep(2)

    def vote_help_cake():
        global vote_welcome_help, no_counter_vhc
        vote_welcome_help = input("\nWill you help me make the cake? Yes or No?\n>>> ")

        if vote_welcome_help == "Yes" or vote_welcome_help == "yes":
            print("Thank you for helping me! Let's start, I guess...")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            subprocess.run([sys.executable, "pantryCheck.py"])
            story_start()
        elif vote_welcome_help == "No" or vote_welcome_help == "no":
            no_counter_vhc += 1
            
            def no_count_one():
                print("Wait... you don't want to help me?")
                time.sleep(2)
                print("You're pretty rude, huh? Such a bad person... why no help Pikachu-Dev?")
                time.sleep(3)
                print("YOU WILL HELP ME NOW, OKAY?!")
                time.sleep(2)
                vote_help_cake()

            def no_count_two():
                print("So, you still want to reject me, huh?")
                time.sleep(2)
                print("Uh-huh, better not say no a third time, IDIOT.")
                time.sleep(2)
                vote_help_cake()

            def no_count_three():
                print("You know what? I don't need your help anymore.")
                time.sleep(2)
                print("I can make the cake myself, and I will do it better than you.")
                time.sleep(3)
                print("Goodbye, and don't come back here again.")
                time.sleep(2)
                sys.exit()

            if no_counter_vhc == 1:
                no_count_one()
            elif no_counter_vhc == 2:
                no_count_two()
            elif no_counter_vhc == 3:
                no_count_three()
        else:
            vote_help_cake()

    vote_help_cake()

def username_question():
    global file_path_config
    print("Hello, before you can play the game...")
    time.sleep(1)

    with open(file_path_config, "r", encoding="utf-8") as f:
        config = json.load(f)

    config["user"]["username"] = str(input("Choose a username:\n>>> "))

    config["user"]["age"] = int(input("Choose your age:\n>>> "))

    with open(file_path_config, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print("Thank you! <3")
    time.sleep(2)
    
    os.system('cls' if os.name == 'nt' else 'clear')

    welcome()

username_question()