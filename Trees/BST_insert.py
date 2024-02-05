class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinerySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        temp = new_node
        