from tkinter import *
from tkinter.ttk import *
from time import strftime
main=Tk()
main.title("Digital Clock")
def clock():
  tick = strftime("%H:%M:%S %P")
  label.config(text=tick)
  label.after(1000,clock)
label=Label(main,font=("sams",60),background="blue",foreground="black")
label.pack(anchor="center")
clock()
mainloop()
