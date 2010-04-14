nexts = [0] * maximum_depth_of_tree

def minimum_ws(tree, depth=0):
    tree.x = nexts[depth]
    tree.y = depth
    nexts[depth] += 1
    for c in tree.children:
        minimum_ws(tree, c)
