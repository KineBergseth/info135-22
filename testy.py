class Binarysearchtree:
    def __init__(self, value = None):
        self.value = value
        if self.value:
            self.left_child = Binarysearchtree()
            self.right_child = Binarysearchtree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = Binarysearchtree()
            self.right_child = Binarysearchtree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)

    def compute_sum(self):
        sum = sumRight = sumLeft = 0;

        # Check whether tree is empty
        if self.is_empty():
            print("Tree is empty")
            return 0
        else:
            # Calculate the sum of nodes present in left subtree
            if (self.left_child != None):
                sumLeft = self.left_child.compute_sum()

                # Calculate the sum of nodes present in right subtree
            if (self.right_child != None):
                sumRight = self.right_child.compute_sum()

                # Calculate the sum of all nodes by adding sumLeft, sumRight and root node's data
            sum = self.value + sumLeft + sumRight
        return sum


my_tree2 = Binarysearchtree()
my_tree2.insert(2)
my_tree2.insert(4)
my_tree2.insert(6)
my_tree2.insert(8)
my_tree2.insert(10)

print('Sum: ', my_tree2.compute_sum())
#print('Number of nodes : ', my_tree2.compute_count())