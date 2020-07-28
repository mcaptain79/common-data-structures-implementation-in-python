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
class Node2:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def __str__(self):
        return str(self.key)+','+str(self.value)
class hashTable:
    def __init__(self):
        self.a = [LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList()]
    def hashFunction(self,key):
        return key%5
    def search(self,key):
        slot = self.hashFunction(key)
        x = self.a[slot].head
        while x != None:
            if x.key.key == key:
                return x.key
            x = x.next
        return 'NOTFOUND'
    def insert(self,key,value):
            node = Node2(key,value)
            slot = self.hashFunction(key)
            self.a[slot].List_Insert(node)
    def delete(self,key):
        slot = self.hashFunction(key)
        isFound = False
        x = self.a[slot].head
        if self.a[slot].head == None:
            return
        if self.a[slot].head.key.key == key and self.a[slot].head == self.a[slot].tail:
            self.a[slot].head = None
            self.a[slot].tail = None
            return
        if self.a[slot].head.key.key == key:
            self.a[slot].head = x.next
            return
        if self.a[slot].tail.key.key == key:
            self.a[slot].tail = self.a[slot].tail.previous
            return
        while x != None:
            if x.key.key == key:
                isFound = True
                break
            previous = x
            x = x.next
        if isFound:
            previous.next = x.next
            x.next.previous = previous 
    def printer(self):
        for i in range(5):
            self.a[i].Print_List()
            print()
h1 = hashTable()
h1.insert(1,'ali') 
h1.insert(7,'hasan')
h1.insert(18,901)
h1.insert(2,'mohsen')
h1.insert(22,'sibil')
h1.insert(34,'mew')
h1.insert(98,23)
h1.printer()
print('---------------------------------')
h1.delete(10)
h1.delete(18)
h1.delete(34)
h1.delete(25)
h1.delete(2)
h1.printer()





            
        
        
    
    
    
    
    
    
    
    
    
    
    