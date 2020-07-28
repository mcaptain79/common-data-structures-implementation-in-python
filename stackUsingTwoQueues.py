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
    def isEmpty(self):
        if len(self.__a) == 0:
            return True
        return False
class Stack:
    __counter = 0
    __q1 = Queue()
    __q2 = Queue()
    def __init__(self):
        print('object is created')
    def isEmpty(self):
        return self.__q1.isEmpty()
    def push(self,x):
        self.__q1.enqueue(x)
        self.__counter += 1
    def pop(self):
        if self.__counter == 0:
            pass
        else:
            for i in range(self.__counter): 
                self.__q2.enqueue(self.__q1.dequeue())
            for i in range(self.__counter-1):
                self.__q1.enqueue(self.__q2.dequeue())
            self.__counter -= 1
            return self.__q2.dequeue()
#I wrote it in order to check if queue is working
s1 = Stack()
for i in range(10):
    s1.push(i**2)
for i in range(9):
    print(s1.pop())
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

    