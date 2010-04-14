class DrawTree(object):
    def __init__(self, tree, depth=0):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(t, depth+1) for t in tree]
