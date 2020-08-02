from creditz.db import dbk

class debit:
    amount = 0
    who = ""
    purpose = ""

    def entry_amount(self):
        try:
            self.amount = int(input("Enter debit amount: "))
        except:
            print("Not valid number!")
            debit.entry_amount(self)
        debit.entry_who(self)

    def entry_who(self):
        try:
            self.who = input("Enter name of receipient: ")
        finally:
            debit.entry_purpose(self)

    def entry_purpose(self):
        try:
            self.purpose = input("Enter purpose for transaction: ")
        finally:
            debit.store_debit(self)

    def store_debit(self):
        dbk.store_debit(self, a=self.amount, b=self.who, c=self.purpose)
