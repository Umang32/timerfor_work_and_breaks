from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#9ea2ab"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text = "Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps = 0
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(long_break_sec)
        label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="WORK", fg=GREEN)




#
# def start_timer():
#     count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_Sec = count % 60
    if count_Sec < 10:
        count_Sec = f"0{count_Sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_Sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_marks.cnfig(text=marks)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Break Time")
window.config(padx=100, pady=50, bg=GREY)




canvas = Canvas(width=200, height=224, bg=GREY, highlightthickness = 0)
tomato_img = PhotoImage(file= "monster.png")
canvas.create_image(100,112,  image = tomato_img)

label = Label(text = "Timer", font=(FONT_NAME, 35, "bold"), bg=GREY)
label.grid(column=2, row=1)

timer_text = canvas.create_text(100, 112, text="00:00", fill="purple", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=2, row=2)


button_start = Button(text="Calculate", highlightthickness = 0, command= start_timer)
button_start.grid(column=1, row=3)




button_reset = Button(text="reset", highlightthickness = 0, command = reset_timer)
button_reset.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=3)
window.mainloop()