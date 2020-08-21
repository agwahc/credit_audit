from creditz.db import dbk


class credit:
    def __init__(self, amount=0, who='', purpose='', mode='', typeT=''):
        self.amount = amount
        self.who = who
        self.purpose = purpose
        self.mode = mode
        self.typeT = typeT
        credit.store_credit(self)

    def store_credit(self):
        dbk.store_credit(self, self.amount, self.who, self.purpose, self.mode, self.typeT)
