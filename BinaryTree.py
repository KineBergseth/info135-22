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

    # in-order print
    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.value),
        if self.right_child:
            self.right_child.print_tree()

    def pretty_print(self, indent=0):
        if self.left_child:
            self.left_child.pretty_print(indent + 1)
        print(' ' * 4 * indent + '-> ' + self.value)
        if self.right_child:
            self.right_child.pretty_print(indent + 1)

    def invert_tree(self):
        self.left_child, self.right_child = self.right_child, self.left_child
        if self.right_child:
            self.right_child.invert_tree()
        if self.left_child:
            self.left_child.invert_tree()


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
tree.pretty_print()
tree.invert_tree()
tree.pretty_print()
