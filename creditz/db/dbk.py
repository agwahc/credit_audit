from datetime import datetime
from creditz.source import *
import dir
import ast
import pandas as pd

access1 = {'Type': ' ', 'date/time': " ", 'amount': 0, 'sender': " ", 'purpose': " ", 'method': ' '}
table = {}


def call_part():  # returns data from db.txt
    o = dir.file('/db.txt')
    z = open(o, 'r')
    for i in z:
        f = ast.literal_eval(i)
        if f['Type'] == 'CREDIT':
            table['CREDIT'] = table.get('CREDIT', []) + [f['amount']]
            table['RECP'] = table.get('RECP', []) + [f['sender']]
            table['METHOD'] = table.get('METHOD', []) + [f['method']]
            table['DEBIT'] = table.get('DEBIT', []) + ['-']
            table['DATE/TIME'] = table.get('DATE/TIME', []) + [f['date/time']]
        elif f['Type'] == 'DEBIT':
            table['DEBIT'] = table.get('DEBIT', []) + [f['amount']]
            table['CREDIT'] = table.get('CREDIT', []) + ['-']
            table['RECP'] = table.get('RECP', []) + [f['sender']]
            table['METHOD'] = table.get('METHOD', []) + [f['method']]
            table['DATE/TIME'] = table.get('DATE/TIME', []) + [f['date/time']]
    report = pd.DataFrame(table)
    table.clear()
    return str(report)


def analyze():
    # z = int(input('Show remaining money? Yes = 1 OR No = Any_key : '))
    # if z == 1:
    p = dir.file('/db.txt')
    z = open(p, 'r')
    cal = 0
    rem = 0
    for i in z:  # reading values of amount in db to sum up to cal
        y = ast.literal_eval(i)
        if y['Type'] == 'CREDIT':
            x = int(y['amount'])
            cal += x
        elif y['Type'] == 'DEBIT':
            m = int(y['amount'])
            rem += m
    statement_cre = 'Your total credit amount : N{}'.format(cal)
    statement_deb = 'Your total debit amount : N{}'.format(rem)
    final = cal - rem
    if final < 0:
        final_fix = abs(final)
        statement_err = 'Your balance is: N{}, means you have spend N{} over-budget'.format(final,
                                                                                               final_fix)  # gets absolute of remaining money
        statement_tol = 0
    else:
        statement_err = 0
        statement_tol = 'Your balance is: N{}'.format(final)
    x = [statement_cre, statement_deb, statement_tol, statement_err]
    z.close()
    return x


def store_credit(self, a, b, c, m, t):
    dt = datetime.now()
    d_t = dt.strftime('%d/%m/%Y %H:%M')
    access1['date/time'] = d_t
    access1['amount'] = a
    access1['sender'] = b
    access1['purpose'] = c
    access1['method'] = m
    access1['Type'] = t
    access1str = str(access1)
    d = open("db.txt", "a")
    d.write(access1str)
    d.write('\n')
    d.close()