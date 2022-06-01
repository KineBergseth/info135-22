from BinaryTree import BinaryTree


def build_my_tree():
    my_tree = BinaryTree("H")
    my_tree.insert_left("A")
    my_tree.insert_right("C")

    my_tree.left_child.insert_left("D")
    my_tree.left_child.insert_right("E")

    my_tree.right_child.insert_right("B")

    my_tree.right_child.right_child.insert_left("G")
    my_tree.right_child.right_child.insert_right("F")

    return my_tree


tree = build_my_tree()
print(f"Level 0:\t\t   {tree.value}")
print(f"Level 1:\t{tree.left_child.value}\t\t\t{tree.right_child.value}")
print(f"Level 2: "
      f"{tree.left_child.left_child.value}\t"
      f"\t{tree.left_child.right_child.value}\t"
      f"\t\t{tree.right_child.right_child.value}")
print(f"Level 3: "
      f"\t\t\t\t{tree.right_child.right_child.left_child.value}\t"
      f"\t{tree.right_child.right_child.right_child.value}\t")

# in order print
print(tree.print_tree())


# Exercise 3 BST from lecture, see bottom functions
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

"""
Exercise 4 

The answer is n^4, as that is the term with the largest growth rate so we remove all other terms than n^4/9. 
Then since 9n^4 does not grow dependent on 9 and 9 is a constant we can remove it. Then we are left with n^4 
"""
