from gen import Tree
from demo_trees import trees
import ws2
reload(ws2)
from ws2 import layout

t = layout(trees[5])

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
        
size(1000, 500)
translate(2, 2)
stroke(0)
drawconn(t, 0)
fill(1,1,1)
drawt(t, 0)