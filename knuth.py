class DrawTree(object):
    def __init__(self, tree, depth=-1):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(t) for t in tree]
        self.thread = None
        self.offset = 0

    def left(self): 
        return self.thread or len(self.children) and self.children[0]

    def right(self):
        return self.thread or len(self.children) and self.children[-1]

def layout(tree):
    dt = DrawTree(tree)
    setup(dt)
    return dt

def setup(tree, i=0):
    if not tree: return i
    
    if len(tree.children) > 0: l = tree.children[0]
    else:                      l = None
    if len(tree.children) > 1: r = tree.children[1]
    else:                      r = None

    i = setup(l, i)
    tree.x = i
    i += 1
    return setup(r, i)
