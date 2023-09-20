class treeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def insert(self,value):
        if value<self.value:
            if not self.left:
                self.left=treeNode(value)
            else:
                self.left.insert(value)
        if value>self.value:
            if not self.right:
                self.right=treeNode(value)
            else:
                self.right.insert(value)

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.value)
        if self.right:
            self.right.inorderTraversal()

    def preorderTraversal(self):
        print(self.value)
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()

    def postorderTraversal(self):
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()
        print(self.value)

t1=treeNode(8) #head
t1.insert(3)
t1.insert(1)
t1.insert(6)
t1.insert(10)
t1.insert(14)
#t1.inorderTraversal()
#t1.preorderTraversal()
t1.postorderTraversal()