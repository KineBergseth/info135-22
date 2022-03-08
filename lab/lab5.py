"""
Task 1:

Joe has made his own minibank system that stores the amount of money he currently has, can be used to pay bills,
and can sort incoming bills from highest to lowest, only criteria is that you make a class with these functions.

Bonus points if you add other functions you would want in a personal minibank system. A way of adding money to the system
or pay a friend method, or a way of authentication maybe?
"""


class MiniBank:

    def __init__(self, money):
        self.money = money

    def deposit_money(self):
        amount = float(input("Enter amount of money you wish to deposit into your bank account: "))
        self.money += amount
        print(f"Money deposited: {amount} kr, Total balance: {self.money} kr")

    # method to withdraw money from account based on input value, and print relevant info
    def withdraw_money(self):
        amount = float(input("Enter amount of money you wish to withdraw from your bank account: "))
        if amount > self.money:
            print("Insufficient funds")
            return
        else:
            self.money -= amount
            print(f"Money withdrawn: {amount} kr, Total balance: {self.money} kr")

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
joe.deposit_money()
joe.withdraw_money()
"""
Task 2 fibonaci and O(n)
Fibonaci sequence is where one number is the sum of previous two numbers
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

a) Make a function that prints out this sequence. Try to be creative and not just googleing it
There is a ton of possible ways to do this:D
b) What is the O notation to your algorithm you think?
"""


"""
A recursive method for the fibonacci list, not effective at all is O(2^N)
To calculate F(n), the maximum depth of the call tree is n, and 
since each function call produces two additional function calls, the time complexity of this recursive function is O(2n)

Inside recur_fibo(), you first check the base case. 
You then return the sum of the values that results from calling the function with the two preceding values of n. 
The computation gets more and more expensive as n gets bigger. 
The required time grows exponentially because the function calculates many identical subproblems over and over again.
To calculate F(5), recur_fibo() has to call itself 15 times.

Generating the Fibonacci sequence is a classic recursive problem. Recursion is when a function refers to itself to 
break down the problem it’s trying to solve. In every function call, the problem becomes smaller until it reaches a 
base case, after which it will then return the result to each intermediate caller until it returns the final result 
back to the original caller. 

If you wanted to calculate the F(5) Fibonacci number, you’d need to calculate its predecessors, F(4) and F(3), 
first. And in order to calculate F(4) and F(3), you would need to calculate their predecessors. The breakdown of F(5) 
into smaller subproblems would look like this: 

F(5) = F(4) + F(3)
     = F(3) + F(2) + F(2) + F(1)
     = F(2) + F(1) + F(1) + F(0) + F(1) + F(0) + 1
     = F(1) + F(0) + 1 + 1 + 0 + 1 + 0 + 1
     = 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1
     = 5
     
Each time the Fibonacci function is called, it gets broken down into two smaller subproblems because that’s how you 
defined the recurrence relation. When it reaches the base case of either F(0) or F(1), it can finally return a result 
back to its caller. 

Do not try this function with a number greater than 50. Depending on your hardware,
you might be waiting for a long time before seeing the result—if you make it to the end.
"""
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


nterms = 5

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
