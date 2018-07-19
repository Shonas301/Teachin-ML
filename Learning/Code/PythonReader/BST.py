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
