####################################################################################################################################################################
# Name: Ryan Pencak
# Class: MatPlot Plotter
# Summary: The MatPlot Plotter class has two methods to plot different types of graphs. The method scatter plots a scatter graph using matplotlib and the method barPlot plots a bar graph using matlibplot
####################################################################################################################################################################


import csv
import sys
# import matplotlib.pyplot as plt
# import numpy as np


class MatPlotPlotter():


	# Creates a scatter plot using pyplot in matplotlib
	# Precondition: Lists of variable x and y. One list of variables will default to y variables if only one list is entered
	# Postcondition: Outputs a pyplot scatter plot of the data
	
	def scatter(x, y = None):
		if y == None:
			y = x
			x = range(len(y))

		N = 50
		colors = np.random.rand(0, N)
		area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
		ax.set_ylabel('Word')
		ax.set_title('Frequency')
		plt.scatter(x, y, s=area, c=colors, alpha=0.5)
		plt.show()


	# Creates a bar plot using pyplot in matplotlib
	# Precondition: Lists of variable x and y. One list of variables will default to y variables if only one list is entered
	# Postcondition: Outputs a pyplot bar plot of the data
	
	def barPlot(x, y = None):
		if y == None:
			y = x
			x = range(len(y))

		N = len(x)

		ind = np.arange(N)  # the x locations for the groups
		width = 0.35       # the width of the bars

		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, menMeans, width, color='r', yerr=y)

		# add text for labels, title and axes ticks
		ax.set_ylabel('Word')
		ax.set_title('Frequency')
		ax.set_xticks(ind + width)
		ax.set_xticklabels()

		ax.legend((rects1[0]), (Frequency))

		plt.show()
