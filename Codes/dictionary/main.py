import os
from os import system
import pandas

cur_version = "v2.77"
# to get uesr's OS type
os_type = os.name



def clear():
    # posix for linux
    if os_type == 'posix':
        system("clear")
    elif os_type == 'nt':
        system('cls')


print(f"Welcome to EWD (English Word Dictionary) {cur_version}")
print("Type these Codes to do another things:\n"
      "● to get the Release Date : -release\n"
      "● to get the current version : -cur\n"
      "● to clear the screen : -c\n"
      "● to read about the program: -about\n"
      "● if you want to contact with me : -cont\n")

users_word = input("Please enter a word: ").lower()



def start_loop(user_s_word):
    """This loop goes into the word_mean list that includes dictionary of words and checks if the user's input is in the
    dictionary or not"""
    founded = False
    for data_count in range(1, 6):
        new = f"data{data_count}.csv"
        data = pandas.read_csv(new)
        words_list = data["word"].to_list()
        start_the_dictionary_loop = True
        while start_the_dictionary_loop:
            # if users_word in words_list:
            #     print(current_word_meaning["meaning"].item())
            if user_s_word in words_list:
                current_word_meaning = data[data.word == user_s_word]
                word = users_word
                try:
                    mean = current_word_meaning["meaning"].item()
                    print(f"\nWord :{word.title()}\nMeaning {mean}")
                    founded = True
                except ValueError:
                    pass
            elif user_s_word.title() in words_list:
                word = users_word.title()
                current_word_meaning = data[data.word == word]
                try:
                    mean = current_word_meaning["meaning"].item()
                    print(f"\nWord :{word}\nMeaning {mean}")
                    founded = True
                except ValueError:
                    pass
            start_the_dictionary_loop = False
    if not founded:
        print(f"""The word " {users_word} " is not in program's dictionary yet.""")




def checking():
    """checks if the user wants to do another things"""
    global users_word

    if users_word == "-release":
        print("ver1 : August,24,2023")

    elif users_word == "-c":
        clear()

    elif users_word == "-exit":
        exit()

    elif users_word == "-cur":
        if os.name == "posix":
            device = "Linux"
        elif os.name == "nt":
            device = "Windows"
        print(f"The current version you're using is {cur_version} on a {device} Device.")

    elif users_word == "-about":
        print("\n● English-To-English-Dictionary\n"
              f"I made this English to English dictionary as a hobby project.\n "
              f"It’s got a bunch of words and definitions in it,"
              f" so you can learn new stuff and sound smarter when you talk.\n "
              f"It’s super easy to use - just type in the word you want and boom! You get the definition.\n"
              f"It’s great for students, professionals, or anyone\n"
              f"who wants to learn new words and impress their friends.\n")

    elif users_word == "-cont":
        print("\nHey i'm Aydin\n"
              f"You can contact with me on Telegram just send a massage to this ID\n"
              f"@ichbinaydinq")


def main_fun():
    """To start the main program"""
    global users_word

    it_should_continue = True
    while it_should_continue:
        if (users_word == "-exit" or users_word == "-cur" or users_word == "-c" or users_word == "-release" or
                users_word == "-about" or users_word == "-cont"):
            checking()
            users_word = input("Please enter a word: ").lower()
        else:
            start_loop(users_word)
            users_word = input("Please enter a word: ").lower()


main_fun()
