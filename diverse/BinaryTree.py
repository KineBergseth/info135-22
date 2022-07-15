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
