import csv
import sys

class Sentence:
	def __init__(self):
		self.data = []
		self.wordCount = None
		self.charCount = None
		self.punctuation = ""

	# Returns an array of words in the file
	def parseWords():
		word_array = []
		word_array = self.data.split()
		return word_array


	# Returns an array of characters in the sentences of the file
	def parseChar():
		#for x in self.data character array.append(x)
		char_array = []

		for x in self.data:
			char_array.append(x)

		return char_array
