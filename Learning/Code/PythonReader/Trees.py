class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insertLeft(self, data):
        self.left = BinaryTree(data)

    def insertRight(self, data):
        self.right = BinaryTree(data)

#Ordering Using Recursion
def preorder(tree):
    if tree == None:
        return
    print(tree.data)
    preorder(tree.left)
    preorder(tree.right)

def inorder(tree):
    if tree == None:
        return
    inorder(tree.left)
    print(tree.data)
    inorder(tree.right)

def postorder(tree):
    if tree == None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.data)

def bfs(tree):
    queue = Queue()
    queue.put(tree)

    while not queue.empty():
        current = queue.get()
        print(current.data)

        if current.left:
            queue.put(current.left)
        if current.right:
            queue.put(current.right)

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data and self.left:
            self.left.insert(data)
        elif data <= self.data:
            self.left = BST(data)
        elif data > self.data and self.right:
            self.right.insert(data)
        else:
            self.right = BST(data)

    def find(self, data):
        if data < self.data and self.left:
            return self.left.find(data)
        if data > self.data and self.right:
            return self.right.find(data)

        return data == self.data

    def clear(self):
        self.data = None
        self.left = None
        self.right = None

    def delete(self, data, parent):
        if data < self.data and self.left:
            return self.left.remove_node(data, self)
        elif data < self.data:
            return False
        elif data > self.data and self.right:
            return self.right.remove_node(data, self)
        elif data > self.data:
            return False
        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.clear()
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear()
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear()
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.clear()
            elif self.right and self.left is None and self == parent.left:
                parent.left = self.right
                self.clear()
            elif self.right and self.left is None and self == parent.right:
                parent.right = self.right
                self.clear()
            else:
                self.data = self.right.find_minimum_data()
                self.right.remove_node(self.data, self)

        return True
