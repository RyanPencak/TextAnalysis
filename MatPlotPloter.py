
class MatPlotPloter():

	def scatter(x, y = None):
		if y == None:
			y = x
			x = range(len(y))

		N = 50
		colors = np.random.rand(N)
		area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses
		ax.set_ylabel('Word')
		ax.set_title('Frequency')
		plt.scatter(x, y, s=area, c=colors, alpha=0.5)
		plt.show()

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

		#autolabel(rects1)
		#autolabel(rects2)

		plt.show()


	'''def autolabel(rects):
    	# attach some text labels
    	for rect in rects:
        	height = rect.get_height()
        	ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
            	'%d' % int(height),
            	ha='center', va='bottom')'''
