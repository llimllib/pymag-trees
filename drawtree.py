from math import atan, sin, cos, pi
from PIL import Image, ImageDraw
from demo_trees import trees
from reingold_thread import reingold_tilford as rt
#from reingold_naive import reingold_tilford as rt
from buchheim import buchheim


# print trees[5][0]
t = buchheim(trees[5])
# t = rt(trees[5])

DIAMETER = 30
SPACING_VERTICAL = DIAMETER * 1.5
SPACING_HORIZONTAL = DIAMETER * 1.5


def drawt(draw, root, depth):
    draw.ellipse([root.x * SPACING_HORIZONTAL,
                  depth * SPACING_VERTICAL,
                  root.x * SPACING_HORIZONTAL + DIAMETER,
                  depth * SPACING_VERTICAL + DIAMETER],
                 fill=(225),
                 outline=(0))
    for child in root.children:
        drawt(draw, child, depth + 1)


def drawconn(draw, root, depth):
    for child in root.children:
        draw.line([root.x * SPACING_HORIZONTAL + (DIAMETER / 2),
                   depth * SPACING_VERTICAL + (DIAMETER / 2),
                   child.x * SPACING_HORIZONTAL + (DIAMETER / 2),
                   (depth + 1) * SPACING_VERTICAL + (DIAMETER / 2)],
                  fill=(0))
        drawconn(draw, child, depth + 1)


def sign(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    else:
        return -1


def dottedline(draw, x1, y1, x2, y2):
    segment = 5
    if x2 == x1:
        theta = pi / 2
    elif x2 - x1 > 0:
        theta = atan(float(y2 - y1) / float(x2 - x1))
    else:
        theta = pi + atan(float(y2 - y1) / float(x2 - x1))

    dx = cos(theta) * segment
    dy = sin(theta) * segment
    xdir = x1 < x2
    ydir = y1 < y2

    while 1:
        if xdir != (x1 < x2) or ydir != (y1 < y2):
            break
        draw.line([x1, y1, x1 + dx, y1 + dy], fill=(0))
        x1, y1 = x1 + 2 * dx, y1 + 2 * dy


def drawthreads(draw, root, depth):
    for child in root.children:
        c = child.thread
        if c:
            dottedline(draw, child.x * SPACING_HORIZONTAL + (DIAMETER / 2), (depth + 1) * SPACING_VERTICAL + (DIAMETER / 2),
                       c.x * SPACING_HORIZONTAL + (DIAMETER / 2), (depth + 2) * SPACING_VERTICAL + (DIAMETER / 2))
        drawthreads(draw, child, depth + 1)


im = Image.new('L', (500, 500), (255))
draw = ImageDraw.Draw(im)
drawconn(draw, t, 0)
drawthreads(draw, t, 0)
drawt(draw, t, 0)

im.save('drawtree.png')
