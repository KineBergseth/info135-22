"""
Task 1:

Joe has made his own minibank system that stores the amount of money he currently has, can be used to pay bills,
and can sort incoming bills from highest to lowest, only criteria is that you make a class with these functions.

Bonus points if you add other functions you would want in a personal minibank system. A way of adding money to the system
or pay afriend method, or a way of authentication maybe?
"""


class MiniBank:

    def __init__(self, money):
        self.money = money

    # Sorting method that uses merge sort as seen in lectures
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

    # Method that access the list and compares to a class variable money
    # Here there are alot of possible answers as long as your answer works correctly it is fine
    def pay_bill(self, bills):
        self.sort_bills(bills)
        i = 0
        while i != len(bills):
            if self.money < bills[i][1]:
                print("You cant pay the bill from", bills[i],
                      " With your current balance of: ", self.money)
                i += 1
            elif self.money >= bills[i][1]:
                self.money -= bills[i][1]
                print("we pay the bill to", bills[i], " which amount to: ", bills[i][1],
                      " Current balance: ", self.money)
                i += 1


# def put_in_Money(self, amount): maybe add a method so that you can put in money to the system?
# def pay_a_friend(self, amount, friend): Maybe you want to pay a friend or a specific person?


bills = [("Strøm", 1234), ("Leie", 5000), ("Wolfram alpha", 200), ("Velvære", 5000)]
joe = MiniBank(6000)
joe.sort_bills(bills)
print(bills)
joe.pay_bill(bills)

"""
Task 2 fibonaci and O(n)
Fibonaci sequence is where one number is the sum of previous two numbers
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

a) Make a function that prints out this sequence. Try to be creative and not just googleing it
There is a ton of possible ways to do this:D
b) What is the O notation to your algorithm you think?
"""


# A recursive method for the fibonacci list, not effective at all is O(2^N)
# Would be better if we could let this method have some sort of way of remembering....
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


nterms = 7

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))

"""
Task 3

What do these functions print

Ask your sem for hints
"""

# A
N = 15

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j - 1) == i):
            print('*', end='')
        else:
            print(' ', end='')
    print('')


# B
def a_space_classic(n):
    z = n - 1
    x = 1
    for i in range(0, n):
        for i in range(0, z):
            print(' ', end='')
        for i in range(0, x):
            print('+', end='')
        for i in range(0, z):
            print(' ', end='')
        x = x + 2
        z = z - 1
        print()


a_space_classic(5)
