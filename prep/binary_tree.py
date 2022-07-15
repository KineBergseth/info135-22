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

    def pre_order_print(self):
        """
        Visit nodes in this order: Root, Left, Right
        Algorithm Preorder(tree):
           1. Visit the root.
           2. Traverse the left subtree, i.e., call Preorder(left-subtree)
           3. Traverse the right subtree, i.e., call Preorder(right-subtree)
        """
        print(self.value)  # print value to node
        if self.left_child:
            self.left_child.pre_order_print()  # recursion on left child
        if self.right_child:
            self.right_child.pre_order_print()  # recursion on right child

    def in_order_print(self):
        """
        Visit nodes in this order: Left, Root, Right
        Algorithm Inorder(tree):
           1. Traverse the left subtree, i.e., call Inorder(left-subtree)
           2. Visit the root.
           3. Traverse the right subtree, i.e., call Inorder(right-subtree)
        """
        if self.left_child:
            self.left_child.in_order_print()  # recursion on left child
        print(self.value)  # print value to node
        if self.right_child:
            self.right_child.in_order_print()  # recursion on right child

    def post_order_print(self):
        """
        Visit nodes in this order: Left, Right, Root
        Algorithm Postorder(tree)
           1. Traverse the left subtree, i.e., call Postorder(left-subtree)
           2. Traverse the right subtree, i.e., call Postorder(right-subtree)
           3. Visit the root.
        """
        if self.left_child:
            self.left_child.post_order_print()  # recursion on left child
        if self.right_child:
            self.right_child.post_order_print()  # recursion on right child
        print(self.value)  # print value to node

    def pretty_print(self, indent=0):
        # A prettier way to print a tree, with indents representing levels. modified in order traversal
        if self.left_child:
            self.left_child.pretty_print(indent + 1)
        print(' ' * 4 * indent + '-> ' + self.value)
        if self.right_child:
            self.right_child.pretty_print(indent + 1)

    def invert_tree(self):
        """
        Method that inverts/mirrors the tree. (speilvendt)
        Modified preorder traversal, but instead of printing the node, we make the left and right child swap places
        :return:
        """
        self.left_child, self.right_child = self.right_child, self.left_child
        if self.right_child:
            self.right_child.invert_tree()
        if self.left_child:
            self.left_child.invert_tree()


def build_my_tree():  # function to create tree object and insert nodes
    my_tree = BinaryTree("H")
    my_tree.insert_left("A")
    my_tree.insert_right("C")

    my_tree.left_child.insert_left("D")
    my_tree.left_child.insert_right("E")
    my_tree.right_child.insert_right("B")

    my_tree.right_child.right_child.insert_left("G")
    my_tree.right_child.right_child.insert_right("F")

    return my_tree


def main():
    tree = build_my_tree()  # create tree and insert nodes

    # different ways to print tree
    print('Preorder traversal')
    tree.pre_order_print()
    print('Inorder traversal')
    tree.in_order_print()
    print('Postorder traversal')
    tree.post_order_print()

    # print nodes one by one. Not dynamic, so if the tree content changes, it will not print everything.
    # er også tungvindt å skrive alle nodene ut på denne måten. Rekursiv traversering er mye bedre og enklere
    print('static print:')
    print(f"root:{tree.value}")
    print(f"Level 1: {tree.left_child.value}\t{tree.right_child.value}")

    print('pretty print:')
    tree.pretty_print()

    tree.invert_tree()  # invert tree. left and right nodes switch places

    # tree is now mirrored/reversed. print again to check
    print('reversed tree pretty print:')
    tree.pretty_print()


if __name__ == '__main__':
    main()
