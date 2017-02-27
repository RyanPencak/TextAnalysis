####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Document
# Summary: The Document class will act as the primary data type for this project. It has private variables for wordCount, lineCount, and charCount. It takes in a file name in its initialization. Getters and setters for the private variables are contained in this class. The function generateWhole will create class variables doc, sentenceList, title, and author. File print prints the entire file and getWordList returns a list of words in the document.
####################################################################################################################################################################


import csv
import sys
from Sentence import *
from DocumentStream import *
from BasicStats import *


class Document:


	# Initializes Document with a fileName and creates private variables wordCount, lineCount, and charCount
	# Precondition: A valid file name must be inputted as a parameter to initialize a document
	# Postcondition: Nothing is returned
		
	def __init__(self, fileName):
		self.id = id
		self._wordCount = 0
		self._lineCount = 0
		self._charCount = 0
		self._year = None
		self._genre = None
		self.fileName = fileName


	# Finds the word count of the document if it is not already found and returns the value
	# Precondition: Word count is returned if already determined
	# Postcondition: Returns private variable wordCount
		
	def getWordCount(self):
		if self._wordCount == None:
			count = 0
			with open(filename, 'r') as f:
				for line in f:
					for word in line.split():
						count += 1
		else:
			return self._wordCount


	# Sets the word count of the document
	# Precondition: Takes a word count to set the private variable
	# Postcondition: Sets the private variable wordCount
			
	def setWordCount(self, x):
		self._wordCount = x
	
	
	# Gets the year of the document
	# Precondition: None
	# Postcondition: Returns the year of the document
	
	def getYear(self):
		return self._year
	
	
	# Sets the year of the document
	# Precondition: Takes in the year of document as x
	# Postcondition: Sets the year of the document
	
	def setYear(self, x):
		self._year = x
	
	
	# Gets the genre of the document
	# Precondition: None
	# Postcondition: Returns the genre of the document
		
	def getGenre(self):
		return self._year
	
	
	# Sets the genre of the document
	# Precondition: Takes in the genre of the document as x
	# Postcondition: Sets the genre of the document
	
	def setGenre(self, x):
		self._genre = x


	# Finds the line count of the document if not already found and returns the value
	# Precondition: Line count is returned if already determined
	# Postcondition: Returns private variable lineCount
	
	def getLineCount(self):
		if self._lineCount == None:
			count = 0
			with open(filename, 'r') as f:
				for line in f:
					count += 1
		else:
			return self._lineCount


	# Sets the line count of the document
	# Precondition: Takes a line count to set the private variable
	# Postcondition: Sets the private variable lineCount
	
	def setLineCount(self, x):
		self._lineCount = x


	# Returns the character count of the document
	# Precondition: None
	# Postcondition: Returns private variable charCount
	
	def getCharCount(self):
		return self._charCount


	# Sets the character count of the document
	# Precondition: Takes a Character count to set the private variable
	# Postcondition: Sets the private variable charCount
	
	def setCharCount(self, x):
		self._charCount = x


	# Uses the getWhole method in DocumentStream and parses the title and author information
	# Precondition: Uses the file parameter of the document class to create a DocumentStream object
	# Postcondition: Sets class variables doc, sentenceList, title, author
		
	def generateWhole(self):
		
		self.doc = DocumentStream(self.fileName)
		self.sentenceList = self.doc.readWhole()
		self.title = self.doc.stripTitle()
		self.author = self.doc.stripAuthor()


	# Prints the entire file using the writeWhole method of the DocumentStream class
	# Precondition: generateWhole method must be called first so that doc is created
	# Postcondition: writeWhole prints the document
		
	def filePrint(self):
		self.doc.writeWhole(self.sentenceList)


	# Calls parse from sentences to get list of words
	# Precondition: File name entered in initialization
	# Postcondition: List of word wordList is returned
		
	def getWordList(self):

		f = open(self.fileName, 'r')
		wordList = []
		for word in f:
			wordList.append(word)
		return wordList
