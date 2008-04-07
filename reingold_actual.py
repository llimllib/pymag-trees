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

class Extreme(object):
    def __init__(self, tree, level, offset):
        self.tree = tree
        self.level = level
        self.offset = offset

def layout(tree):
    setup(DrawTree(tree), 0, None, None)

minsep = 1
def setup(T, level, rmost, lmost):
    if T is None: 
        rmost = lmost = -1
        return

    T.y = level
    L = T.left()
    R = T.right()

    LL = LR = RR = RL = None
    setup(L, level+1, LR, LL)
    setup(R, level+1, RR, RL)

    #T is a leaf
    if not R and not L:
        rmost = Extreme(T, level, 0)
        lmost = Extreme(T, level, 0)
        T.offset = 0
        return

    cursep = rootsep = minsep
    loffsum = roffsum = 0

    while L and R:
        if cursep < minsep:
            rootsep += minsep - cursep
            cursep = minsep
        if L.right():
            loffsum += L.offset
            cursep -= L.offset
            L = L.right()
        else:
            loffsum -= L.offset
            cursep += L.offset
            L = L.left()
        if R.left():
            loffsum -= R.offset
            cursep -= R.offset
            R = R.left()
        else:
            loffsum += R.offset
            cursep += R.offset
            R = R.right()

    T.offset = (rootsep + 1) / 2
    loffsum -= T.offset
    roffsum += T.offset

    #XXX: why aren't RL and LL always None?
    if RL.level > LL.level or not T.left():
        lmost = RL
        lmost.offset += T.offset
    else:
        lmost = LL
        lmost.offset -= T.offset

    if LR.level > RR.level or not T.right():
        rmost = LR
        rmost.offset -= T.offset
    else:
        rmost = RR
        rmost.offset += T.offset

    if L and L != T.left():
        RR.tree.offset = abs(RR.offset + T.offset - loffsum)
        RR.tree.thread = L              #XXX:is .thread == llink and rlink?
    elif R and R != T.right():
        LL.tree.offset = abs(LL.offset - T.offset - roffsum)
        LL.tree.thread = R
