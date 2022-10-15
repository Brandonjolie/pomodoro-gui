from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer")
    checks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    work_sec = WORK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    if reps % 8 == 0:
        heading.config(text="Long Break")
        countdown(long_sec)
        reps += 1
    elif reps % 2 == 0:
        heading.config(text="Short Break")
        countdown(short_sec)
        reps += 1
    else:
        heading.config(text="Work")
        countdown(work_sec)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(num):
    mins = str(int(num / 60)).rjust(2, "0")
    secs = str(num % 60).rjust(2, "0")
    if num >= 0:
        global timer
        timer = window.after(1000, countdown, num - 1)
        canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    else:
        start()
        _tex = ""
        for _ in range(int(reps / 2)):
            _tex += "✓"
        checks.config(text=_tex)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


heading = Label(text="Timer", font=("Arial", 35), fg=GREEN, bg=YELLOW)
heading.grid(column=1, row=0)

checks = Label(font=("Arial", 20), fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)


window.mainloop()
