from creditz import menu
import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title('CREDIT$')
label = ttk.Label(app, text='CREDIT$ BEGIN')
label.grid(column=0, row=0)


def start():
    label.configure(text='Started')
    menu.select(1)


def end():
    exit()


action1 = ttk.Button(app, text='START!', command=start())
action1.grid(column=1, row=0)

action2 = ttk.Button(app, text='END', command=end())
action2.grid(column=1, row=1)

if __name__ == '__main__':
    app.mainloop()
