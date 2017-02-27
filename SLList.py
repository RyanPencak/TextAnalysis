####################################################################################################################################################################
# Name: Ryan Pencak
# Class: SLList, ListNode, and ListIterator
# Summary: The SLList class is a data structure for a singly linked list. It is initialized with a head, a size, and a frequency all default to None or zero. It has methods to return the size, iterate, insert, append, pop, and peek. The ListNode class is the node class for the singly linked list. It is initialized with data and a next node and has a method to represent the node. The ListIterator class is the iterator for the singly linked list initialized with a head node. It has methods next and calls itself in an iter method.
####################################################################################################################################################################


class SLList:


	# Creates an empty list with a head node
	# Precondition: None
	# Postcondition: Initializes the singly linked list class
	
	def __init__ (self):
		self._head = None
		self._size = 0
		self.freq = 0


	# Returns the size of the list
	# Precondition: Called on the SLList object
	# Postcondition: Returns the size of the list
	
	def __len__ (self):
		return self._size


	# Gives list class functionality for an iterator by overriding iter method
	# Precondition: Overrides the iter method
	# Postcondition: Returns the List Iterator class as the iterator for the singly linked list
	
	def __iter__(self):
		return _ListIterator(self._head)


	# Inserts an item at a given index
	# If index is too small, insert at index 0
	# If index is too large, insert at end of list
	# If no index is entered, automatically adds to beginning of list
	# Precondition: Item to be inserted in the list and an optional index value
	# Postcondition: Creates a node with the given item, adds it to the appropriate position in the linked list, and increments size
	
	def insert (self, item, index = 0):
		newNode = ListNode()
		newNode.data = item
		curNode = self._head
		count = 0

		if self._size == 0:

			self._head = newNode


		elif index <= 0:

			newNode.next = self._head
			self._head = newNode


		elif index <= self._size:

			while curNode.next != None and count < index:
				curNode = curNode.next
				count += 1

			newNode.next = curNode.next
			curNode.next = newNode


		else:

			while curNode.next != None:
				curNode = curNode.next

			curNode.next = newNode
			

		self._size += 1


	# Appends an item to the end of the list
	# Precondition: Takes in an item to append to the end of the singly linked list
	# Postcondition: Creates a node with the item given and adds it to the end of the list
	
	def append (self, item):
		newNode = ListNode()
		newNode.data = item
		curNode = self._head

		if self._size > 0:

			while curNode.next != None:
				curNode = curNode.next

			curNode.next = newNode

		else:

			self._head = newNode

		self._size += 1


	# Removes and returns the item at the given index
	# If index is not provided remove and return the last item in the list
	# Precondition: Given an index to remove, or defaults to remove the last item in the list
	# Postcondition: Returns the removed item
	
	def pop (self, index = 'a'):

		curNode = self._head

		if(index == 'a'):

			index = (self._size - 2)
			count = 0

			while count < index:
				curNode = curNode.next
				count += 1

			r = curNode.next.data
			curNode.next = None

		elif index == 0:

			r = curNode.data
			self._head = curNode.next


		elif index > 0:

			count = 0

			while curNode.next != None and count < index:
				curNode = curNode.next
				count += 1

			r = curNode.next.data
			curNode.next = curNode.next.next

		self._size -= 1
		return r


	# Returns the item at the given index
	# Precondition: Index value to be returned
	# Postcondition: Returns given index value
	
	def peek (self, index):
		curNode = self._head

		if index >= 0 and index < self._size:

			count = 0

			while count < index:
				curNode = curNode.next
				count += 1

			return curNode.next.data

		else:
			raise Exception




#Class for creating List Nodes
class ListNode:


	# Creates an empty list with a head node
	# Precondition: None
	# Postcondition: Initializes a list node object with a string of data and next
	
	def __init__ (self):
		self.next = None
		self.data = []


	# Repr used to return data
	# Precondition: Called on List Node Object
	# Postcondition: Returns data in a printable form
	
	def __repr__ (self):
		return self.data




#Linked List Iterator for List
class _ListIterator:


	# Creates iterator and gets it ready to return data
	# Precondition: Takes in a head to initialize the iterator
	# Postcondition: Initializes the iterator with a current node assigned as the given head
	
	def __init__ (self, head):
		self._curNode = head



	# Returns the next data in order in the ADT
	# If there is no next data, raise a StopIteration exception
	# Precondition: Called on ListIterator object
	# Postcondition: Returns data until there is no next data then raises StopIteration
	
	def __next__ (self):
		if self._curNode == None:
			raise StopIteration
		else:
			data = self._curNode.data
			self._curNode = self._curNode.next
			return data



	# Returns ListIterator(self)
	# Precondition: Called on ListIterator object
	# Postcondition: Returns itself to override iterator
	
	def __iter__ (self):
		return self
