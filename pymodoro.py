from tkinter import *
import math

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

def reset_timer():
    '''Function responsible for resetting the program.'''
    window.after_cancel(timer)
    canvas.itemconfig(timer_countdown, text= "00:00")
    timer_label.config(text= "Timer", fg=GREEN)
    check_mark.config(text= "")
    global reps
    reps = 0

def start_timer():
    '''Function responsible for starting the countdown.'''
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break!", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break!", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work!", fg=GREEN)


def countdown(count):
    '''Function responsible for the countdown.'''

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Updates the timer text in canvas.
    canvas.itemconfig(timer_countdown, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

        # When you complete the time for work, a check mark is added to the GUI.
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_mark.config(text= marks)

# Window features.
window = Tk()
window.title("PyModoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0) # Window size

# Canvas features.
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_countdown = canvas.create_text(102, 130, text="00:00", fill="white", font= (FONT_NAME, 35, "bold")) # Timer
canvas.grid(column=1, row=1, pady=50)

# Title
timer_label = Label(text="Timer", font= (FONT_NAME, 30, "bold"), bg= YELLOW, fg= GREEN)
timer_label.grid(column=1, row=0, pady=20)

# Buttons
start_button = Button(text="Start", command= start_timer) # Start the countdown function.)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command= reset_timer)
reset_button.grid(column=2, row=2)

# Check mark.
check_mark = Label(text="", bg=YELLOW)
check_mark.grid(column=1, row=3)

# Keeps showing the window with GUI.
window.mainloop()