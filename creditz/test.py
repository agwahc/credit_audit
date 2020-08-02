import tkinter as tk
from tkinter import ttk
import os
import sys
import ast

'''
app = tk.Tk()
app.title('CREDIT$')
label = ttk.Label(app, text='CREDIT$ BEGIN')
label.grid(column=0, row=0)


def click():
    label.configure(text='FLUID')


action = ttk.Button(app, text='START!', command=click())
action.grid(column=1, row=0)

if __name__ == '__main__':
    app.mainloop()
'''

#find = os.path.dirname(__file__)
#print(find)

z = ast.literal_eval("{'date/time': '28/07/2020 20:54', 'amount': 5000, 'beneficiary': 'Azotani', 'purpose': 'Lens'}")
x = z['amount']
print(x)