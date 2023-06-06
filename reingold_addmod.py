from sys import stdout


class DrawTree:
    def __init__(self, tree, depth=-1):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = []
        self.thread = None
        self.mod = 0

    def left(self):
        return self.thread or len(self.children) and self.children[0]

    def right(self):
        return self.thread or len(self.children) and self.children[-1]

# traverse to the bottom of the tree, and place the leaves at an arbitrary
#   x coordinate
# if the node is a parent, draw its subtrees, then shift the right one as close
#   to the left as possible
# place the parent in the middle of the two trees.


def layout(tree):
    dt = reingold_tilford(tree)
    return addmods(dt)


def addmods(tree, mod=0):
    tree.x += mod
    for c in tree.children:
        addmods(c, mod + tree.mod)
    return tree


def reingold_tilford(tree, depth=0):
    dt = DrawTree(tree, depth)
    if len(tree) == 0:
        dt.x = 0
        return dt

    if len(tree) == 1:
        dt.children = [reingold_tilford(tree[0], depth + 1)]
        dt.x = dt.children[0].x
        return dt

    left = reingold_tilford(tree[0], depth + 1)
    right = reingold_tilford(tree[1], depth + 1)

    dt.children = [left, right]
    dt.x = fix_subtrees(left, right)
    return dt

# place the right subtree as close to the left subtree as possible


def fix_subtrees(left, right):
    li, ri, diff, loffset, roffset, lo, ro \
        = contour(left, right)
    diff += 1
    diff += (right.x + diff + left.x) % 2  # stick to the integers

    right.mod = diff
    right.x += diff
    if right.children:
        roffset += diff

    # right was deeper than left
    if ri and not li:
        lo.thread = ri
        lo.mod = roffset - loffset
    # left was deeper than right
    elif li and not ri:
        ro.thread = li
        ro.mod = loffset - roffset

    return (left.x + right.x) / 2


def contour(left,
            right,
            max_offset=None,
            loffset=0,
            roffset=0,
            left_outer=None,
            right_outer=None):
    if not max_offset \
            or left.x + loffset - (right.x + roffset) > max_offset:
        max_offset = left.x + loffset - (right.x + roffset)

    if not left_outer:
        left_outer = left
    if not right_outer:
        right_outer = right

    lo = left_outer.left()
    li = left.right()
    ri = right.left()
    ro = right_outer.right()

    if li and ri:
        loffset += left.mod
        roffset += right.mod
        return contour(li, ri, max_offset, loffset, roffset, lo, ro)

    return li, ri, max_offset, loffset, roffset, left_outer, right_outer

# given an array of nodes, print them out reasonably on one line


def printrow(level):
    x = dict((t.x, t.tree) for t in level)
    for i in range(max(x.keys()) + 1):
        try:
            stdout.write(str(x[i])[:4])
        except:
            stdout.write("    ")


def p(tree):
    level = [tree]
    while 1:
        newlevel = []
        printrow(level)
        for t in level:
            newlevel.extend(t.children[:2])
        print
        if not newlevel:
            break
        level = newlevel


if __name__ == "__main__":
    def mirror(t):
        if len(t.children) > 1:
            t.children = (t.children[1], t.children[0])
        for c in t.children:
            mirror(c)
        return t

    from demo_trees import trees
    layout(mirror(trees[10]))

# root = gentree("/Users/llimllib/Movies")
# root.children.reverse()
# drawtree = reingold_tilford(root)
# p(drawtree)
