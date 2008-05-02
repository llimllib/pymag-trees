from gen import Tree
from demo_trees import trees
from buchheim import buchheim as layout

t = layout(trees[3][1])
t2 = layout(trees[3][0])

r = 30
rh = r*1.5
rw = r*1.5
stroke(0)

def drawt(root, depth, offset=0):
    global r
    oval((root.x * rw) + offset, depth * rh, r, r)
    fill(0)
    text(str(int(round(root.x*2, 0))), (root.x * rw) + rw/6 + offset, (depth * rh) + rh/2)
    fill(1)
    for child in root.children:
        drawt(child, depth+1, offset)

def drawconn(root, depth, offset=0):
    for child in root.children:
        line(root.x * rw + (r/2) + offset, depth * rh + (r/2),
             child.x * rw + (r/2) + offset, (depth+1) * rh + (r/2))
        drawconn(child, depth+1, offset)
        
size(1000, 500)
translate(2, 2)
stroke(0)
drawconn(t2, 0)
drawconn(t, 0, 80)
fill(1,1,1)
drawt(t2, 0)
drawt(t, 0, 80)