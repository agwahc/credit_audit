from creditz.db import dbk

class credit:
    amount = 0
    who = ""
    purpose = ""

    def entry_amount(self):
        try:
            self.amount = int(input("Enter credit amount: "))
        except:
            print("Not valid number!")
            credit.entry_amount(self)
        credit.entry_who(self)

    def entry_who(self):
        try:
            self.who = input("Enter source of fund: ")
        finally:
            credit.entry_purpose(self)

    def entry_purpose(self):
        try:
            self.purpose = input("Enter purpose for transaction: ")
        finally:
            credit.store_credit(self)

    def store_credit(self):
        dbk.store_credit(self, self.amount, self.who, self.purpose)