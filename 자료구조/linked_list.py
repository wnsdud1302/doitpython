class Node:
    def __init__(self, data, next = None):
         self.data = data
         self.next = next
    
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.crnt = None

    def search(self, data):
        ptr = self.head
        while ptr.next != None:
            if ptr.data == data:
                self.crnt = ptr
                return ptr
            ptr = ptr.next
        return None


    def InsertFront(self, data):
        tmpNode = Node(data)
        tmpNode.next =self.head
        self.head = tmpNode
        self.crnt = self.head
        del tmpNode

    def InsertRear(self, data):
        start = self.head
        tmpNode = Node(data)
        while start.next != None:
            start = start.next
        start.next = tmpNode
        self.crnt = start.next
        del tmpNode

    def RemoveFront(self):
        if self.head != None:
            tmpNode = self.head.next
            del self.head
        self.head = self.crnt = tmpNode



    def RemoveRear(self):
        start = self.head
        if start != None:
            if start.next == None:
                self.RemoveFront()
            else:
                pre = Node(None)
                while start.next != None:
                    pre = start
                    start = start.next
                pre.next = None
                self.crnt = pre
                

    def RemoveCurrent(self):
        if self.head != None:
            if self.crnt == self.head:
                self.RemoveFront()
            else:
                ptr = self.head
                curnt = self.crnt
                while ptr.next != curnt:
                    ptr = ptr.next
                ptr.next = curnt.next
                self.crnt = ptr


    def Clear(self):
        while self.head != None:
            self.RemoveFront()
        self.crnt = None


    def PrintCurrentData(self):
        if self.crnt == None:
            print("선택한 노드가 없습니다.")
        else:
            print(self.crnt.data)

    def PrintCurrentNext(self):
        print(self.crnt.next)

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
        print()
            



mylist = Linked_list()
mylist.InsertFront(3)
mylist.InsertFront(2)
mylist.InsertRear(5)
mylist.InsertFront(6)
mylist.InsertRear(3)
mylist.Print()
