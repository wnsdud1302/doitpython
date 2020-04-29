class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class double_linked_list:
    def __init__(self):
        self.head = Node("head")
        self.head.prev = self.head.next = self.head
    def insertFront(self, data):
        insert(data, self.head)

    
    def insertRear(self, data):
        insert(data,self.head.next.prev)

    
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
def insert(data, p):
    new_node = Node(data, p.next, p)
    p.next = p.next.prev = new_node

    


mylist = double_linked_list()
mylist.insertRear(8)
mylist.insertRear(5)
mylist.insertFront(3)
mylist.insertFront(4)
mylist.insertFront(7)
mylist.print()
