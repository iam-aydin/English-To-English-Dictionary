# fix this issues
# TODO-1 install the pyinstaller package to create an .exe file for this main.py with pasting this command into
# the terminal of pycharm -> pyinstaller main.py --onefile
from os import system
from second_library import words_mean_2
from first_library import word_dict

words_mean = [word_dict]
cur_version = "v2.34"


def clear():
    system("cls")


print(f"Welcome to EWD (English Word Dictionary) {cur_version}")
print('You are able to get information about the program with typing\n "-opt"\n')
len_words_mean_list = len(words_mean)
len_words_mean_list_2 = len(words_mean_2)

users_word = input("Please enter a word: ")


def start_loop(user_s_word):
    """This loop goes into the word_mean list that includes dictionary of words and checks if the user's input is in the
    dictionary or not"""
    start_the_dictionary_loop = True
    founded = False
    while start_the_dictionary_loop:
        for current_pos in range(len_words_mean_list):
            if user_s_word in words_mean[current_pos]:
                word = users_word
                mean = words_mean[current_pos][users_word]
                print(f"\nWord :{word.title()}\nMeaning {mean}")
                founded = True
        for current_pos in range(len_words_mean_list_2):
            if user_s_word in words_mean_2[current_pos]:
                word = users_word
                mean = words_mean_2[current_pos][users_word]
                print(f"\nWord :{word.title()}\nMeaning : {mean}")
                founded = True
        if not founded:
            print(f"""The word " {users_word} " is not in program's dictionary yet.""")
        start_the_dictionary_loop = False


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
        print(f"The current version you're using is {cur_version}")

    elif users_word == "-opt":
        print("Type these Codes to do another things:\n"
              "● to get the Release Date : -release\n"
              "● to get the current version : -cur\n"
              "● to clear the screen : -c\n"
              "● to read about the program: -about\n"
              "● if you want to contact with me : -cont\n")

    elif users_word == "-about":
        print(f"\n● English-To-English-Dictionary\n"
              f"I made this English to English dictionary as a hobby project.\n "
              f"It’s got a bunch of words and definitions in it,"
              f" so you can learn new stuff and sound smarter when you talk.\n "
              f"It’s super easy to use - just type in the word you want and boom! You get the definition.\n"
              f"It’s great for students, professionals, or anyone\n"
              f"who wants to learn new words and impress their friends.\n")

    elif users_word == "-cont":
        print(f"\nHey i'm Aydin\n"
              f"You can contact with me on Telegram just send a massage to this ID\n"
              f"@ichbinaydinq")


def main_fun():
    """To start the main program"""
    global users_word

    it_should_continue = True
    while it_should_continue:
        if (users_word == "-exit" or users_word == "-cur" or users_word == "-c" or users_word == "-release" or
                users_word == "-about" or users_word == "-opt" or users_word == "-cont"):
            checking()
            users_word = input("please enter a word: ")
        else:
            start_loop(users_word)
            users_word = input("please enter a word: ")


main_fun()
