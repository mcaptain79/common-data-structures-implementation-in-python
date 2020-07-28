class Stack:
    __a = []
    def __init__(self):
        print('object created')
    def top(self):
        if len(self.__a) == 0:
            return 'stack is empty'
        else:    
            return len(self.__a)-1
    def pop(self):
        if len(self.__a) == 0:
            return 'stack under flow'
        else:
            x = self.__a[len(self.__a)-1]
            self.__a.pop()
            return x
    def push(self,x):
        self.__a.append(x)
    def isEmpty(self):
        if len(self.__a) == 0:
            return True
        return False
stack1 = Stack()
for i in range(10):
    stack1.push((i)**2)
for i in range(15):
    print('is empty:',stack1.isEmpty(),'top index:',stack1.top(),'removed element:',stack1.pop())