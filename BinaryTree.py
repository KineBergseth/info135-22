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
