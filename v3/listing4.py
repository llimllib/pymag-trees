def layout(tree):
    setup(tree)
    addmods(tree)
    return tree

def setup(tree, depth=0, nexts=None, offset=None):
    if nexts is None:  nexts  = defaultdict(lambda: 0)
    if offset is None: offset = defaultdict(lambda: 0)

    for c in tree.children:
        setup(c, depth+1, nexts, offset)

    tree.y = depth
    
    if not len(tree.children):
        place = nexts[depth]
        tree.x = place
    elif len(tree.children) == 1:
        place = tree.children[0].x - 1
    else:
        s = (tree.children[0].x + tree.children[1].x)
        place = s / 2

    offset[depth] = max(offset[depth], nexts[depth]-place)

    if len(tree.children):
        tree.x = place + offset[depth]

    nexts[depth] += 2
    tree.offset = offset[depth]

def addmods(tree, modsum=0):
    tree.x = tree.x + modsum
    modsum += tree.offset

    for t in tree.children:
        addmods(t, modsum)
