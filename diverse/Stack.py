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


# reverse list with stack, using only is_empty, push, pop stack methods
def reverse_list(my_list):
    reversed_list = []
    s = Stack()
    for i in my_list:
        s.push(i)
    print(f"Current stack in original order: {s.items}")
    while not s.is_empty():
        reversed_list.append(s.pop())
    return f"reversed list: {reversed_list}"


if __name__ == "__main__":
    li = [1, 2, 3]
    print(reverse_list(li))
