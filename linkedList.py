#program to reverse a linked list

class node():
    def __init__(self,value):
        self.data=value
        self.next=None

class linkedList():
    def __init__(self):
        self.head=None
    
    #add new nodes
    def append(self,value):
        if self.head is None:
            self.head=node(value)
        else:
            currentNode=self.head
            while currentNode.next is not None:
                currentNode=currentNode.next
            currentNode.next=node(value)

    #To print a Linkedlist
    def display(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.next

    #To find the length of linkedlist
    def length(self):
        currentNode=self.head
        len=0
        while currentNode is not None:
            len=len+1
            currentNode=currentNode.next
        print("length of linkedlist = " + str(len))

    #To display element at given position
    def getElement(self,position):
        currentNode=self.head
        i=0
        while currentNode is not None:
            if i==position:
                print("Data:" + str(currentNode.data))
            currentNode=currentNode.next
            i+=1
        return None
    
#To reverse a linked list
def reverse(lst):
        if lst.head is None:
            return
        
        current=lst.head
        prev=None

        while current is not None:
            next=current.next #track next node to not loose the rest of list

            current.next=prev #reverse the next of each node(to its previous one)

            prev=current
            current=next
        lst.head=prev
        

        

list1=linkedList()

list1.append(3)
list1.append(7)
list1.append(2)

reverse(list1)
list1.display()

list1.length()
list1.getElement(1)
