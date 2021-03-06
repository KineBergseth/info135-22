"""
INFO135 - Lab 1
Note that this is simply a suggestion of how to solve the tasks,
there will be many other valid solutions!
"""


# CLASSES
# Exercise 1
class Person:

    def __init__(self, name):
        self.name = name

    def greets(self, person):
        print(f"Hello, {person.name}!")


alice = Person('Alice')
bob = Person('Bob')

alice.greets(bob)

print()


# Exercise 2
class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = 10000

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def print_email(self):
        print(f"{self.firstname}.{self.lastname}@company.com")

    def increase_salary(self, rate):
        self.salary *= rate


gunnar = Employee('Gunnar', 'Hansen')
lars = Employee('Lars', 'Nilsen')
print(gunnar.get_fullname())
gunnar.print_email()
print(f'gunnar salary:  {gunnar.salary}')
gunnar.increase_salary(6)
print('gunnar new salary: ', gunnar.salary)

print()

# BINARY SEARCH
# Exercise 1
# a) 1, 3, 5

# Exercise 2
import math


def binary_search_big_o(input_list):
    return math.ceil(math.log(len(input_list), 2))


def simple_search_big_o(input_list):
    return len(input_list)


# Testing the functions with a list containing 964 elements
my_list = [x for x in range(964)]  # list comprehension

# kan skrive det samme på denne måten også
my_list2 = []
for x in range(964):
    my_list2.append(x)

print("Simple search big O:", simple_search_big_o(my_list)) # O1 best case| O n worst case
print("Binary search big O:", binary_search_big_o(my_list)) # O1 best case| O LOG n worst case
print()


# Extra task
# 4. n^2, for every element in the list the function iterates over the list again, therefore using n * n = n^2 steps


# Extra task 2

class reverseWordOrder:
    def reverse_words(self, string):
        # split the string on spaces
        words = string.split()
        # reverse order with reversed() function
        reversed_words = reversed(words)
        # join the reversed words back to a string and return them
        return ' '.join(reversed_words)


reverse = reverseWordOrder()
print(reverse.reverse_words('hello world'))  # Expected Output : 'world hello'
print(reverse.reverse_words('I really love python'))  # Expected Output : 'python love really I'
