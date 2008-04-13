from gen import Tree
from demo_trees import trees
from reingold_thread import reingold_tilford as rtc
from reingold_thread import p as printtree
import unittest

class TreeTest(unittest.TestCase):
    def assertTree(self, tree, expected):
        self.assertEqual(tree.x, expected[0])
        for i in range(1, len(tree.children)+1):
            child = tree.children[i-1]
            exp = expected[i]
            if isinstance(exp, int): self.assertTree(child, [exp])
            else:                    self.assertTree(child, exp)

class TestBinTree(TreeTest):
    def testSimple(self):
        dt = self.f(trees[0])
        self.assertTree(dt, [1, 0, 2])

    def testDeepLeft(self):
        dt = self.f(trees[1])
        expected = [1, [0, [0, [0, [0]]]], 2]
        self.assertTree(dt, expected)

    def testDeepRight(self):
        dt = self.f(trees[2])
        expected = [1, 0, [2, [2, [2, 2]]]]
        self.assertTree(dt, expected)

    def testBalanced(self):
        dt = self.f(trees[3])
        expected = [2, [1, [1, 0, 2]], [3, 2, [4, 3, 5]]]
        self.assertTree(dt, expected)

    def testUnbalanced(self):
        #this one is a portion of a category tree from work;
        #it tests threads pretty strenuously. There should probably
        #be a thread-specific test.
        dt = self.f(trees[4])
        expected = [6, [4, [3, [2, [1, 0, 2], 3], 4], 5], [8, [7, 6, 8], 9]]
        self.assertTree(dt, expected)

    def testWSTree(self):
        #this is the tree featured prominently in Wetherell-Shannon. I draw it
        #slightly differently, since I don't have strong right-left trees, we draw
        #single children directly underneath parents
        dt = self.f(trees[5])
        expected = [3, [1, 0, [2, 1, 3]], [5, [5, [5, [5, [4, 3, 5], 6]]]]]
        self.assertTree(dt, expected)

    def testBuchMerge(self):
        #the simplest tree I could make fail on buchheim's algo
        dt = self.f(trees[6])
        expected = [3, [1, 0, 2], [5, 4, 6]]
        self.assertTree(dt, expected)

class TestNaryTree(TreeTest):
    def testBuchheim(self):
        #Figure 2 in buchheim
        dt = self.f(trees[7])
        expected = [1, 0, 1, 2]
        self.assertTree(dt, expected)

class TestNaive(TestBinTree):
    def setUp(self): 
        import reingold_naive
        self.f = reingold_naive.reingold_tilford

class TestThread(TestBinTree):
    #TODO: My current tests didn't make the lattach bug fail... write a test
    #      that does. (See r116, reingold_thread.py)
    def setUp(self): 
        import reingold_thread
        self.f = reingold_thread.reingold_tilford

class TestAddMod(TestBinTree):
    def setUp(self): 
        import reingold_addmod
        self.f = reingold_addmod.reingold_tilford

class TestBuchheim(TestBinTree, TestNaryTree):
    def setUp(self):
        import buchheim
        self.f = buchheim.buchheim

if __name__ == "__main__":
    load = unittest.TestLoader().loadTestsFromTestCase
    suite = load(TestNaive)
    suite.addTests(load(TestThread))
    #suite.addTests(load(TestAddMod))
    suite.addTests(load(TestBuchheim))
    unittest.TextTestRunner(verbosity=2).run(suite)
