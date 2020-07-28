class Heap:
    def __init__(self):
        self.a = []
    def max_heapify(self,i,n):
        left = 2*i+1
        right = 2*i+2
        if left < n and self.a[i] < self.a[left]:
            largest = left
        else:
            largest = i
        if right < n and self.a[largest] < self.a[right]:
            largest = right
        if i != largest:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.max_heapify(largest,n)
    def build_max_heap(self):
        for i in range(len(self.a)//2,-1,-1):
            self.max_heapify(i,len(self.a))
    def heapSort(self):
        #self.build_max_heap()
        for i in range(len(self.a)-1,0,-1):
            self.a[0],self.a[i] = self.a[i],self.a[0]
            self.max_heapify(0,i)
    def heap_increase_key(self,i,key):
        if self.a[i] > key:
            return
        self.a[i] = key
        while i > 0 and self.a[i] > self.a[(i-1)//2]:
            self.a[i],self.a[(i-1)//2] = self.a[(i-1)//2],self.a[i]
            i = (i-1)//2
    def heap_insert(self,key):
        self.a.append(-1000000)
        self.heap_increase_key(len(self.a)-1,key)
    def print_heap(self):
        print(self.a)
heap1 = Heap()
heap1.heap_insert(4)
heap1.heap_insert(10)
heap1.heap_insert(8)
heap1.heap_insert(16)
heap1.heap_insert(14)
heap1.heap_insert(7)
heap1.heap_insert(1)
heap1.heap_insert(2)
heap1.heap_insert(9)
heap1.heap_insert(3)
heap1.heap_insert(200)
heap1.heap_insert(19)
heap1.print_heap()
heap1.heapSort()
heap1.print_heap()













