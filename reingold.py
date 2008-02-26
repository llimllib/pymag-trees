from gen import Tree, gentree
from operator import lt, gt
from sys import stdout

#traverse to the bottom of the tree, and place the leaves at an arbitrary
#   x coordinate
#if the node is a parent, draw its subtrees, then shift the right one as close
#   to the left as possible
#place the parent in the middle of the two trees.
def reingold_tilford(tree, depth=0):
    tree.y = depth
    if len(tree) == 0:
        tree.x = 0
        return tree

    if len(tree) == 1:
        tree.x = (reingold_tilford(tree, depth+1)).x
        return tree

    left = reingold_tilford(tree[0], depth+1)
    right = reingold_tilford(tree[1], depth+1)

    tree.x = fix_subtrees(left, right)
    return tree

#place the right subtree as close to the left subtree as possible
def fix_subtrees(left, right):
    wl = contour(left, lt)
    wr = contour(right, gt)
    diff = max(map(lambda (x,y): x-y, zip(wl,wr))) + 1
    #stick to the integers
    diff += (right.x + diff + left.x) % 2
    addtotree(right, diff)
    return (left.x + right.x) / 2

def addtotree(tree, val):
    tree.x += val
    if len(tree):
        for child in tree[:2]: addtotree(child, val)
    
def contour(tree, comp, level=0, cont=None):
    if not level: 
        cont = [tree.x]
    elif len(cont) < level+1:
        cont.append(tree.x)
    elif comp(cont[level], tree.x):
        cont[level] = tree.x

    for child in tree.children[:2]:
        contour(child, comp, level+1, cont)

    return cont

#given an array of nodes, print them out reasonably on one line
def printrow(level):
    x = dict((t.x, t) for t in level)
    for i in range(max(x.keys())+1):
        try: stdout.write(str(x[i])[:4])
        except: stdout.write("    ")

def p(tree):
    level = [tree]
    while 1:
        newlevel = []
        printrow(level)
        for t in level:
            #stdout.write("%s%s%s" % (t.x*"____", str(t)[:3], t.x))
            newlevel.extend(t[:2])
        print
        if not newlevel: break
        level = newlevel

root = gentree("/Users/llimllib/Movies")
root.children.reverse()
reingold_tilford(root)
p(root)
