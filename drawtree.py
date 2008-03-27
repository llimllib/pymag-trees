from gen import Tree
from reingold_thread import reingold_tilford as rt

tree = Tree("root", [
     Tree("l1", [
       Tree("l2", [
         Tree("l3", [
           Tree("l4")])])]),
     Tree("r1")])
t1 = rt(tree)

tree = Tree("root", [
     Tree("l1", [
       Tree("l2", [
         Tree("l3"), Tree("l4")])]),
     Tree("r1", [
       Tree("rl1"),
       Tree("rr1", [
         Tree("rr2"), Tree("rr3")])])])
t2 = rt(tree)

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

size(260, 210)
translate(2, 2)
drawconn(t2, 0)
fill(1,1,1)
drawt(t2, 0)
fill(0)
font("Georgia-Italic", 20)
#text("Figure 1: A tree for testing", 12, 200, outline=True)
p = textpath("Figure 1: A tree for testing", 12, 200)
drawpath(p)