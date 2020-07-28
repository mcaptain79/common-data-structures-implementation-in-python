class Node:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'red'
class redBlackTree:
    def __init__(self):
        self.Nil = Node('not found')
        self.Nil.color = 'black'
        self.root = self.Nil
        self.root.parent = self.Nil
    def Tree_search(self,x,key):
        if x == self.Nil or x.key == key:
            return x
        if x.key > key:
            return self.Tree_search(x.left, key)
        else:
            return self.Tree_search(x.right, key)
    #initial call is x = T.root
    def Tree_Max(self,x):
        while x != self.Nil:
            y = x
            x = x.right
        return y
    def Tree_Min(self,x):
        while x != self.Nil:
            y = x
            x = x.left
        return y
    def Inorder_Tree_walk(self,x):
        if x != self.Nil:
            self.Inorder_Tree_walk(x.left)
            print(x.key,x.color,end = ' ')
            self.Inorder_Tree_walk(x.right) 
    def Tree_successor(self,key):
        result = self.Tree_search(self.root, key)
        if result == self.Nil:
            return 'not found'
        if result == self.Tree_Max(self.root): 
            return 'not found'
        if result.right != None:
            return self.Tree_Min(result.right)
        y = result.parent
        while y != self.Nil and result.key > y.key:
            y = y.parent
        return y
    def Left_Rotate(self,x):
        y = x.right
        if y == self.Nil:
            return
        y.parent = x.parent
        x.right = y.left
        if y.left != self.Nil:
            y.left.parent = self.Nil
        if x.parent == self.Nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.left = x
        x.parent = y
    def Right_Rotate(self,x):
        y = x.left
        if y == self.Nil:
            return
        y.parent = x.parent
        x.left = y.right
        if y.right != self.Nil:
            y.right.parent = self.Nil
        if x.parent == self.Nil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def RB_Insert_Fixedup(self,z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    y.color = 'black'
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.Left_Rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.Right_Rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    y.color = 'black'
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.Right_Rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.Left_Rotate(z.parent.parent)
        self.root.color = 'black'        
    def RB_Insert(self,key):
        z = Node(key)
        y = self.Nil
        x = self.root
        while x != self.Nil:
            y = x
            if x.key > z.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.Nil:
            self.root = z
        elif y.key > z.key:
            y.left = z
        else:
            y.right = z
        z.left = self.Nil
        z.right = self.Nil
        z.color = 'red'
        self.RB_Insert_Fixedup(z)
    def rb_delete_fixedup(self,x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.Left_Rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'red':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.Right_Rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.Left_Rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.Right_Rotate(x.parent)
                    w = x.parent.left
                if w.left.color == 'black' and w.right.color == 'red':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.Left_Rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.Right_Rotate(x.parent)
                    x = self.root
    def rb_delete(self,key):
        z = self.Tree_search(self.root, key) 
        if z.left == self.Nil or z.right == self.Nil:
            y = z
        else:
            y = self.Tree_successor(key)
        if y.left != self.Nil:
            x = y.left
        else:
            x = y.right
        x.parent = y.parent
        if y.parent == self.Nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x 
        else:
            y.parent = x
        z.key = y.key
        if y.color == 'black':
            self.rb_delete_fixedup(x) 
        return y
rb = redBlackTree()
rb.Inorder_Tree_walk(rb.root)
rb.RB_Insert(55)
rb.RB_Insert(44)
rb.RB_Insert(33)
rb.RB_Insert(22)
rb.RB_Insert(11)
rb.RB_Insert(1)
rb.Inorder_Tree_walk(rb.root)
print('\n+++++++++++++++++++++++++++++++++++++')
rb.rb_delete(22)
rb.Inorder_Tree_walk(rb.root)
print("\n+++++++++++++++++++++++++++++++++++++") 
rb.rb_delete(33)
rb.Inorder_Tree_walk(rb.root)
print("\n+++++++++++++++++++++++++++++++++++++")
rb.rb_delete(55)
rb.Inorder_Tree_walk(rb.root)
        
        
        
        
        
        
    