from collections import defaultdict


class DrawTree(object):
    def __init__(self, tree, depth=-1):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(t) for t in tree]
        self.thread = None
        self.offset = 0


def layout(tree):
    dt = DrawTree(tree)
    setup(dt)
    addmods(dt)
    return dt


def setup(tree, depth=0, nexts=None, offset=None):
    if nexts is None:
        nexts = defaultdict(lambda: 0)
    if offset is None:
        offset = defaultdict(lambda: 0)

    for c in tree.children:
        setup(c, depth + 1, nexts, offset)

    tree.y = depth

    if not len(tree.children):
        place = nexts[depth]
        tree.x = place
    elif len(tree.children) == 1:
        place = tree.children[0].x - 1
    else:
        s = (tree.children[0].x + tree.children[1].x)
        print(tree.children[0].x, tree.children[1].x, tree.tree)
        place = s / 2

    offset[depth] = max(offset[depth], nexts[depth] - place)

    if len(tree.children):
        tree.x = place + offset[depth]

    nexts[depth] += 2
    tree.offset = offset[depth]


def addmods(tree, modsum=0):
    tree.x = tree.x + modsum
    modsum += tree.offset

    for t in tree.children:
        addmods(t, modsum)
