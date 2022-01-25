# Solution Suggestion for Lab 2 Exercises
# Linked Lists

# a)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# b)
node1 = Node('First node')
node2 = Node('Second node')
node3 = Node('Third node')

node1.next = node2
node2.next = node3


# c)
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        """
        add node at end of linked list
        :param new_data: value of item we want to insert
        """
        new_node = Node(new_data)
        # Check if list is empty
        if self.head is None:
            self.head = new_node
            return

        node = self.head  # node stores start node
        # iterate through list to find last item
        # terminates when last node is found
        while node.next:
            node = node.next
        # set reference of the last node to be our new node
        node.next = new_node

    # add node to the beginning of linked list
    def add_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


# add nodes to linked list
my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add_at_beginning(0)

# print elements from list
print(my_list.head.data)
print(my_list.head.next.data)
print(my_list.head.next.next.data)
print(my_list.head.next.next.next.data)
