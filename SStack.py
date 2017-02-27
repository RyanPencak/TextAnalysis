####################################################################################################################################################################
# Name: Ryan Pencak
# Class: SStack
# Summary: The SStack class is a data stucture for a stack using a singly linked list initialized with a head node and size. It has methods to push an item onto the stack, pop (remove and return) the top item from the stack, and peek (return) the top item on the stack.
####################################################################################################################################################################


class SStack:
    
    
    # Initializes a stack data type object
    # Precondition: Optional head and size attributes are default to None and zero respectively
    # Postcondition: Initializes the stack with the optional attributes head and size
    
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size


    # Pushes an item onto the stack
    # Precondition: Takes in a value to push on the stack
    # Postcondition: Creates a node with the given value and pushes it onto the stack
    
    def push(self,value):
        n = Node()
        n.data = value
        n.next = self.head
        self.head = n
        self.size += 1


    # Pops the top item off the stack
    # Precondition: There should be one item on the stack or it will return None
    # Postcondition: Removes the top item from the stack and returns the value or returns none if the stack is empty
    
    def pop(self):
        if (self.size != 0):
            item = self.head.data
            self.head = self.head.next
            self.size -= 1
            return item
        else:
            return None
            
            
    # Peeks at the top item in the stack
    # Precondition: There should be one item on the stack or it will return None
    # Postcondition: Returns the top item in the stack or returns None if the stack is empty
    
    def peek(self):
        if (self.size != 0):
            return self.head
        else:
            return None
