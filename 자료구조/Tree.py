class BinNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def printBinNode(self):
        print(self.data)

class BinTree:
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
        del_node = self.root
        parent_node = del_node
        while True:
            if del_node.data == data:
                break
            elif del_node.data > data:
                parent_node = del_node
                del_node = del_node.left
            elif del_node.data < data:
                parent_node = del_node
                del_node = del_node.right
        
        if del_node.left == None and del_node.right == None:
            if parent_node.data > data:
                parent_node.left = None
            else:
                parent_node.right = None
        elif del_node.left != None and del_node.right == None:
            if parent_node.data > data:
                parent_node.left = del_node.left
            else:
                parent_node.right = del_node.left
        elif del_node.left == None and del_node.right != None:
            if parent_node.data > data:
                parent_node.left = del_node.right
            else:
                parent_node.right = del_node.right
        else:
            change_node = del_node
            parent_node = del_node
            del_node = del_node.right
            while del_node.left:
                parent_node = del_node
                del_node = del_node.left
            change_node.data = del_node.data
            if del_node.right != None:
                parent_node.left = del_node.right
            else :
                parent_node.left = None

    def search(self, data):
        start = self.root
        while start:
            if start.data == data:
                print(start.data)
                return True
            elif start.data > data:
                print(start.data)
                start = start.left
            else:
                print(start.data)
                start = start.right
