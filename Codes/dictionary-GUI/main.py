from tkinter import Tk, Canvas, Button, Entry, PhotoImage
import pandas
import pyperclip

data = pandas.read_csv("dictionary_data.csv")
dictionary = data.set_index('word')['meaning'].to_dict()

about_content = "\n● English-To-English-Dictionary\n" \
                "I made this English to English dictionary\nas a hobby project.\n" \
                "It’s got a bunch of words and definitions in it," \
                " so you can learn new stuff\nand sound smarter when you talk.\n" \
                "It’s super easy to use\njust type in the word you want and boom!\n" \
                "You get the definition.\n" \
                "It’s great for students,\nprofessionals,\nor anyone\n" \
                "who wants to learn new words\nand impress their friends.\n\n" \
                "My Telegram ID:@ichbinaydinq"


def about():
    canvas2.itemconfig(answer_to_search, text=about_content, font=("consolas", 11, "normal"))


def copy():
    global for_copy
    if canvas2.itemcget(answer_to_search, "text") == about_content:
        pyperclip.copy(about_content)
    else:
        pyperclip.copy(for_copy)


def search_answer(event=None):
    global for_copy
    user_s_word = search_entry.get()
    if len(user_s_word) > 45:
        canvas2.itemconfig(answer_to_search, text="Hey, that's more than 45 characters!", font=("consolas", 14, "normal"))
        for_copy = ""
    else:
        word = user_s_word.lower() if user_s_word.lower() in dictionary else user_s_word.title()
        if word in dictionary:
            mean = dictionary[word]
            font_size = 12 if len(mean) > 200 else 11 if len(mean) > 500 else 14
            canvas2.itemconfig(answer_to_search, text=f"\nWord :{word.title()}\nMeaning {mean}", font=("consolas", font_size, "normal"))
            for_copy = f"\nWord :{word.title()}\nMeaning {mean}"
        elif word == "" :
            canvas2.itemconfig(answer_to_search, text="", font=("consolas", 14, "normal"))
            for_copy = ""

        else:
            canvas2.itemconfig(answer_to_search, text=f"""The word "{user_s_word}" is not in program's dictionary yet.""", font=("consolas", 14, "normal"))
            for_copy = ""


def round_button(widget):
    widget.bind("<Enter>", lambda event: widget.config(bg="#f9f900"))
    widget.bind("<Leave>", lambda event: widget.config(bg="#fff200"))


window = Tk()
window.title("Dict v3.30")
window.config(padx=50, pady=50, bg="#3f48cc")

canvas1 = Canvas(height=30, width=300, bg="#3f48cc", highlightthickness=0)
search_box = PhotoImage(file="images/search_box.png")
canvas1.create_image(190, 20, image=search_box)
canvas1.grid(column=0, row=0, columnspan=1)

search_entry = Entry(width=45)
search_entry.grid(column=0, row=1, columnspan=2)
search_entry.focus()
search_entry.bind('<KeyRelease>', search_answer)

about_button = Button(text="About", width=10, bg="#fff200", command=about)
about_button.grid(column=1, row=0)
round_button(about_button)

copy_button = Button(text="Copy", width=10, bg="#fff200", command=copy)
copy_button.grid(column=1, row=1)
round_button(copy_button)

canvas2 = Canvas(width=639.4, height=361, highlightthickness=0)
background_img = PhotoImage(file="images/background.png")
canvas2.create_image(320, 180, image=background_img)
answer_to_search = canvas2.create_text(320, 180, text="Welcome to\n Dict.", width=500, font=("consolas", 24, "bold"), fill="black")
canvas2.grid(column=0, row=4, columnspan=2)

window.mainloop()
