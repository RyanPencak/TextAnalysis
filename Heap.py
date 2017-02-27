####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Heap
# Summary: The Heap class creates a class for a heap data structure. It contains an initialization of the heap, an add method which adds an item to the heap, and a remove method which removes an item from the heap. It also has methods exch, fixUp, and fixDown which are utilized in the add and remove methods.
####################################################################################################################################################################


class Heap:


	# Initializes the heap
	# Precondition: A real value n must be inputted, and optionally tree and end variables
	# Postcondition: Heap is initialized and size is set
		
	def __init__(self, n, tree = None, end = 0):
		self.n = n
		self.end = end
		self.tree = tree
		if self.tree == None:
			self.tree = [None] * self.n


	# An item is added to the heap and inserted in the correct position utilizing fixUp
	# Precondition: A variable for item must be entered as a parameter
	# Postcondition: Nothing is returned and the item is added to the heap

	def add(self, item):
		self.end += 1
		if(self.end < self.n):
			self.tree[self.end] = item
			fixUp(self.tree, self.end, self.end + 1)


	# An item is removed from the heap and the heap is corrected with fixDown
	# Precondition: The tree must be initialized, there are no parameters
	# Postcondition: Returns the tree after the item is removed

	def remove(self):
		if self.end == 0:
			return False
		t = self.tree[1]
		exch(self.tree, 1, self.end)
		fixDown(self.tree, 1, self.end)
		self.end -= 1
		return t
		
		
	# Fixes the tree up when items are added
	# Precondition: The first parameter should be a list, the second and third both integers
	# Postcondition: Sets a new i value
		
	def fixUp(self, aList, i, n):
		while i > 1 and aList[parent(i)] < aList[i]:
			exch(aList, i, parent(i))
			i = parent(i)


	# Fixes the tree down when items are removed
	# Precondition: The first parameter should be a list, the second and third both integers
	# Postcondition: Sets a new j value

	def fixDown(self, aList, i, n):
		while left(i) < n:
			j = left(i)
			if (j+1 < n) and (aList[j] < a[j+1]):
				j+=1
			if not (aList[i] < aList[j]):
				break
			exch(aList,i,j)
			i = j
			
			
	# Exchanges the position of two items in a list
	# Precondition: A list should be entered as a parameter as well as two indices
	# Postcondition: The two indices of the list are swapped
			
	def exch(self, aList, i, j):
		t = aList[i]
		aList[i] = aList[j]
		aList[j] = t
		
		
	# Returns the parents of the given index
	# Precondition: Takes in an index value
	# Postcondition: Returns the parent of index i
	
	def parent(i):
		return i // 2
		
		
	# Returns the left of the given index
	# Precondition: Takes in an index value
	# Postcondition: Returns the left of index i
		
	def left(i):
		return 2*i


	# Returns the right of the given index
	# Precondition: Takes in an index value
	# Postcondition: Returns the right of index i
	
	def right(i):
		return 2*i+1
		