import csv
import sys

class CommandLinePlotter:

	# Generates a 2D coordinate plane given a start and end point for x and y axis
	def coordinateGenerator(x_start, x_end, y_start, y_end):
		coordinates = []
		for x in range(x_end - x_start):
			for y in range(y_end - y_start):
				coordinates.append((x,y))

		return coordinates


	# Takes two lists with list 2 default to 0. First list is x coordinate, second is y coordinate
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
