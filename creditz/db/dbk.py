from datetime import datetime
from creditz.menu import *
import dir

access1 = {"date/time": " ", "amount": 0, "sender": " ", "purpose": " "}
access2 = {"date/time": " ", "amount": 0, "beneficiary": " ", "purpose": " "}


def call():  # returns data from db.txt to access
    o = int(input('Which? Credit OR Debit, 1 OR 2 : '))
    if o == 1:
        p = dir.for_credit()
        data = open(p, 'r')
        print(data.read())
        data.close()
    elif o == 2:
        p = dir.for_debit()
        data = open(p, 'r')
        print(data.read())
        data.close()
    else:
        print('Didn\'t work')
        select(1)
    menu()


def analyze():
    z = int(input('Show remaining money? Yes = 1 OR No = Any_key : '))
    if z == 1:
        import ast
        p = dir.for_credit()
        r = dir.for_debit()
        cal = 0
        rem = 0
        for i in open(p, 'r'):  # reading values of amount in credit_db to sum up to cal
            print(i)
            y = ast.literal_eval(i)
            x = y['amount']
            cal += x
        print('Your total credit amount : N{}'.format(cal))
        for b in open(r, 'r'):  # reading values of amount in debit_db to subtract from cal
            n = ast.literal_eval(b)
            m = n['amount']
            rem += m
        print('Your total debit amount : N{}'.format(rem))
        final = cal - rem
        if final < 0:
            final_fix = abs(final)
            print('Your remaining money amount : N{}, means you have spend N{} over-budget'.format(final,
                                                                                                  final_fix))  # gets absolute of remaining money
        else:
            print('Your remaining money amount : N{}'.format(final))
        return menu()
    else:
        return menu()


def store_debit(self, a, b, c):
    dt = datetime.now()
    d_t = dt.strftime('%d/%m/%Y %H:%M')
    access2["date/time"] = d_t
    access2["amount"] = a
    access2["beneficiary"] = b
    access2["purpose"] = c
    access2str = str(access2)
    d = open("debit_db.txt", "a")
    d.write(access2str)
    d.write('\n')
    d.close()
    menu()


def store_credit(self, a, b, c):
    dt = datetime.now()
    d_t = dt.strftime('%d/%m/%Y %H:%M')
    access1["date/time"] = d_t
    access1["amount"] = a
    access1["sender"] = b
    access1["purpose"] = c
    access2str = str(access1)
    d = open("credit_db.txt", "a")
    d.write(access2str)
    d.write('\n')
    d.close()
    menu()


def menu():
    select(self=1)
