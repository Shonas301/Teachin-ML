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

