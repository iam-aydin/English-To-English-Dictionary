import os
from os import system
import pandas
import sys

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Temp folder where PyInstaller unpacks files
else:
    base_path = os.path.abspath(".")

data_path = os.path.join(base_path, "dictionary_data.csv")
cur_version = "v3.7"
# to get user's OS type
os_type = os.name

def clear():
    # posix for linux
    
    if os_type == 'posix':
        system("clear")
    elif os_type == 'nt':
        system('cls')

print(f"Welcome to English Word Dictionary {cur_version}")

users_word = input("Please enter a word: ").lower()

def start_loop(user_s_word):
    """Searches for the user's input word in a single dictionary CSV file."""
    try:
        data = pandas.read_csv(data_path)
    except FileNotFoundError:
        print("The dictionary data file was not found.")
        return

    words_list = data["word"].to_list()
    founded = False
    
    if user_s_word in words_list:
        current_word_meaning = data[data.word == user_s_word]
        try:
            mean = current_word_meaning["meaning"].item()
            print(f"\nWord: {user_s_word.title()}\nMeaning: {mean}")
            founded = True
        except ValueError:
            pass
    elif user_s_word.title() in words_list:
        current_word_meaning = data[data.word == user_s_word.title()]
        try:
            mean = current_word_meaning["meaning"].item()
            print(f"\nWord: {user_s_word.title()}\nMeaning: {mean}")
            founded = True
        except ValueError:
            pass
    
    if not founded:
        print(f"""The word "{users_word}" is not in the program's dictionary yet.""")

def checking():
    """Checks if the user wants to do other actions."""
    global users_word

    if users_word == "-c":
        clear()

    elif users_word == "-e":
        exit()
        
    elif users_word == "-man":
        print("● to exit : -e\n"
              "● to clear : -c\n")

def main_fun():
    """Starts the main program."""
    global users_word

    it_should_continue = True
    while it_should_continue:
        if users_word in ["-e","-c", "-man"]:
            checking()
            users_word = input("Please enter a word: ").lower()
        else:
            start_loop(users_word)
            users_word = input("Please enter a word: ").lower()

main_fun()
