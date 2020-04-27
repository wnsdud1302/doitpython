class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class double_linked_list:
    def __init__(self):
        tmpNode = Node(None)
        self.head = tmpNode
        tmpNode.prev = tmpNode.next = tmpNode

    def insertFront(self, data):
        insert(self.head, data)
    def insertRear(self, data):
        insert(self.head.prev, data)
    def print(self):
        start = self.head.next
        if start.next == None:
            print("비어있습니다!")
        while start != self.head:
            print(str(start.data), end=" ")
            start = start.next
            if start:
                print("-->", end=" ")
        print()

def insert(p, data):
    newNode = Node(data, p.next, p)
    p.next = p.next.prev = newNode




          


mylist = double_linked_list()
mylist.insertFront(3)
mylist.insertFront(4)
mylist.print()
