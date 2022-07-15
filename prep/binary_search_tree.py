class BinarySearchTree:

    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)

    def find(self, value):
        if self.is_empty():
            return False
        elif value == self.value:
            return True
        elif value < self.value:
            return self.left_child.find(value)
        elif value > self.value:
            return self.right_child.find(value)

    # if a node has no children, it is a leaf node
    def is_leaf(self):
        return self.left_child.is_empty() and self.right_child.is_empty()

    # different ways to traverse nodes, depending on root is read first, last or in between the children
    def in_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.in_order() + [self.value] + self.right_child.in_order()

    def pre_order(self):
        if self.is_empty():
            return []
        else:
            return [self.value] + self.left_child.pre_order() + self.right_child.pre_order()

    def post_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.post_order() + self.right_child.post_order() + [self.value]

    # in a BST we know how values is stored (since they are sorted) we can just go left until we reach the bottom
    # the minimum value is always in the leftmost position
    def get_min(self):
        minimum = self
        while minimum.left_child.value is not None:
            minimum = minimum.left_child
        return minimum.value

    # Same as minimum but here we go right instead to find maximum value
    def get_max(self):
        maximum = self
        while maximum.right_child.value is not None:
            maximum = maximum.right_child
        return maximum.value

    def count_nodes(self):  # count number of nodes in tree
        if self.is_empty():
            return 0
        else:
            # recursive traversal of all nodes, pre-order visit order
            # for all nodes we increase value by one and return sum when all computations are done
            return 1 + self.left_child.count_nodes() + self.right_child.count_nodes()

    def calculate_values(self):
        if self.is_empty():
            return 0
        else:
            # recursive traversal, return all values added with each other
            # for all nodes we find the value, add them to each other and return sum when it is done
            return self.left_child.calculate_values() + self.value + self.right_child.calculate_values()


my_Bst = BinarySearchTree()
my_Bst.insert(3)
my_Bst.insert(1)
my_Bst.insert(4)
my_Bst.insert(2)
my_Bst.insert(5)
my_Bst.insert(-1)

print(my_Bst.in_order())
print("Min: ")
print(my_Bst.get_min())
print("Max: ")
print(my_Bst.get_max())
print('number of nodes:')
print(my_Bst.count_nodes())
print('total value of nodes:')
print(my_Bst.calculate_values())
