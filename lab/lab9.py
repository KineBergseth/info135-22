"""
Exercise 1
    a) H A D E C B G F
    b) D A E H C G B F
    c) D E A G F B C H
"""

# Exercise 2
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        # If the current node does not have a left child, we just create a new node and set it to the current node’s
        # left_child.
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        # If it does have the left child, we create a new node and put it in the current left child’s place. Allocate
        # this left child node to the new node’s left child.
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    """
    In-order print of binary tree
    Recursively traverse its left subtree. When this step is finished, we are back at n again.
    Process n itself.
    Recursively traverse its right subtree. When this step is finished, we are back at n again. 
    """
    def print_in_order(self):
        if self.left_child:
            self.left_child.print_in_order()
        print(self.value, end=" ")
        if self.right_child:
            self.right_child.print_in_order()

    def print_pre(self):
        print(self.value, end=" ")
        if self.left_child:
            self.left_child.print_pre()
        if self.right_child:
            self.right_child.print_pre()

    def print_post(self):
        if self.left_child:
            self.left_child.print_post()
        if self.right_child:
            self.right_child.print_post()
        print(self.value, end=" ")


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



tree = build_my_tree() # lag tre og sett inn data

# dette er en statisk og dårlig måte å printe ting ut på
print(f"Level 0:\t\t   {tree.value}")
print(f"Level 1:\t{tree.left_child.value}\t\t\t{tree.right_child.value}")
print(f"Level 2: "
      f"{tree.left_child.left_child.value}\t"
      f"\t{tree.left_child.right_child.value}\t"
      f"\t\t{tree.right_child.right_child.value}")
print(f"Level 3: "
      f"\t\t\t\t{tree.right_child.right_child.left_child.value}\t"
      f"\t{tree.right_child.right_child.right_child.value}\t")

print()

# ulike rekkefølger man kan printe i
print('pre-order:')
tree.print_pre()
print('\n in-order:')
tree.print_in_order()
print('\n post-order')
tree.print_post()


# pretty print med in-order rekkefølge
# Her bruker jeg en level parameter for å gi indentering for å representere nivåer
def printTree(node, level=0):
    if node is not None:
        printTree(node.left_child, level + 1)
        print(' ' * 4 * level + '-> ' + node.value)
        printTree(node.right_child, level + 1)


print('\n\n')
printTree(tree)

print('')


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

    # A handy way of getting the minimum value in a BST as we know how values is stored we can just go left
    # until we reach the bottom and there we have the minimum value
    def get_min(self):
        minimum = self
        while minimum.left_child.value is not None:
            minimum = minimum.left_child

        print(minimum.value)

    # Same as minimum but here we go right instead
    def get_max(self):
        maximum = self
        while maximum.right_child.value is not None:
            maximum = maximum.right_child

        print(maximum.value)


my_Bst = BinarySearchTree()
my_Bst.insert(3)
my_Bst.insert(1)
my_Bst.insert(4)
my_Bst.insert(2)
my_Bst.insert(5)
my_Bst.insert(-1)

my_Bst.in_order()
print("Min: ")
my_Bst.get_min()
print("Max: ")
my_Bst.get_max()

"""
Exercise 4 

The answer is n^4, as that is the term with the largest growth rate so we remove all other terms than 9n^4. 
(n^4 er polynomial, log n er logarithmic. the polynomial term has bigger growth)
Then since 9n^4 does not grow dependent on 9, and 9 is a constant we can remove it. Then we are left with n^4 

"""
