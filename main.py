from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
count=5
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
# def reset_timer():
#     canvas.itemconfig(timer_text, text=f"00:00")
#     count_down()
#     start_timer()
# trigger reset_timer:
#1. stop previous timer
#2. set timer_text to "00:00"
def reset_timer():
    #if wouldn't have written reps as global variable, then even after assigning
    #reps=0, reps value wouldn't have changed because, this reps will be local
    #variable
    global reps
    reps=0
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    print(f"the reps is {reps}")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    print(reps)
    # if reps == 8:
    #     count_down(5 * 60)
    # elif reps%2==1:
    #     count_down(2*60)
    # elif reps%2==0:
    #     count_down(1*60)
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    #iF IT'S THE 1ST/3RD/5TH/7TH REP:
    if reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)

    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


    #count_down(2*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
#I couldn't use count_down function in button command because if I will write
# command=count_down, it will cause error because it expect a positional argument
# we don't have any option except, if we call some different function
#eg. command=start_timer, then when I will press button, this function will be called
# which will call count_down(5).

def count_down(count):
    # if count % 60<10:
    #     canvas.itemconfig(timer_text, text=f"0{int(count/60)}:0{count%60}")
    # else:
    #     canvas.itemconfig(timer_text, text=f"0{int(count / 60)}:{count % 60}")
    count_min=math.floor(count/60)
    count_sec=count%60
    # if count_sec==0 and count_min==0:
    #     start_timer()

    if count_sec<10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")


    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
            # I have used global check because if I would have taken check=""
            # each time this else triggered check again become empty
            # so this problem could be solved by using global which will fetch
            # 1st value as global constant which will be empty after that it will
            # keep updating check which is global constant
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✔"
        check_marks.config(text=mark)





# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("pomodoro")
windows.config(padx=100, pady=100, bg=YELLOW)



title_label=Label(text="Timer", font=(FONT_NAME,35,"bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=canvas_img)
canvas.grid(row=1,column=1)
timer_text=canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))





start_button=Button(text="Start", fg="Black", font=(FONT_NAME,18,"bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button=Button(text="Reset", fg="Black", font=(FONT_NAME,18,"bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks=Label(text="", bg=YELLOW, fg="green", font=(FONT_NAME,14,"bold"))
check_marks.grid(row=3, column=1)













windows.mainloop()