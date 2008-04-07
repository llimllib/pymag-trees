from gen import Tree, gentree
from operator import lt, gt
from sys import stdout

class DrawTree:
    def __init__(self, tree, parent, depth=-1):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(t, self, depth+1) for t in tree]
        #XXX: how else do I determine if a node has a left brother?
        #     Should this be here when I have to maintain the ancestor node anyway
        self.parent = parent
        self.thread = None
        self.mod = None
        self.ancestor = self

    def left(self): 
        return self.thread or len(self.children) and self.children[0]

    def right(self):
        return self.thread or len(self.children) and self.children[-1]

    def lbrother(self):
        n = None
        for node in self.parent.children:
            if node == self: return n
            else:            n = self

def walker(tree):
    dt = DrawTree(tree, None, 0)
    firstwalk(tree)
