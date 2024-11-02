class Node:
    def __init__(self, data=None):
        self.data=data # The value stored in the node
        self.next=None # The reference to the next node

class Linkedlist:
    def __init__(self):
        self.head= None # The head of the list, initally None

    def append(self, data):
        '''Add a node with the sepcified data to the end of the list'''
        new_node= Node(data)
        if not self.head:
            self.head=new_node #If the list is empyry, set the node as the head return
            return
        last=self.head
        while last.next: #Traverse to the ast node
            last=last.next
        last.next=new_node #Link the last node to the new node

    def prepend(self,data):
        '''Add a node with the specified data to the start of the list'''
        new_node=Node(data)
        new_node.next=self.head #Point the new nodes's next to the current head
        self.head=new_node # Set the new node as the new head

    def display(self):
        '''Print the linked list'''
        elements=[]
        current=self.head
        while current: 
            elements.append(current.data)
            current=current.next
        print("->".join(map(str, elements))+"-> None")

    def count(start):
        count = 0
        current = start
        while current:
            count = count + 1
            current = current.next
        return count


    def ispalindrome(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        current = self.head
        
        ispalin = False
        while current:
            if current.data == elements.pop():
                
                ispalin = True   
                     
            else:
                ispalin = False 
                break
            
            current=current.next
        
        return ispalin

    def connect(self, other_list):
        if not self.head:
            self.head = other_list.head
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = other_list.head
    

    def bubble_sort(self):
        if not self.head:
            return
    
        while True:
            swapped = False
            current = self.head
       
            while current and current.next:
                if current.data > current.next.data:
                    if current.data != current.next.data:
                        temp = current.data
                    current.data = current.next.data
                    current.next.data = temp
                    swapped = True
                current = current.next
            
            if not swapped: 
                break

myLL=Linkedlist()
myLL.append(1)
myLL.append(5)
myLL.append(10)
myLL.append(12)
myLL.append(3)
myLL.append(4)

myLL.display()
myLL.bubble_sort()
myLL.display()

