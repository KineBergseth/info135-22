"""
Task 1.
a) Britannica English Dictionary: 18 steps - 171476 words
b) Indian Dictionary: 21 steps - 1100373 words
c) Japanese Dictionary: 18 steps - 260000 words


Task 2.
Write a class called School that has two following methods:
Method 1: __init__() that creates a string variable called student and initially sets it to “Sara”.
Method 2: print_hello() that prints a welcome message, e.g., “Hello!”
"""


class School:
    def __init__(self):
        self.student = "Sara"

    def print_hello(self):
        print('Hello!')


student = School()
student.print_hello()

"""
Task 3 
Given the following linked-list class, write a method called print_list() that loops over and prints the entire 
contents of a linked-list starting from head. 

"""


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next







import Stack


def reverse_list(input_list):
    s = Stack.Stack()
    rev_list = []

    for item in input_list:
        s.push(item)

    while not s.isEmpty():
        rev_list.append(s.pop())
    return rev_list


ll = [1, 2, 3]
print(reverse_list(ll))
