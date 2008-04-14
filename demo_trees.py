from gen import Tree

trees = [
#0 simple test
Tree("root", 
     Tree("l"), 
     Tree("r")),

#1 deep left
Tree("root", 
  Tree("l1", 
    Tree("l2", 
      Tree("l3", 
        Tree("l4")))),
  Tree("r1")),

#2 deep right
Tree("root", 
  Tree("l1"),
  Tree("r1", 
    Tree("r2", 
      Tree("r3", 
        Tree("r4"))))
  ),

#3 tight right
Tree("root", 
  Tree("l1", 
    Tree("l2", 
      Tree("l3"), Tree("l4"))),
  Tree("r1", 
    Tree("rl1"),
    Tree("rr1", 
      Tree("rr2"), Tree("rr3")))),

#4 unbalanced
Tree("root", 
  Tree("l1", 
    Tree("l2", 
      Tree("l3", 
        Tree("l4", 
          Tree("l5"),
          Tree("l6")),
        Tree("l7")),
      Tree("l8")),
    Tree("l9")),
  Tree("r1", 
    Tree("r2", 
      Tree("r3"),
      Tree("r4")),
    Tree("r5"))),

#5 Wetherell-Shannon Tree
Tree("root",
  Tree("l1",
    Tree("ll1"),
    Tree("lr1",
      Tree("lrl"),
      Tree("lrr"))),
  Tree("r1",
    Tree("rr2",
      Tree("rr3",
        Tree("rrl",
          Tree("rrll",
            Tree("rrlll"),
            Tree("rrllr")),
          Tree("rrlr")))))),

#6 Buchheim Failure
Tree("root", 
  Tree("l",
    Tree("ll"),
      Tree("lr")),
  Tree("r", 
    Tree("rl"),
    Tree("rr"))),

#7 simple n-ary
Tree("root",
  Tree("l"),
  Tree("m"),
  Tree("r")),

#8 buchheim n-ary tree
#we see with this tree that spacing is not perfect; the middle subtrees tend
#slightly towards the right. However, it fulfuills all the criteria set out
#in the paper.
Tree("root",
  Tree("bigleft",
    Tree("l1"),
    Tree("l2"),
    Tree("l3"),
    Tree("l4"),
    Tree("l5"),
    Tree("l6"),
    Tree("l7", Tree("ll1"))),
  Tree("m1"),
  Tree("m2"),
  Tree("m3", Tree("m31")),
  Tree("bigright",
    Tree("brr",
      Tree("br1"),
      Tree("br2"),
      Tree("br3"),
      Tree("br4"),
      Tree("br5"),
      Tree("br6"),
      Tree("br7")))),

#9 random tree from http://www.brpreiss.com/books/opus5/html/page257.html
# so... the "tree to the right thing" is actually a bug
Tree("root",
  Tree("E",
    Tree("F",
      Tree("F1"),
      Tree("F2"),
      Tree("F3")),
    Tree("E2"),
    Tree("E3")),
  Tree("G",
    Tree("H",
      Tree("I",
        Tree("I1"),
        Tree("I2"),
        Tree("I3")),
      Tree("H2"),
      Tree("H3")),
    Tree("J",
      Tree("K",
        Tree("K1"),
        Tree("K2"),
        Tree("K3")),
      Tree("L",
        Tree("L1"),
        Tree("L2"),
        Tree("L3")),
      Tree("J3")),
    Tree("M",
      Tree("M1"),
      Tree("M2"),
      Tree("M3"))),
  Tree("D3")),
]
