from dictionary_library import words_mean_2
from english_dictionary.scripts.read_pickle import get_dict
words_mean = [get_dict()]
print("Welcome to EWD (English Word Dictionary) v1.971\n")

len_words_mean_list = len(words_mean)
len_words_mean_list_2 = len(words_mean_2)

founded = False

users_word = input("please enter a word(without any space!): ")
is_over = False


def start_loop(user_s_word):
    """This loop goes into the word_mean list that includes dictionary of words and checks if the user's input is in the
    dictionary or not"""
    start_the_dictionary_loop = True
    global founded
    while start_the_dictionary_loop:
        for current_pos in range(len_words_mean_list):
            if user_s_word in words_mean[current_pos]:
                word = users_word
                mean = words_mean[current_pos][users_word]
                print(f"\nWord :{word}\nMeaning {mean}")
                founded = True
        for current_pos in range(len_words_mean_list_2):
            if user_s_word in words_mean_2[current_pos]:
                word = users_word
                mean = words_mean_2[current_pos][users_word]
                print(f"\nWord :{word}\nMeaning : {mean}")
                founded = True
        if not founded:
            print(f"The word {users_word} is not in the dictionary yet.")
        start_the_dictionary_loop = False


start_loop(users_word)

while not is_over:
    if input('do you want to continue("Yes"):').lower() == "yes":
        users_word = input("please enter a word(without any space!): ").lower()
        start_loop(users_word)
    else:
        is_over = True
        print("GoodBye （￣︶￣)↗　")




