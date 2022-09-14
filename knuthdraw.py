from gen import Tree
from demo_trees import trees
import knuth
#reload(knuth) not sure what that was supposed to do.
from knuth import layout


def drawt(root, depth, r, rh, rw):
    #global r    don't need globals
    #oval(root.x * rw, depth * rh, r, r)        probably just some object
    
    #my custom geom object, but using positional values
    #my_r=geom.rectangle(d_vec=(r,r,0),local_position=(root.x *rw, depth * rh,0))
    
    my_r=(r, # width
            r, # height
            root.x *rw, #position x
            depth * rh) #position y
            
    objects=[]
    objects.append(my_r)
    for child in root.children:
        more_objects=drawt(child, depth+1, r, rh, rw)
        objects+=more_objects
    return objects
    
def drawconn(root, depth, r, rh, rw):
    
    objects=[]
    
    for child in root.children:
        #line(root.x * rw + (r/2), depth * rh + (r/2),
        #     child.x * rw + (r/2), (depth+1) * rh + (r/2))
        
        
        p1=(root.x * rw + (r/2), depth * rh + (r/2),0)
        p2=(child.x * rw + (r/2), (depth+1) * rh + (r/2),0)
        
        # my custom geom object but using the same info
        my_line=(p1,p2)
        
        more_objects=drawconn(child, depth+1,r, rh, rw)
        objects.append(my_line)
        objects+=more_objects
    return objects

def main():
    
    #this should work.
    t = layout(trees[5])
    
    # basic values
    r = 30
    rh = r*1.5
    rw = r*1.5
    
    # functions from the other software package/module
    #stroke(0)
    #size(1000, 500)
    #translate(2, 2)
    #stroke(0)
    
    lines = drawconn(t, 0, r, rh, rw) #this is recursive and defined here.
    rects = drawt(t, 0, r, rh, rw) #this is recursive and defined here.
    
    # the code above is virtually unchanged, it's just more explicit in
    # passing around objects and values.
    # the return value of these functions are now lists of tuples
    # describing the elements.
    
    return lines, rects

