from gen import Tree
from reingold_thread import reingold_tilford as rtc
import unittest

class TestDrawTree(unittest.TestCase):
    def testSimple(self):
        tree = Tree("root", [
                 Tree("l"), 
                 Tree("r")])
        dt = self.f(tree)

        self.assertEqual(dt.x, 1)
        self.assertEqual(dt.children[0].x, 0)
        self.assertEqual(dt.children[1].x, 2)

    def testDeepLeft(self):
        tree = Tree("root", [
                 Tree("l1", [
                   Tree("l2", [
                     Tree("l3")])]),
                 Tree("r1")])
        dt = self.f(tree)

        eq = self.assertEqual
        eq(dt.x, 1)
        eq(dt.children[0].x, 0)
        eq(dt.children[0].children[0].x, 0)
        eq(dt.children[0].children[0].children[0].x, 0)
        eq(dt.children[1].x, 2)

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
