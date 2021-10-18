
'''
###   Owned by @akshaysmin github akshaysmin@gmail.com   ###

Name : animator.py

Use : a handler for matplotlib animations

'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

#classes

class plotObject:
	def __init__(self, fig, ax, line=None, dsource=None, xlim=None, ylim=None, add=False):
		self.fig = fig
		self.ax = ax
		self.line = line
		self.dsource = dsource
		self.xlim = xlim
		self.ylim = ylim

		if add:	plotObject.add_object(self)

	objects = []

	def add_object(obj): plotObject.objects.append(obj)

	def remove_object(obj): plotObject.objects.remove(obj)

	def get_objects(): plotObject.objects


# functions

def data_source(x,y):
	pos = 0
	length = len(x)
	while pos <=length:
		if pos == length:
			pos = 0
		yield x[pos], y[pos]
		pos += 1
		

def _animate(i, plot_object):
	dsource = plot_object.dsource
	mat = plot_object.line
	mat.set_data(next(dsource))
	return mat,

def animate(plot_object,interval=50, frames=100):

	dsource = plot_object.dsource

	mat, = ax.plot(next(dsource), 'o')
	ax.set_xlim(plot_object.xlim)
	ax.set_ylim(plot_object.ylim)
	plot_object.line = mat

	# ax.axis([-15,5,-15,5])
	ani = animation.FuncAnimation(fig, _animate, interval=interval, frames=frames, fargs=(plot_object,))
	plt.show()

#main function
def animate_points(x,y,interval=50, frames=100): 
	global fig, ax
	fig, ax = plt.subplots()
	xlim = min(x),max(x)
	ylim = min(y), max(y)
	anim_object = plotObject(fig, ax, dsource=data_source(x,y), xlim = xlim, ylim = ylim)
	animate(anim_object,interval=interval, frames=frames)

def show(): plt.show()

# sample data for (3,4) matrix

points = [ (0,0), (1,1), (2,2), (1,3), (0,2), (1,1), (2,0)]
x = [0,1,2,1,0,1,2]
y = [0,1,2,3,2,1,0]

# global variables
path   = []
pathi = []
pathj = []
balls = zip(pathi,pathj)
fig, ax = plt.subplots()

#objects
animObject = plotObject(fig, ax, dsource=data_source(x,y))

