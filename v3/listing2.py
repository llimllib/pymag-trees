i = 0
def knuth_layout(tree, depth):
    if tree.left_child: 
        knuth_layout(tree.left_child, depth+1)
    tree.x = i
    tree.y = depth
    i += 1
    if tree.right_child: 
        knuth_layout(tree.right_child, depth+1)
