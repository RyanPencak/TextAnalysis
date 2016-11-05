import csv
import sys
from Document import *
from CommandLinePlotter import *
from BasicStats import *
from tkinter import Tk, Label, Button, Entry, StringVar, END, W, E
from UserGui import *
from MatPlotPloter import *
#import DocumentStreamError
#import MatPlotPloter
#import UserInputError

def main():

	# Ask user to input a file name
	# f = input ("Enter a file name:")

	# Using the GUI to get user input and store file in f
	root = Tk()
	my_gui = UserGui(root)
	f = root.mainloop()


def mainwork(f):
	# Create a document object with the fileName
	doc = Document(f)

	# Use generateWhole method to read the file in
	doc.generateWhole(f)

	# parse words from document
	words = doc.getWordList()

	# call createFreqMap to get frequencies of words in parsed words
	d = createFreqMap(words)

	# call topN where n = 10 on the dictionary of parsed words
	freq = topN(d, 10)

	# use scatter to get scatter plot of frequencies (only input frequencies)
	scatter(freq)
	barPlot(freq)


if __name__ == "__main__":
	main()
