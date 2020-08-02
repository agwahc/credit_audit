import os

find = os.path.dirname(__file__)


def for_credit():
    return find + '/credit_db.txt'


def for_debit():
    return find + '/debit_db.txt'
