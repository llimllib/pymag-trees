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

#3 balanced
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
  Tree("l1",
    Tree("l9"),
      Tree("l10")),
  Tree("r1", 
    Tree("r2"),
    Tree("r5"))),

#6 buchheim n-ary tree
Tree("root",
  Tree("bigleft",
    Tree("l1"),
    Tree("l2"),
    Tree("l3"),
    Tree("l4"),
    Tree("l5"),
    Tree("l6"),
    Tree("l7", Tree("ll1"))),
  Tree("r1"),
  Tree("r2"),
  Tree("r3", Tree("r31")),
  Tree("bigright",
    Tree("brr",
      Tree("br1"),
      Tree("br2"),
      Tree("br3"),
      Tree("br4"),
      Tree("br5"),
      Tree("br6"),
      Tree("br7"))))
]
