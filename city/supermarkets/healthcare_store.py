import subprocess
import sys
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

file_path_select_location = os.path.join("city", "select_location.py")

print("You enter the healthcare store in your local area...")
time.sleep(2)
print("You notice that a Chocolate Nutella Cake is not healthy.")
time.sleep(2)
print("\nYou: What the hell am I doing in a healthcare store? Cakes are not healthy!\n")
time.sleep(3)

vote_return_sl = input("Do you want to exit the healthcare store? Yes or No?")

if vote_return_sl == "Yes" or vote_return_sl == "yes":
    print("You exit the healthcare store happily and don't look back.")
    time.sleep(3)
    subprocess.run([sys.executable, file_path_select_location])
elif vote_return_sl == "No" or vote_return_sl == "no":
    print("Listen up, you will go out of this store now, okay?\n>>> ")
    time.sleep(3)
    print("Oh wait, actually I can force you to exit this store without your consent... BYE!")
    time.sleep(4)
    subprocess.run([sys.executable, file_path_select_location])