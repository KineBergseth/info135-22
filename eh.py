# Oppgave 1
# a) 171476 > 85738 > 42869 > 21434 > 10717 > 5358 > 2679 >
#    1339 > 669 > 334 > 167 > 83 > 41 > 20 > 10 > 5 > 2 > 1
#    steps: 18
# b) steps: 21
# c) steps: 19


# Oppgave 2

class Student:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greeting(self):
        print(f' Hei! my name is {self.name}')
        print(f' I am {self.age} years old')
        print(f' I am from {self.country}')


student = Student("Sara", 25, "Norway")
student.greeting()


# Oppgave 3

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        list = self.head
        for element in list:
            print(element)


# Oppgave 4

class Stack:
    def __init__(self):
        self.items = []

    def reverse_list(self):
        print(reversed(self))


my_list = [1, 2, 3, 4, 5]
reverse_list(my_list)
