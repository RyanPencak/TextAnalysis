####################################################################################################################################################################
# Name: Ryan Pencak
# File: TextAnalysisMain
# Function: main
# Summary: This is the main function of the program. It launches the GUI which will handle to work for the program.
####################################################################################################################################################################


import csv
import sys
from Document import *
from CommandLinePlotter import *
from BasicStats import *
from tkinter import Tk, Label, Button, Entry, StringVar, END, W, E
from UserGui import *
#from MatPlotPloter import *
#import DocumentStreamError
#import UserInputError


# Main function for the program to run
# Precondition: None
# Postcondition: Launches the GUI and runs the program, returning the analysis which is the root of the mainloop of the GUI

def main():

	# Ask user to input a file name
	# f = input ("Enter a file name:")
	
	Files = input("Please enter the number of files will you be using." + "\n")
	
	numFiles = int(Files)

	# Using the GUI to get user input and store file in f
	root = Tk()
	GUI = UserGUI(root, numFiles)
	evaluation = root.mainloop()
	
	print(evaluation)


if __name__ == "__main__":
	main()
