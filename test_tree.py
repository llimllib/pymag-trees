from gen import Tree
from reingold_thread import reingold_tilford as rtc
import unittest

class TestDrawTree(unittest.TestCase):
    def assertTree(self, tree, expected):
        self.assertEqual(tree.x, expected[0])
        for i in range(1, len(tree.children)):
            child = tree.children[i-1]
            exp = expected[i]
            if isinstance(exp, int): self.assertTree(child, [exp])
            else:                    self.assertTree(child, exp)

    def testSimple(self):
        tree = Tree("root", [
                 Tree("l"), 
                 Tree("r")])
        dt = self.f(tree)

        self.assertTree(dt, [1, [0, 2]])

    def testDeepLeft(self):
        tree = Tree("root", [
                 Tree("l1", [
                   Tree("l2", [
                     Tree("l3", [
                       Tree("l4")])])]),
                 Tree("r1")])
        dt = self.f(tree)
        expected = [1, [0, [0, [0, [0]]]], 2]

        self.assertTree(dt, expected)

    def testDeepRight(self):
        tree = Tree("root", [
                 Tree("l1"),
                 Tree("r1", [
                   Tree("r2", [
                     Tree("r3", [
                       Tree("r4")])])])
                 ])
        dt = self.f(tree)
        expected = [1, 0, [2, [2, [2, [2]]]]]

        self.assertTree(dt, expected)

    def testBalanced(self):
        """It helps to draw these out on paper and have an editor that matches
        parentheses :)"""
        tree = Tree("root", [
                 Tree("l1", [
                   Tree("l2", [
                     Tree("l3"), Tree("l4")])]),
                 Tree("r1", [
                   Tree("rl1"),
                   Tree("rr1", [
                     Tree("rr2"), Tree("rr3")])])])
        dt = self.f(tree)
        expected = [2, [1, [1, [0, 2]]], [3, [2], [4, [3, 5]]]]

        self.assertTree(dt, expected)

class TestNaive(TestDrawTree):
    def setUp(self): 
        import reingold_naive
        self.f = reingold_naive.reingold_tilford

class TestThread(TestDrawTree):
    def setUp(self): 
        import reingold_thread
        self.f = reingold_thread.reingold_tilford

class TestAddMod(TestDrawTree):
    def setUp(self): 
        import reingold_addmod
        self.f = reingold_addmod.reingold_tilford

if __name__ == "__main__":
    load = unittest.TestLoader().loadTestsFromTestCase
    suite = load(TestNaive)
    suite.addTests(load(TestThread))
    suite.addTests(load(TestAddMod))
    unittest.TextTestRunner(verbosity=2).run(suite)
