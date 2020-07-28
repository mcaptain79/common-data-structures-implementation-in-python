class Queue:
    __a = []
    def __init__(self):
        print('object created')
    def enqueue(self,x):
        self.__a.append(x)
    def dequeue(self):
        if len(self.__a) == 0:
            return 'under flow'
        else:
            x = self.__a[0]
            self.__a.pop(0)
            return x
queue1 = Queue()
for i in range(10):
    queue1.enqueue(i**2)
for i in range(6):            
      print('removed element: ',queue1.dequeue())
print('-----------------------------------------------')
queue1.enqueue(17)
for i in range(6):
    print('removed element: ',queue1.dequeue())
