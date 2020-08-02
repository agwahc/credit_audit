import tkinter as tk
from tkinter import ttk
from creditz.credit import *
from creditz.debit import *
from creditz import summary as sum


def select(self):
    a = 0
    try:
        a = int(input('Credit OR Debit OR Summary OR View_Remaining_funds OR Exit (1 OR 2 OR 3 OR 4 OR Any_key)? : '))
        if a == 1:
            start_credit(self)
        elif a == 2:
            start_debit(self)
        elif a == 3:
            sum.get()
        elif a == 4:
            sum.balance()
        else:
            exit()
    except:
        select(self)


def exit(self):
    return None


def start_credit(self):
    credit.entry_amount()


def start_debit(self):
    debit.entry_amount()

