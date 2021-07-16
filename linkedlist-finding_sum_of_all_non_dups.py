#Node class to create nodes.
class Node:
    
    def __init__(self,val):
        self.val=val
        self.next=None


#linkedlist class which lets you add nodes in the begining. Good technique        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def add_nodes(self,node): #adding node at the start of linkedlist
        
        if self.head is None:
            self.head=node
            
        else:
            node.next=self.head
            self.head=node
        
    def print_nodes(self):
        
        while self.head:
            print(self.head.val)
            self.head=self.head.next
            
    def find_sum_of_nondups(self):
        
        ressum=0
        visited_set=set()
        
        while self.head:
            if self.head.val not in visited_set:
                ressum+=self.head.val
                visited_set.add(self.head.val)
            else:
                ressum-=self.head.val
            self.head=self.head.next    
        return ressum
   
arr=[7,4,2,6,4,2,1]
ll = LinkedList()

#creating and adding nodes to linked list from values in arr
for x in arr:
    print("adding node with val " + str(x))
    node1 = Node(x)
    ll.add_nodes(node1)

#Print final result
#print(ll.print_nodes())    
print(ll.find_sum_of_nondups())
