from gen import Tree, gentree
from operator import lt, gt
from sys import stdout

class DrawTree(object):
    def __init__(self, tree, parent=None, depth=0):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = [DrawTree(c, self, depth+1) for c in tree.children]
        #XXX: how else do I determine if a node has a left brother?
        #     Should this be here when I have to maintain the ancestor node anyway
        self.parent = parent
        self.thread = None
        self.mod = 0
        self.ancestor = self
        self.change = self.shift = 0
        self._lmost_sibling = None

    def left(self): 
        return self.thread or len(self.children) and self.children[0]

    def right(self):
        return self.thread or len(self.children) and self.children[-1]

    def lbrother(self):
        n = None
        if self.parent:
            for node in self.parent.children:
                if node == self: return n
                else:            n = node
        return n

    def get_lmost_sibling(self):
        if not self._lmost_sibling and self.parent and self != \
        self.parent.children[0]:
            self._lmost_sibling = self.parent.children[0]
        return self._lmost_sibling
    lmost_sibling = property(get_lmost_sibling)

def buchheim(tree):
    dt = firstwalk(DrawTree(tree))
    second_walk(dt)
    return dt

def firstwalk(v, distance=2):
    if len(v.children) == 0:
        if v.lmost_sibling:
            v.x = v.lmost_sibling.x + distance
        else:
            v.x = 0
    else:
        default_ancestor = v.children[0]
        for w in v.children:
            firstwalk(w)
            default_ancestor = apportion(w, default_ancestor)
        execute_shifts(v)
        midpoint = (v.children[0].x + v.children[-1].x) / 2
        w = v.lbrother()
        if w:
            v.x = w.x + distance #distance #XXX: what's distance?
            v.mod = v.x - midpoint
        else:
            v.x = midpoint
    return v

def apportion(v, default_ancestor):
    w = v.lbrother()
    if w:
        #in buchheim notation:
        #i == inner; o == outer; r == right; l == left; r = +; l = -
        vir = vor = v
        vil = w
        vol = v.lmost_sibling
        sir = sor = v.mod
        sil = vil.mod
        sol = vol.mod
        while vil.right() and vir.left():
            if str(v.tree) == "r1":
                print "%s %s %s %s" % (vil.tree, vir.tree, vol.tree, vor.tree)
            vil = vil.right()
            vir = vir.left()
            vol = vol.left()
            vor = vor.right()
            vor.ancestor = v
            shift = (vil.x + sil) - (vir.x + sir) + 1 #distance
            if shift > 0:
                move_subtree(ancestor(vil, v, default_ancestor), v, shift)
                sir = sir + shift
                sor = sor + shift
            sil += vil.mod
            sir += vir.mod
            sol += vol.mod
            sor += vor.mod
        right = vil.right()
        if right and not vor.right():
            vor.thread = vil.right()
            vor = vor.mod + sil - sor
        left = vir.left()
        if left and not vol.left():
            vol.thread = left
            vol.mod = vol.mod + sir - sol
            default_ancestor = v
    return default_ancestor

def move_subtree(wl, wr, shift):
    subtrees = len(wr.children) - len(wl.children)
    wr.change -= shift / subtrees
    wr.shift += shift
    wl.change += shift / subtrees
    wr.x += shift
    wr.mod += shift

def execute_shifts(v):
    shift = change = 0
    for w in v.children[::-1]:
        w.x += shift
        w.mod += shift
        change += w.change
        shift += w.shift + change

def ancestor(vil, v, default_ancestor):
    if vil.ancestor in v.children:
        return vil.ancestor
    else:
        return default_ancestor

def second_walk(v, m=0, depth=0):
    v.x += m
    v.y = depth
    for w in v.children:
        second_walk(w, m + v.mod, depth+1)

if __name__ == "__main__":
    from demo_trees import trees
    from reingold_thread import p as printtree

    dt = buchheim(trees[5])
    printtree(dt)
