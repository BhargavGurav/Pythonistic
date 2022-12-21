from datetime import *
from tkinter import *

root = Tk()
root.title("Bhargav's Digital Clock")
def show():
    x = datetime.now()
    y = f"{x.strftime('%d')}/{x.strftime('%m')}/{x.strftime('%Y')} {x.strftime('%A')}\n{x.strftime('%X')} "
    clock_label.config(text=y)
    clock_label.after(1000, show)


clock_label = Label(root, fg='green', bg='black', font=('Algerian', 40, 'bold'))
clock_label.pack()
show()
root.mainloop()
