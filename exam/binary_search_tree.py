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

    def is_leaf(self):
        return self.left_child.is_empty() and self.right_child.is_empty()

    def make_empty(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def copy_child(self, child):
        if child == 'left':
            self.value = self.left_child.value
            self.right_child = self.left_child.right_child
            self.left_child = self.left_child.left_child
        elif child == 'right':
            self.value = self.right_child.value
            self.right_child = self.right_child.right_child
            self.left_child = self.right_child.left_child

    def in_order(self):
        if self.is_empty():
            return []
        else:
            self.left_child.in_order() + [self.value] + self.right_child.in_order()

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

    # A handy way of getting the minimum value in a BST as we know how values is stored we can just go left
    # until we reach the bottom and there we have the minimum value
    def get_min(self):
        minimum = self
        while minimum.left_child.value is not None:
            minimum = minimum.left_child
            print(minimum.value)
        print(minimum.value)

    # Same as minimum but here we go right instead
    def get_max(self):
        maximum = self
        while maximum.right_child.value is not None:
            maximum = maximum.right_child
        print(maximum.value)

    def count_nodes(self):
        if self.is_empty():
            return 0
        else:
            return self.left_child.count_nodes() + self.value + self.right_child.count_nodes()

    def calculate_values(self):
        if self.is_empty():
            return 0
        else:
            return self.left_child.count_nodes() + self.value + self.right_child.count_n

my_Bst = BinarySearchTree()
my_Bst.insert(3)
my_Bst.insert(1)
my_Bst.insert(4)
my_Bst.insert(2)
my_Bst.insert(5)
my_Bst.insert(-1)

print("Min: ")
my_Bst.get_min()
print("Max: ")
my_Bst.get_max()
