from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
timer = None


# ---------------------------------- READ WORDS FORM CSV --------------------------------- #
try:
    words_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_df = pd.read_csv("data/french_words.csv")
finally:
    words_dict = words_df.to_dict(orient="records")


# ---------------------------------- NEXT CARD --------------------------------- #
def next_card():
    global current_card, timer
    screen.after_cancel(timer)
    canvas.itemconfigure(card_image, image=front_image)
    current_card = random.choice(words_dict)
    french_word = current_card["French"]
    canvas.itemconfigure(card_title, text="French", fill="black")
    canvas.itemconfigure(card_word, text=french_word, fill="black")
    timer = screen.after(3000, func=flip_card)


# ------------------------------- KNOWN CARD REMOVAL ---------------------------- #
def is_known():
    words_dict.remove(current_card)
    to_learn_df = pd.DataFrame(words_dict)
    to_learn_df.to_csv(path_or_buf="data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------------- FLIP CARD --------------------------------- #
def flip_card():
    global current_card, timer
    english_word = current_card["English"]
    canvas.itemconfigure(card_image, image=back_image)
    canvas.itemconfigure(card_title, text="English", fill="white")
    canvas.itemconfigure(card_word, text=english_word, fill="white")


# ---------------------------------- UI SETUP ----------------------------------- #
screen = Tk()
screen.title("Flashy")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

timer = screen.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

screen.mainloop()
