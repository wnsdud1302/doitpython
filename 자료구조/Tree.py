 
class BinNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def printBinNode(self):
        print(self.data)

class Tree:
    def __init__(self, root):
        self.root = BinNode(root)

    def add(self, data):
        start = self.root
        while True:
            if start.data > data:
                if start.left != None:
                    start = start.left
                else:
                    start.left = BinNode(data)
                    break
            else:
                if start.right != None:
                    start = start.right
                else:
                    start.right = BinNode(data)
                    break

    def remove(self, data):
        start = self.root
        parent = start
        while start:
            if start.data == data:
                break
            elif start.data > data:
                parent = start
                start = start.left
            elif start.data < data:
                parent = start
                start = start.right
            else:
                return False
        if start.left == None and start.right == None:
            if parent.data > data:
                parent.left = None
            else:
                self.parent.right = None
        elif start.left != None and start.right == None:
            if parent.data > data:
                parent.left = start.left
            else:
                parent.right = start.left
        elif start.left == None and start.right != None:
            if parent.data > data:
                parent.left = start.right
            else:
                parent.right = start.left
        elif start.left != None and start.right != None:
            pass


    def search(self, data):
        start = self.root
        while start:
            if start.data == data:
                print(start.data)
                return True
            elif start.data < data:
                print(start.data)
                start = start.left
            else:
                print(start.data)
                start = start.right
            

