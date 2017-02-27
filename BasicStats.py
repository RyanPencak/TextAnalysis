####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Basics Stats
# Summary: This class handles the statistics used to analyze the documents. It can calculate the frequency map of a list of words using linked lists using the function slinkFreq. It also determines the top and bottom N words using heaps in the functions topNHeap and bottomNHeap.
####################################################################################################################################################################


import csv
import sys
import heapq


class BasicStats:


	# Takes a list and returns values of frequencies of entry types in the list
	# Precondition: A list of words in inputted into the function
	# Postcondition: A dictionary of frequencies is returned
	# Time Analysis: O(n)
	
	@staticmethod
	def createFreqMap(words):
		freqDict = {}
		for i in words:
			if freqDict.get(i) == None:
				# Insert i as a key with frequency 1
				freqDict[i] = 1
			else:
				# This key is already in the dictionary
				# Increment the value of this key by 1
				freqDict[i] += 1

		return freqDict


	# Takes a list and returns values of frequencies of entry types in the list
	# Precondition: A list of words in inputted into the function
	# Postcondition: A linked list of frequencies is returned
	# Time Analysis: O(n) or O(n^2) if put directly into a linked list
	
	def slinkFreq(words):
		freqLL = sllist()
		found = False
		
		for i in words:
			
			runner = freqLL.head
			
			while (runner != None) and (found is False):
				
				if (runner.data == i):
					found = True
				runner = runner.next
				
			if (found is True):
				runner.freq += 1

			else:
				newNode = Node()
				newNode.data = i
				newNode.next = freqLL.head
				freqLL.head = newNode

		return freqLL


	# The top N most frequent words are determined with topNHeap
	# Precondition: A heap that is not None is entered as the first parameter and a positive variable n is entered for the second
	# Postcondition: A list of the top N most frequent words is returned with their frequencies
	# Time Analysis: 

	def topNHeap(heap,n):
		for sentence in self.sentenceList:
			for word in sentence:
				heap.heappush(heap, word)

		heapq.nlargest(n,heap)


	# The top N most frequent words are determined with topNHeap
	# Precondition: A heap that is not None is entered as the first parameter and a positive variable n is entered for the second
	# Postcondition: A list of the bottom N least frequent words is returned with their frequencies
	# Time Analysis: 

	def bottomNHeap(heap,n):
		for sentence in self.sentenceList:
			for word in sentence:
				heapq.heappush(heap, word)

		heapq.nsmallest(n,heap)


	# Takes a dictionary and a value n and returns a dictionary with keys being the top keys in the given dictionary
	# Precondition: A dictionary that is not None is entered as the first parameter and a positive variable n is entered for the second
	# Postcondition: A dictionary of the top N most frequent words is returned with their frequencies
	# Time Analysis: O(n)
	
	def topN(d, n):
		counter = 0
		minFreq = 99999999999999999999999999
		minFreqKey = None
		topD = {}
		for i in d:
			if counter < n:
				topD[i] = d[i]

			else:
				for j in topD:
					if topD[j] < minFreq:
						minFreq = topD[j]
						minFreqKey = j

					if d[i] > topD[j]:
						del topD[minFreqKey]
						topD[i] = d[i]

						# First Method: topd[minFreqKey] = d[i]

			counter += 1

		return topD


	# Takes a dictionary and a value n and returns a dictionary with keys being the bottom keys in the given dictionary
	# Precondition: A dictionary that is not None is entered as the first parameter and a positive variable n is entered for the second
	# Postcondition: A dictionary of the bottom N least frequent words is returned with their frequencies
	# Time Analysis: O(n)

	def bottomN(d, n):
		counter = 0
		maxFreq = 0
		maxFreqKey = None
		bottomD = {}
		for i in d:
			if counter < n:
				bottomD[i] = d[i]

			else:
				for j in bottomD:
					if bottomD[j] > maxFreq:
						maxFreq = bottomD[j]
						maxFreqKey = j

					if d[i] < bottomD[j]:
						del bottomD[j]
						bottomD[i] = d[i]
						# First Method: topD[maxFrequencyKey] = d[i]

			counter += 1

		return bottomD


# Takes a dictionary and a value n and returns a dictionary with keys being the top keys in the given dictionary
# Precondition: A dictionary that is not None is entered as the first parameter and a positive variable n is entered for the second
# Postcondition: A dictionary of the top N most frequent words is returned with their frequencies

def topNLL(l, n):	
	templ = SStack()
	runner = l.head
	while (templ.size < n):
		minFreq = sys.maxint
		while (runner != None):
			if (runner.data < minFreq):
				minFreq = runner.data
			runner = runner.next
		templ.push(minFreq)
		