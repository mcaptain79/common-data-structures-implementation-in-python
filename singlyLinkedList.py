class X:
    def __init__(self,key):
        self.key = key
        self.nexty = None
class LinkedList:
    def __init__(self):
        self.head = None
    def List_Insert(self,key):
        x = X(key)
        x.nexty = self.head
        self.head = x
    def List_Delete(self,key):
        isFound = False
        x = self.head
        if self.head == None:
            return
        if self.head.key == key:
           self.head = x.nexty
           return
        while x != None:
            if x.key == key:
                isFound = True
                break
            previous = x
            x = x.nexty
        if isFound:
            previous.nexty = x.nexty
    #if exists returns attribute else returns not found
    def List_Search(self,key):
        counter = 0
        x = self.head
        while x != None:
            if x.key == key:
                return counter
            counter += 1
            x = x.nexty
        return 'NotFound'
    def Union(self,L2):
        x = self.head
        while x != None:
            y = x
            x = x.nexty
        y.nexty = L2.head
    def printList(self):
        tmp = self.head
        while tmp != None:
            print(tmp.key,end = '-->')
            tmp  = tmp.nexty
        print('None')
#I made an object and tested all the functions and they work properly
L1 = LinkedList()
for i in range(10):
    L1.List_Insert(i)
print('initial list:')
L1.printList()
print('-------------------------------------------------------')
L1.List_Delete(9)
L1.List_Delete(8)
L1.List_Delete(7)
L1.List_Delete(11)
L1.List_Delete(0)
L1.List_Delete(3)
L1.List_Delete(111)
print('List after deleting some items:')
L1.printList()
print('-------------------------------------------------------')
print('searching some elements:')
print(L1.List_Search(6),L1.List_Search(2),L1.List_Search(1),L1.List_Search(20),L1.List_Search(9))
print('-------------------------------------------------------')
L2 = LinkedList()
L2.List_Insert(100)
L2.List_Insert(200)
L2.List_Insert(300)
L2.List_Insert(25)
L2.List_Insert(777)
#union code test
print('union of list1 and List2:')
L1.Union(L2)
L1.printList()




