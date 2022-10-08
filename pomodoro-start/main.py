from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", foreground=GREEN)
    checkbox_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_in_sec = WORK_MIN * 60
    short_break_in_sec = SHORT_BREAK_MIN * 60
    long_break_in_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_in_sec)
        timer_label.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_in_sec)
        timer_label.config(text="Break", foreground=PINK)
    else:
        count_down(work_in_sec)
        timer_label.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    clock = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=clock)
    if count > 0:
        timer = screen.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkbox_label.config(text="✅"*(reps//2))


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, foreground=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkbox_label = Label(highlightthickness=0, foreground=GREEN, bg=YELLOW)
checkbox_label.grid(row=3, column=1)

screen.mainloop()
