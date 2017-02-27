####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Command Line Plotter
# Summary: This class utilizes the command line to create a coordinate plane and creates a scatter plot given one or two lists. The coordinate generator creates coordinates based on the paramters for the start and end of x and y. TwoDScatter creates a scatter plot when given one or two lists. This is used to generate a scatter plot of frequencies of words.
####################################################################################################################################################################


import csv
import sys
import os

class CommandLinePlotter:
	

	# Initializes the class with coordinates
	# Precondition: None
	# Postcondition: Initializes the class with a list of coordinates
	
	def __init__(self):
		self.coordinates = []


	# Generates a 2D coordinate plane given a start and end point for the x and y axis
	# Precondition: Four parameters must be entered for the start and end of both x and y
	# Postcondition: An array acting as a coordinate plane is returned
	
	def coordinateGenerator(xStart, xEnd, yStart, yEnd):
		coordinates = []
		for x in range(x_end - x_start):
			for y in range(y_end - y_start):
				coordinates.append((x,y))

		return coordinates


	# Takes two lists with the second list defaulting to 0. The first list is x coordinate and the second is y coordinate
	# Precondition: At least one list must be entered. If one is entered it will become the y axis. If two are entered it will be x and y respectively
	# Postcondition: The coordinates are printed and the scatter plot is displayed
		
	def TwoDScatter(x, y = None):

		if y == None:
			y = x
			x = range(len(y))

		maxInput = 0
		lines = os.get_terminal_size().lines
		y_scale_factor = maxInput/lines
		ynew = y/y_scale_factor

		for i in x:
			for ii in y:
				coordinates[i,ii] = X

		print (coordinates)
