class Account:

    def __init__(self, name, money):
        self.name = name
        self.balance = money
        self.transaction_history = []

    # method to deposit money into account based on input value, and print relevant info
    def deposit_money(self):
        amount = float(input("Enter amount of money you wish to deposit into your bank account: "))
        self.balance += amount
        print(f"Money deposited: {amount} kr, Total balance: {self.balance} kr")
        self.add_transaction_to_history("deposited", amount, "DEBIT")

    # method to withdraw money from account based on input value, and print relevant info
    def withdraw_money(self):
        amount = float(input("Enter amount of money you wish to withdraw from your bank account: "))
        if amount > self.balance:
            print("Insufficient funds")
            return
        else:
            self.balance -= amount
            print(f"Money withdrawn: {amount} kr, Total balance: {self.balance} kr")
            self.add_transaction_to_history("withdrawn", amount, "CREDIT")

    # print current balance
    def display_balance(self):
        print(f"Current balance is: {self.balance}")

    # sort bills from highest to lowest with merge sort
    def sort_bills(self, bills):
        if len(bills) > 1:
            mid = len(bills) // 2
            left = bills[:mid]
            right = bills[mid:]
            self.sort_bills(left)
            self.sort_bills(right)
            i = j = k = 0
            while i < len(left) and j < len(right):

                if left[i][1] > right[j][1]:
                    bills[k] = left[i]
                    i += 1
                else:
                    bills[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                bills[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                bills[k] = right[j]
                j += 1
                k += 1

    # pay a selected bill from the bill list if possible
    def pay_bill(self, bills):
        print(self.sort_bills(bill_list))
        bill = int(input("Enter the index of the bill you want to pay: "))
        if self.balance < bills[bill][1]:
            print(f"Insufficient funds")
            return
        else:
            self.balance -= bills[bill][1]
            print(f"You have payed the bill from {bills[bill][0]} at the price of {bills[bill][1]} kr")
            self.display_balance()
            self.add_transaction_to_history(bills[bill][0], bills[bill][1], "CREDIT")

    # pay all the bills if possible, starting with the highest one
    def pay_all_bills(self):
        self.sort_bills(bill_list)
        for index, tuple in enumerate(bill_list):
            if self.balance < tuple[1]:
                print(f"Insufficient funds, cannot pay the bill from {tuple[0]}")
                return
            else:
                self.balance -= tuple[1]
                print(f"You have payed the bill for {tuple[0]} at the price of {tuple[1]} kr")
                self.display_balance()
                self.add_transaction_to_history(tuple[0], tuple[1], "CREDIT")
                # If all bills are payed, inform the client of so
                if index == len(bill_list) - 1:
                    print("All the bills are payed")

    # transfer money to another persons account
    def transfer_money_to_friend(self, individual):
        amount = float(input(f"Enter amount of money you wish to transfer to {individual.name}: "))
        if self.balance < amount:
            print(f"Insufficient funds, cannot transfer money to {individual.name}")
        else:
            self.balance -= amount
            individual.balance += amount
            print(f"{self.name} has transferred {amount} kr to {individual.name}")
            self.add_transaction_to_history(individual.name, amount, "CREDIT")

    # helper function, adds transaction to history
    def add_transaction_to_history(self, recipient, amount, inout):
        self.transaction_history.insert(0, (recipient, amount, inout))

    # show transfer history
    def print_transaction_history(self):
        print("TRANSACTION HISTORY: ")
        for source, amount, inout in self.transaction_history:
            print(f"Source: {source}, Amount in kr: {amount}, {inout}")


class SavingsAccount(Account):
    def __init__(self, name, money):
        super().__init__(name, money)

    def calculate_interest(self):
        interest = self.balance * 0.05
        print(f"Calculated interest gain for the year based on the current balance is {interest} kr")

if __name__ == "__main__":
    bill_list = [("Strøm", 1234), ("Leie", 5000), ("Wolfram alpha", 200), ("Velvære", 5000)]
    joe = Account("Joe", 1000)
    sara = Account("Sara", 1000)
    # joe.sort_bills(bill_list)
    print(bill_list)
    joe.deposit_money()
    joe.withdraw_money()
    joe.pay_all_bills()
    joe.transfer_money_to_friend(sara)
    print()
    print(joe.print_transaction_history())

    print()
    print("Joe's savings account: ")
    joeS = SavingsAccount("Joe", 3000)
    joeS.display_balance()
    joeS.calculate_interest()
