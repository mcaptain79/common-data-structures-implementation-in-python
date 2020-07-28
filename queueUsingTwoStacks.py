class Queue:
    __s1 = []
    __s2 = []
    __size = 0
    def __init__(self):
        print('object created')
    def enqueue(self,x):
        self.__s1.append(x)
        self.__size += 1
    def dequeue(self):
        if self.__size == 0:
            pass
        else:
            for i in range(self.__size):
                self.__s2.append(self.__s1.pop())
            x = self.__s2.pop()
            for i in range(self.__size-1):
                self.__s1.append(self.__s2.pop())
            self.__size -= 1
            return x
q1 = Queue()
for i in range(8):
    q1.enqueue(i**2)
for i in range(6):
    print(q1.dequeue())
q1.enqueue(29)
q1.enqueue(291)
q1.enqueue(129)
for i in range(7):
    print(q1.dequeue())




