####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Document Stream
# Summary: The Document Stream class allows a document to be analyzed and broken down into sentence objects. The class takes a file as an optional parameter and has class variables for title and author. The readWhole function reads the file and returns it as a list of sentence objects. The writeWhole function prints the sentence objects out. The stripTitle and stripAuthor functions parse the title and author information from the file respectively.
####################################################################################################################################################################


import csv
import sys
from Sentence import *


class DocumentStream:


	# Initializes Document stream with an optional attribute fileName
	# Precondition: A file name can be inputted
	# Postcondition: Sets title and author to None and creates a sentence list variable
		
	def __init__(self, fileName = None):
		self.fileName = fileName
		self.title = None
		self.author = None
		self.sentenceList = []


	# Reads the document and return a list of sentence objects based on punctuation
	# Precondition: A file name must have been entered as a parameter to the class
	# Postcondition: Returns the list of sentence objects
		
	def readWhole(self):

		f = open(self.fileName, 'r')

		index = 0
		sentenceList = [Sentence()]
		c = f.read(1)

		while (c != ""):
			#if not[c in ".?!;"]:
			if c not in [".","?","!",";"]:
				sentenceList[index].data += str(c)
				print("added word to sentence " + str(index))

			elif c in [".","?","!",";"]:
				sentenceList[index].punctuation = str(c)
				print("added punctuation to sentence " + str(index))
				sentenceList.append(Sentence())
				index += 1

			c = f.read(1)
			
		self.sentenceList = sentenceList

		return sentenceList


	# Prints the whole document out using the data and punctuation of each sentence objects with one sentence per output line
	# Precondition: The generateWhole function must be called first to generate the sentenceList
	# Postcondition: Prints the data and punctuation of each sentence object in sentenceList
		
	def writeWhole(self):
		for i in self.sentenceList:
			print (self.sentenceList[i].data + self.sentenceList[i].punctuation)


	# Strips the title information from the file
	# Precondition: A file name must have been entered as a parameter of the class
	# Postcondition: Returns the title of the file
		
	def stripTitle(self):
		gutenberg = False
		for i in self.sentenceList:
			words = i.parseWords()
			for j in words:
				if j == "Gutenberg":
					gutenberg = True

		if gutenberg == True:
			for i in self.sentenceList:
				words = i.parseWords()
				for j in words:
					if j == "Title:":
						title = words[(j+1):]
		
		self.title = title
						
		return title


	# Strips the author information from the file
	# Precondition: A file name must have been entered as a parameter of the class
	# Postcondition: Returns the author of the file
		
	def stripAuthor(self):
		gutenberg = False
		for i in self.sentenceList:
			words = i.parseWords()
			for j in words:
				if j == "Gutenberg":
					gutenberg = True

		if gutenberg == True:
			for i in self.sentenceList:
				words = i.parseWords()
				for j in words:
					if j == "Author:":
						author = words[(j+1):]
						
		self.author = author
						
		return
