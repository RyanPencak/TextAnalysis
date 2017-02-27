####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Sentence
# Summary: The Sentence class creates a sentence object that is used in the document object. It is initialized with a string of data and a string of the punctuation ending the sentence, as well as a word count and a character count. It contains methods to parse words or parse characters.
####################################################################################################################################################################


import csv
import sys


class Sentence:
	
	
	# Initializes the sentence class
	# Precondition: None
	# Postcondition: Initializes the sentence object with data and punctuation strings, a word count, and a character count
	
	def __init__(self):
		self.data = ""
		self.punctuation = ""
		self.wordCount = None
		self.charCount = None


	# Returns an array of words in the file
	# Precondition: Must be called on a sentence object
	# Postcondition: Parses the words from a sentence object and returns a list of the words
	
	def parseWords(self):
		word_array = []
		word_array = self.data.split()
		return word_array


	# Returns an array of characters in the sentences of the file
	# Precondition: Must be called on a sentence object
	# Postcondition: Parses the characters from a sentence object and returns a list of the characters
	
	def parseChar(self):
		charArray = []
		for x in self.data:
			charArray.append(x)
		return charArray
