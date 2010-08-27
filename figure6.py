from gen import Tree
from math import atan, cos, sin, pi
import demo_trees; reload(demo_trees)
from demo_trees import trees
from buchheim import buchheim as layout

tree = trees[4][1]
tree[0][1].children.append(Tree("a"))
tree[0][1].children.append(Tree("b"))
t = layout(trees[4][1])

r = 30
rh = r*1.5
rw = r*2
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

def dottedline(x1, y1, x2, y2):
    segment = 5
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

size(130, 180)
translate(2, 2)
stroke(0)
drawconn(t, 0)
drawthreads(t, 0)
fill(1,1,1)
drawt(t, 0)