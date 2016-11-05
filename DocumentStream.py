import csv
import sys
from Sentence import *

class DocumentStream:

	# Optional attribute fileName?
	def __init__(self, fileName = "None"):
		self.fileName = fileName
		self.title = None
		self.author = None

	# Read document and return a list of sentences divided based on punctuation or 3+ 	# punctuation
	def readWhole(self):

		f = open(self.fileName, 'r')

		index = 0
		sentenceList = [Sentence()]
		c = f.read(1)

		while (c != None):
			if not[c in ".?!;"]:
				sentenceList[index].data += c

			else:
				sentenceList[index].punctuation = c
				index += 1
				sentenceList.append(Sentence())

		return sentenceList

	# Writes the whole document out using sentences, one per output line
	def writeWhole(self, sl):
		for i in sl:
			print (sl[i].data + sl[i].punctuation)

	# Strips the title and author information from file
	def strip(self):
		gutenberg = False
		for i in sentenceList:
			words = i.parseWords()
			for j in words:
				if j == "Gutenberg":
					gutenberg = True

		if gutenberg == True:
			for i in sentenceList:
				words = i.parseWords()
				for j in words:
					if j == "Title:":
						self.title = words[j+1]
					if j == "Author:":
						self.author = words[j+1]
