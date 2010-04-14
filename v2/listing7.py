from operator import lt, gt

def push_right(left, right):
    wl = contour(left, lt)
    wr = contour(right, gt)
    return max(x-y for x,y in zip(wl, wr)) + 1
    
def contour(tree, comp, level=0, cont=None):
    if not cont: 
        cont = [tree.x]
    elif len(cont) < level+1:
        cont.append(tree.x)
    elif comp(cont[level], tree.x):
        cont[level] = tree.x

    for child in tree.children:
        contour(child, comp, level+1, cont)

    return cont
