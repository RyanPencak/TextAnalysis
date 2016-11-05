import csv
import sys

class BasicStats:

	# Takes a list and the value returns values of frequencies of entry types in the list
	# O(n)
	@staticmethod
	def createFreqMap(words):
		d = {}
		for i in words:
			if d.get(i) == None:
				# insert i as a key.
				d[i] = 1
			else:
				# this key is already in the dictionary
				# increment the value of this key by 1
				d[i] += 1

		return d


	# Uses linked lists to create a frequency map
	# O(n)
	# If put directly into linked list: n^2
	def slinkFreq(words):
		s = sllist()
		found = False
		for i in words:
			runner = s.head
			while (runner != None) and (found is False):
				if (runner.data == i):
					found = True
			if (found is True):
				runner.freq += 1

			else:
				n = Node()
				n.data = i
				n.next = s.head
				s.head = n
				
		return s

		#store dictionary in list


	# Takes a dictionary and a value n and returns a dictionary with keys being the top keys
	# in the given dictionary
	# O(n)
	# input dictionary d, topD = {}, n = 3
	# counter = 0
	# for i in d:
	#   if counter < n:
	# 	   topd.add(i,d[i])
	#   else:
	#   for k in topd:
	#       if d[i] > topd[k]
	def topN(d, n):
		counter = 0
		minFreq = sys.maxint
		minFreqKey = None
		topd = {}
		for i in d:
			if counter < n:
				topd.add(i,d[i])

			else:
				for j in topd:
					if topd[j] < minFreq:
						minFreq = topd[j]
						minFreqKey = j

					if d[i] > topd[j]:
						topd[minFreqKey] = d[i]

			counter += 1

		return topd

	# go through list, find top n
	def topNL(l, n):
		templ = SStack()
		runner = l.head
		while (templ.size < n):
			minFreq = sys.maxint
			while (runner != None):
				if (runner.data < minFreq):
					minFreq = runner.data
				runner = runner.next
			templ.push(minFreq)


	# Takes a dictionary and a value n and returns a dictionary with keys being the bottom
	# keys in the given dictionary
	# Algorithm Analysis: n

	def bottomN(d, n):
		counter = 0
		maxFreq = 0
		maxFreqKey = None
		bottomd = {}
		for i in d:
			if counter < n:
				topd.add(i,d[i])

			else:
				for j in topd:
					if topd[j] > maxFreq:
						maxFreq = topd[j]
						maxFreqKey = j

					if d[i] < topd[j]:
						topd[maxFrequencyKey] = d[i]

			counter += 1

		return bottomd
