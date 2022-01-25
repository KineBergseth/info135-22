class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() <= 0


def reverse_list(stack, my_list):
    for i in range(len(my_list)):
        stack.push(i)
    print(stack.items)
    while not stack.is_empty():
        print(stack.pop())

# print(reverse_list())

li = [1, 2, 3]
s = Stack()
print(reverse_list(s, li))

# def reverse_list(input_list):
#     s = Stack.Stack()
#     rev_list = []
#
#     for item in input_list:
#         s.push(item)
#
#     while not s.isEmpty():
#         rev_list.append(s.pop())
#     return rev_list
#
#
# test_list = [1, 2, 3, 4, 5, 6]
# n_list = reverse_list(test_list)
# print(n_list)