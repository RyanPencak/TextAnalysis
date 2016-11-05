class SStack:
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size

    def push(self,value):
        n = Node()
        n.data = value
        n.next = self.head
        self.head = n
        self.size += 1

    def pop(self):
        if (self.size != 0):
            item = self.head.data
            self.head = self.head.next
            self.size -= 1
            return item
        else:
            return None
