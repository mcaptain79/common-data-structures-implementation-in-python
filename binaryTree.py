class Node:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def Tree_Insert(self,key):
        node = Node(key)
        y = None
        x = self.root
        while x != None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif key < y.key:
            y.left = node
        else:
            y.right = node
    #recursive method
    def Tree_Insert2(self,x,key):
        z = Node(key)
        if x == None:
            self.root = z
            return
        if x.left == None:
            if z.key < x.key:
                x.left = z
                z.parent = x
                return
        if x.right == None:
            if z.key > x.key:
                x.right = z
                z.parent = x
                return
        if z.key < x.key:
            return self.Tree_Insert(x.left, key)
        else:
            return self.Tree_Insert(x.right, key)
    #returns value of minimum
    def Tree_Min(self,x):
        while x.left != None:
            x = x.left
        return x.key
    #returns address of minimum
    def Tree_Min2(self,x):
        while x.left != None:
            x = x.left
        return x
    #recursive function
    def Tree_Min3(self,x):
        if x.left == None:
            return x.key
        else:
            return self.Tree_Min3(x.left)
    def Tree_Max(self,x):
        while x.right != None:
            x = x.right
        return x.key
    #recursive function
    def Tree_Max2(self,x):
        if x.right == None:
            return x.key
        else:
            return self.Tree_Max2(x.right)
    def Tree_Search(self,x,key):
        if x == None or x.key == key:
            return x
        if key < x.key:
            return self.Tree_Search(x.left, key)
        else:
            return self.Tree_Search(x.right, key)
    #returns key of sucessor
    def Tree_successor(self,key):
        result = self.Tree_Search(self.root, key)
        if result == None:
            return None
        if result.key == self.Tree_Max(self.root):
            return None
        if result.right != None:
            return self.Tree_Min(result.right)
        y = result.parent
        while y != None and result.key > y.key:
            y = y.parent
        return y.key
    #returns value of sucessor
    def Tree_successor2(self,key):
        result = self.Tree_Search(self.root, key)
        if result == None:
            return None
        if result.key == self.Tree_Max(self.root):
            return None
        if result.right != None:
            return self.Tree_Min2(result.right)
        y = result.parent
        while y != None and result.key > y.key:
            y = y.parent
        return y
    def Tree_predeccessor(self,key):
        result = self.Tree_Search(self.root, key)
        if result == None:
            return None
        if result.key == self.Tree_Min(self.root):
            return None
        if result.left != None:
            return self.Tree_Max(result.left)
        y = result.parent
        while y != None and result.key < y.key:
            y = y.parent
        return y.key
    def Tree_Delete(self,key):
        z = self.Tree_Search(self.root, key)
        if z == None:
            return None
        #we determine the value of y y is either z or its successor
        if z.left == None or z.right == None:
            y = z
        else:
            y = self.Tree_successor2(key)
        #x becomes child if exists 
        if y.right != None:
            x = y.right
        else:
            x = y.left
        #if x is not none it means it exists and we should update its parent pointer
        if x != None:
            x.parent = y.parent
        #if y has a parent we should update the pointers
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        #we should update value of z in case y != z
        z.key = y.key
        return y
    def Inorder_Tree_Walk(self,x):
        if x != None:
            self.Inorder_Tree_Walk(x.left)
            print(x.key,end = ' ')
            self.Inorder_Tree_Walk(x.right)
    #non recursive method
    def Tree_print(self):
        x = self.Tree_Min2(T.root)
        while x != None:
            print(x.key)
            x = self.Tree_successor2(x.key)
    def Preorder_Tree_walk(self,x):
        if x != None:
            print(x.key,end=' ')
            self.Preorder_Tree_walk(x.left)
            self.Preorder_Tree_walk(x.right)
    def Postorder_tree_walk(self,x):
        if x != None:
            self.Postorder_tree_walk(x.left)
            self.Postorder_tree_walk(x.right)
            print(x.key,end = ' ')
#making objects and testing Binary Tree
T = BinaryTree()
T.Tree_Insert(10)
T.Tree_Insert(15)
T.Tree_Insert(6)
T.Tree_Insert(11)
T.Tree_Insert(9)
T.Tree_Insert(4)
T.Tree_Insert(17)
T.Tree_Insert(1)
T.Tree_Insert(18)
T.Tree_print()
print(T.root.left)
print('---------------------------------')
print('in order:')
T.Inorder_Tree_Walk(T.root)
print('\n-------------------------------')
print('pre order:')
T.Preorder_Tree_walk(T.root)
print('\n-------------------------------')
print('post order:')
T.Postorder_tree_walk(T.root)
print('\n-------------------------------')
print('recursive method: ',T.Tree_Min3(T.root))
print(T.Tree_Min(T.root))
print(T.Tree_Min(T.root.right))
print('---------------------------------')
print('recursive method: ',T.Tree_Max2(T.root))
print(T.Tree_Max(T.root))
print(T.Tree_Max(T.root.left))
print('---------------------------------')
print(T.Tree_Search(T.root.left, 10))
print(T.Tree_Search(T.root, 10))
print('---------------------------------')
print(T.Tree_successor(10))
print(T.Tree_successor(12))
print(T.Tree_successor(11))
print(T.Tree_successor(9))
print(T.Tree_successor(1))
print(T.Tree_successor(17))
print(T.Tree_successor(18))
print('---------------------------------')
print(T.Tree_predeccessor(10))
print(T.Tree_predeccessor(12))
print(T.Tree_predeccessor(11))
print(T.Tree_predeccessor(9))
print(T.Tree_predeccessor(1))
print(T.Tree_predeccessor(17))
print(T.Tree_predeccessor(18))
print('---------------------------------')
x = T.Tree_Delete(10)
print('deleted: ',x.key)
T.Inorder_Tree_Walk(T.root)
print('\n---------------------------------')
x = T.Tree_Delete(4)
print('deleted: ',x.key)
T.Inorder_Tree_Walk(T.root)
print('\n---------------------------------')
x = T.Tree_Delete(18)
print('deleted: ',x.key)
T.Inorder_Tree_Walk(T.root)
print('\n---------------------------------')
x = T.Tree_Delete(100)
print('deleted: ',x)
T.Inorder_Tree_Walk(T.root)
print('\n---------------------------------')







