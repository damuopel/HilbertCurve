from turtle import *
import numpy as np
from math import floor
WIDTH, HEIGHT = 400, 400

l = 1 # Level (>=1)
verts = 4
nx = 2**l
ny = 2**l
h = WIDTH//nx # Both sides have the same length
x = np.linspace(h/2,h*(nx-1/2),nx)
y = np.linspace(h/2,h*(ny-1/2),ny)
x, y = np.meshgrid(x,y)
xy = np.array([x.flatten(),y.flatten()])
n1 = np.array([i+floor(i/nx) for i in range((nx-1)*(ny-1))])
n2 = n1 + 1
n3 = n2 + nx
n4 = n1 + nx
Topology = np.array([n1,n2,n3,n4])

# Setup Turtle
screen = Screen()
screen.setup(WIDTH, HEIGHT)
hideturtle()
speed(1)
# Locate Turtle in origin
penup()
goto(xy[0,0]-WIDTH/2, xy[1,0]-HEIGHT/2)
pendown()

for i in range(0,(nx-1)*(ny-1)):
    Verts = Topology[:,i]
    for j in range(0,verts):
          coords = xy[:,Verts[j]] 
          goto(int(coords[0]-WIDTH/2),int(coords[1]-HEIGHT/2))
