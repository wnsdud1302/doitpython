class BinNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def printBinNode(self):
        print(self.data)

class Tree:
    def __init__(self):
        self.root = None
    
    def printTree(self):
        if self.root != None:
            printTree(self.root.left)
            self.root.printBinNode()
            printTree(self.root.right)
