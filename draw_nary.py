from gen import Tree
from demo_trees import trees
import reingold_thread; reload(reingold_thread)
from reingold_thread import reingold_tilford as rt
#from reingold_naive import reingold_tilford as rt
import buchheim; reload(buchheim)
from buchheim import buchheim

t = buchheim(trees[6])
#t = rt(trees[4])

r = 30
rh = r*1.5
rw = r*1.5
stroke(0)

def drawt(root, depth):
    global r
    oval(root.x * rw, depth * rh, r, r)
    for child in root.children:
        drawt(child, depth+1)

def drawconn(root, depth):
    for child in root.children:
        line(root.x * rw + (r/2), depth * rh + (r/2),
             child.x * rw + (r/2), (depth+1) * rh + (r/2))
        drawconn(child, depth+1)

def sign(x):
    if x == 0: return 0
    if x > 0:  return 1
    else:      return -1

from math import atan, sin, cos, pi
def dottedline(x1, y1, x2, y2):
    segment = 5
    if x2 == x1: print "fucked up"; return
    if x2 - x1 > 0:
        theta = atan(float(y2-y1)/float(x2-x1))
    else:
        theta = pi + atan(float(y2-y1)/float(x2-x1))
    
    dx = cos(theta) * segment
    dy = sin(theta) * segment
    xdir = x1 < x2
    ydir = y1 < y2
    
    while 1:
        if xdir != (x1 < x2) or ydir != (y1 < y2): break
        line(x1, y1, x1+dx, y1+dy)
        x1, y1 = x1+2*dx, y1+2*dy

def drawthreads(root, depth):
    for child in root.children:
        c = child.thread
        if c:
            dottedline(child.x * rw + (r/2), (depth+1) * rh + (r/2),
                       c.x * rw + (r/2), (depth+2) * rh + (r/2))
        drawthreads(child, depth+1)

size(500, 500)
translate(2, 2)
drawconn(t, 0)
stroke(0,.4,.6)
drawthreads(t, 0)
stroke(0)
fill(1,1,1)
drawt(t, 0)