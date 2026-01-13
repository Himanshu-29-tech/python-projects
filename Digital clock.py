#  first we upload TKINTER MODULE ===>> for graphical user interface
#  then we upload TIME MODULE ===>> for date and time

#  rooot windows for tkinter module
#  assign root title

#  write a function ==>> for update time and display
#   string function for time 

# coonfig string to label

# use after ==> for update and current time display


# make a label object and diiferent attributes for display your label

# used main loop methods




import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p\n%D')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(
    root,
    font=("calibri", 50, "bold"),
    background="yellow",
    foreground="black"
)

label.pack(anchor="center")

time()
root.mainloop()
