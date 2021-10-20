
'''
###   Owned by @akshaysmin github akshaysmin@gmail.com   ###

Name : bouncing_ball.py

Input : Matrix dimension
Task  : Trace locus of ball starting from path (0,0) -> (1,1) -> etc. 
        wih reflections from matrix boundaries untill it hits a corner
Output: All locations of ball [(0,0), (1,1), ... ] and plot

'''
print('Starting...')

import matplotlib.pyplot as plt
from animator import animate_points

# functions

def show(paths, preprocess=False, *args, **kwargs):

	for x,y in paths:
		if preprocess:
			x = map(lambda i: x_max-i, x)
		plt.plot(x,y,*args,**kwargs)

	x_max = max(x)
	y_max = max(y)

	all_x = []
	all_y = []
	for i in range(x_max+1):
		for j in range(y_max+1):	
			all_x.append(i)
			all_y.append(j)

	plt.plot(all_x, all_y, 'r*')
	animate_points(pathi,pathj,plot_lines=True, fill = 10)
	plt.show()

def recursivef(direction, loc , m,n):
	'''
	direction = (1,1), (-1,1), (-1,-1), (1,-1)
	loc = (i,j) = present location of ball
	m,n = matrix dimension = i_max, j_max

	we are assuming anticlockwise reflections 
	i.e., m<n and intial point = (0,0) 
	'''

	global path, path_i, path_j

	i,j = loc
	a,b = direction

	path.append((i,j))
	pathi.append(i)
	pathj.append(j)

	print(loc, direction)

	if not ( (0<=i+a<m) or (0<=j+b<n) ): return # checks if ball reached a corner

	if not (0<=i+a<m) : a,b = -a,b       # if ball crosses up or low boundaries, instead change its direction

	if not (0<=j+b<n) : a,b = a,-b       # if ball crosses left or right boundaries, instead change its direction

	i = i+a
	j = j+b

	loc = i,j
	direction = a,b

	recursivef(direction, loc , m,n)

def solve(direction, loc , m,n):

	global path, pathi, pathj
	paths = []

	recursivef(direction, loc , m,n)

	paths.append((pathi,pathj))
	path = []
	pathi = []
	pathj = []
	
	# for alternate path 	# Warning : Assumption that loc = (0,0)
	if (m-1,n-1) in paths[-1]:
		recursivef( (-1,1), (m-1,0) , m,n)
	else:
		recursivef( (-1,-1), (m,n) , m,n)

	paths.append((pathi,pathj))

	print(paths)
	show(paths)
	


# sample data for (3,4) matrix

points = [ (0,0), (1,1), (2,2), (1,3), (0,2), (1,1), (2,0)]
x = [0,1,2,1,0,1,2]
y = [0,1,2,3,2,1,0]

# global variables
path   = []
pathi = []
pathj = []
balls = zip(pathi,pathj)

loc = 0,0
direction = 1,1
m = 5
n = 6


if input('to change default values enter yes'):
	loc = input('loc [eg: 0,0] = ').strip().split(',')
	loc = [int(i) for i in loc ]
	m = int(input('rows = '))
	n = int(input('columns = '))
	direction = (1,1), (-1,1), (-1,-1), (1,-1)
	print("""Enter direction - 
		down right -> 1,1
		up right -> -1,1
		up left -> -1,-1
		down left -> 1,-1
		""")
	direction = input('direction = ').strip().split(',')
	direction = [int(i) for i in direction ]

solve(direction, loc , m,n)
