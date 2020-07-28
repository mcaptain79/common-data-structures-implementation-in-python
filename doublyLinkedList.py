class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.previous = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def List_Insert(self,key):
        node = Node(key)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
    def List_Delete(self,key):
        isFound = False
        x = self.head
        if self.head == None:
            return
        if self.head.key == key and self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if self.head.key == key:
            self.head = x.next
            return
        if self.tail.key == key:
            self.tail = self.tail.previous
            return
        while x != None:
            if x.key == key:
                isFound = True
                break
            previous = x
            x = x.next
        if isFound:
            previous.next = x.next
            x.next.previous = previous
    def Union(self,L):
        self.tail.next = L.head
        L.head.previous = self.tail
        self.tail = L.tail
    def List_Search(self,key):
        counter = 0
        x = self.head
        while x != None:
            if x.key == key:
                return counter
            counter += 1
            x = x.next
        return 'NOTFOUND'
    def Print_List(self):
        x = self.head
        if self.head == self.tail == None:
            print(None)
            return
        print('None',end='<-->')
        while x != self.tail:
            print(x.key,end='<-->')
            x = x.next
        print(self.tail.key,end='<-->None\n')
L1 = LinkedList()
for i in range(10):
    L1.List_Insert(i**3)
L1.Print_List()
L1.List_Delete(10)
L1.List_Delete(729)
L1.List_Delete(0)
L1.List_Delete(13)
L1.List_Delete(125)
L1.List_Delete(216)
L1.List_Delete(27)
L1.Print_List()
L2 = LinkedList()
for i in range(5):
    L2.List_Insert(i**2+2)
L2.Print_List()
L1.Union(L2)
L1.Print_List()
print(L1.List_Search(10),L1.List_Search(512),L1.List_Search(343),L1.List_Search(1),L1.List_Search(18),L1.List_Search(2))





