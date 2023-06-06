from gen import Tree
from demo_trees import trees
from ws2 import layout
from PIL import Image, ImageDraw

t = layout(trees[3])

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


im = Image.new('L', (1000, 500), (255))
draw = ImageDraw.Draw(im)
drawconn(draw, t, 0)
drawt(draw, t, 0)

im.save('figure4.png')
