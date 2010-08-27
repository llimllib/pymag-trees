from pyglet import font
from pyglet import window

win = window.Window()

ft = font.load('Helvetica', 36)
text = font.Text(ft, 'Hello, World!')

while not win.has_exit:
    win.dispatch_events()
    win.clear()
    text.draw()
    win.flip()
