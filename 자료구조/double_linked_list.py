class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class double_linked_list:
    def __init__(self):
        tmpNode = Node(None)
        self.head = Node("head")
        self.head.next = tmpNode
        tmpNode.next = tmpNode.prev = tmpNode
    
    def insertFront(self, data):
        insert(data, self.head.next)

    def insertRear(self, data):
        insert(data,self.head.next.prev)
    
    def removeFront(self):
        remove(self.head.next.next)

    def removeRear(self):
        remove(self.head.next.prev)

    def print(self):
        start = self.head.next
        if start.next == None:
            print("비어있습니다!")
        while True:
            print(str(start.data), end=" ")
            start = start.next
            if start:
                print("-->", end=" ")
            if start.data == None: break
            continue
        print()

def insert(data, p):
    nxt = p.next
    new_node = Node(data, nxt, p)
    p.next = nxt.prev = new_node

def remove(p):
    p.prev.next = p.next
    p.next.prev = p.prev
    del p

    


mylist = double_linked_list()
mylist.insertRear(8)
mylist.insertRear(5)
mylist.insertFront(3)
mylist.insertFront(4)
mylist.insertFront(7)
mylist.insertRear(2)
mylist.removeFront()
mylist.removeRear()
mylist.print()
