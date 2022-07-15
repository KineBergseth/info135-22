class Account:
    def __init__(self, name, money): pass
    # FORSLAG TIL METODER MAN KAN IMPLEMENTERE
    # method to deposit money into account based on input value, and print relevant info
    def deposit_money(self): pass

    # method to withdraw money from account based on input value, and print relevant info
    def withdraw_money(self): pass

    # print current balance
    def display_balance(self): pass

    # sort bills from highest to lowest
    def sort_bills(self, bills): pass

    # pay a selected bill from the bill list if possible
    def pay_bill(self, bills): pass

    # pay all the bills if possible
    def pay_all_bills(self): pass

    # transfer money to saving account
    def transfer_money(self): pass

    # transfer money to another persons account
    def transfer_money_to_friend(self): pass

    # show transfer history
    def transfer_history(self): pass


# use inheritance to make other types of accounts
class SavingsAccount(Account):
    def __init__(self, name, money):
        super().__init__(name, money)

    # function ot calculate interest gained based on current balance
    def calculate_interest(self): pass


