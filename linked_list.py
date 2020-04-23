class Node:
    def __init__(self, data, next = None):
         self.data = data
         self.next = next
    
    def updateData(self, data):
        self.data = data
    
    def SetNext(self, node):
        self.next = node
    
    def getData(self):
        return self.data

    def getNextnode(self):
        return self.next

    def setNode(self, data, next):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, Node, item):
        pass

    def InsertFront(self, data):
        tmpNode = Node(data)
        tmpNode.next =self.head
        self.head = tmpNode
        del tmpNode

    def InsertRear(self, data):
        start = self.head
        tmpNode = Node(data)
        while start.next != None:
            start = start.next
        start.next = tmpNode
        del tmpNode
        return True

    def RemoveFront(self):
        if self.head != None:
            tmpNode = self.head.next
            del self.head
            self.head =tmpNode

            


    def RemoveRear(self):
        pass

    def RemoveCurrent(self):
        pass

    def Clear(self):
        pass

    def PrintCurrentData(self):
        pass

    def PrintCurrentNext(self):
        pass

    def Print(self):
        start = self.head
        if start is None:
            print("empty List!!")
            return False
        while start:
            print(str(start.data), end=" ")
            start = start.next
            if start:
                print("-->", end=" ")
            

mylist = Linked_list()
mylist.InsertFront(1)
mylist.InsertFront(2)
mylist.InsertFront(4)
mylist.InsertRear(3)
mylist.RemoveFront()
mylist.Print()
