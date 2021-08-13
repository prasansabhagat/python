
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import * 
root = Tk()
root.title("Pomodoro")
root.geometry("400x400")
canvas = Canvas(width=200, height=200)
imagea = PhotoImage(file="pomodoro.jpg")
canvas.create_image(100, 100, image=imagea)
canvas.pack()
root.mainloop()
