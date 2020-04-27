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
        new_node = Node(data, self.head.next, self.head)
        self.head.next = self.head.next.prev = new_node
    
    def insertRear(self, data):
        new_node = Node(data, self.head.prev, self.head)
        self.head.prev = self.head.prev.next = new_node
    
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

mylist = double_linked_list()
mylist.insertFront(3)
mylist.insertFront(4)
mylist.insertRear(5)
mylist.print()
