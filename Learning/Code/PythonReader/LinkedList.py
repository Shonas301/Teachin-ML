class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def addNext(self, node):
        self.next = node

class LL:
    def __init__(self):
        self.head = None

    def addToEnd(self, data):
        if self.head is None: 
            self.head = Node(data)
        else:
            node = self.head
            while node.next != None:
                node = node.next 
            node.addNext(Node(data))

    def printList(self):
        node = self.head
        while node != None:
            print(node.data, end='')
            if node.next is None:
                print("\n")
            else:
                print(", ", end='')
            node = node.next
            
    def deleteNode(self, val):
        # Return a list without that value, don't tell them if it was there in 
        # the first place
        if self.head.data == val:
            self.head = self.head.next
            return True
        
        node = self.head.next
        prev = self.head
        while node is not None:
            if node.data == val:
                prev.next = node.next
                node.data = None
                node.next = None
                return True
            node = node.next
            prev = prev.next
        return False

def main():
    # Demo
    demoOne = LL()
    demoOne.addToEnd(5)
    demoOne.addToEnd(6)
    demoOne.addToEnd(7)
    demoOne.printList()

    # Demo 2 
    demoTwo = LL()
    demoTwo.addToEnd(1)
    demoTwo.addToEnd(2)
    demoTwo.addToEnd(3)
    demoTwo.deleteNode(2)
    demoTwo.printList()

if __name__ == "__main__":
    main()
