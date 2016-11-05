import csv
import sys
from Sentence import *
from DocumentStream import *

class Document:
	def __init__(self, fileName):
		self.id = id
		self.wordCount = 0
		self.lineCount = 0
		self.charCount = 0
		self.fileName = fileName

	# Finds this values if not already found and returns them or the value if generated
	def getWordCount(self):
		if self.wordCount == None:
			count = 0
			with open(filename, 'r') as f:
						for line in f:
							for word in line.split():
								count += 1

		else:
			return self.wordCount


	# wordCount Setter
	def setWordCount(self, x):
		self.wordCount = x


	# Finds this values if not already found and returns them or the value if generated
	def getLineCount(self):
		if self.lineCount == None:
			count = 0
			with open(filename, 'r') as f:
				for line in f:
					count += 1

		else:
			return self.lineCount


	# lineCount Setter
	def setLineCount(self, x):
		self.lineCount = x


	# charCount Getter
	def getCharCount(self):
		return self.charCount

	# charCount Setter
	def setCharCount(self, x):
		self.charCount = x

	# Uses method getWhole in DocumentStream and parse the title information given a file
	def generateWhole(self, fileName):
		d = DocumentStream(fileName)
		self.sl = d.readWhole()
		#title = file.readline()

	def filePrint(self, fileName):
		writeWhole(self.sl, fileName)

	# call parse from sentences to get list of words
	def getWordList(self):
		self.words = self.sl.parsewords()
