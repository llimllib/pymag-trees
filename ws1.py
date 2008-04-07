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

def setup(tree, depth=0, nexts=None):
    if not nexts: nexts = []

    try:
        next = nexts[depth]
        nexts[depth] += 1
    except IndexError:
        next = 0
        nexts.append(1)

    tree.x = next
    tree.y = depth
    for c in tree.children:
        setup(c, depth+1, nexts)
