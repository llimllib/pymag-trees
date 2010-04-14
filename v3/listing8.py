def nextright(tree):
    if tree.thread:   return tree.thread
    if tree.children: return tree.children[-1]
    else:             return None

def nextleft(tree):
    if tree.thread:   return tree.thread
    if tree.children: return tree.children[0]
    else:             return None

def contour(left, 
            right, 
            max_offset=0, 
            left_outer=None, 
            right_outer=None):
    if not left_outer:
        left_outer = left
    if not right_outer:
        right_outer = right

    if left.x - right.x > max_offset:
        max_offset = left.x - right.x

    lo = nextleft(left)
    li = nextright(left)
    ri = nextleft(right)
    ro = nextright(right)

    if li and ri:
        return contour(li, ri, max_offset, lo, ro)

    return max_offset
