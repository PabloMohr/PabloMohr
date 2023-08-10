from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
current_card = {}
to_learn = {}
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, time
    window.after_cancel(time)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    time = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    next_card()
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index=False)

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(405, 266, image=front_img)
canvas.grid(column=0, row=0, columnspan= 2)
card_title = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))

check_image = PhotoImage(file="./images/right.png")
cross_image = PhotoImage(file="./images/wrong.png")

check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(column=0, row=1)

cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=1, row=1)

time = window.after(3000, flip_card)
next_card()

window.mainloop()