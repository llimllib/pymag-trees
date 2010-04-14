def layout(tree):
    return addmods(setup(dt))

def addmods(tree, mod=0):
    tree.x += mod
    for c in tree.children:
        addmods(c, mod+tree.mod)
    return tree

def setup(tree, depth=0):
    if len(tree.children) == 0:
        tree.x = 0
        tree.y = depth
        return tree

    if len(tree.children) == 1:
        tree.x = setup(tree.children[0], depth+1).x
        return tree

    left = setup(tree.children[0], depth+1)
    right = setup(tree.children[1], depth+1)

    tree.x = fix_subtrees(left, right)
    return tree
