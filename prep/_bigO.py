"""
The Big O notation for f(n) can be derived from the following simplification rules:

    - If f(n) is a sum of several terms, we keep only the one with largest growth rate.
        In order best to worst Big-O complexity: 1 < log n < n < n log n < n^2 < 2^n < n!
    - If f(n) is a product of several factors, any constant is omitted.

#http://web.mit.edu/16.070/www/lecture/big_o.pdf
"""



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

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


length = 5
for i in range(length):
    print(fibo(i))

def recur_factorial(n):
    if n == 1:
        return n
    return n * recur_factorial(n - 1)


# Testing with 5 = 5 * 4 * 3 * 2 * 1 = 120
print(f"5! = {recur_factorial(5)}")


def string_hash(key):
    hash_value = 1
    for char in key:
        hash_value *= ord(char)

    return hash_value


my_key = "hello"
hashed_key = string_hash(my_key)
print(f"{my_key} string hashed to {hashed_key}")
