#!/usr/bin/env python3

from gif import Gif

g = Gif.from_file("tree.gif")

print("width = %d" % (g.logical_screen.image_width))
print("height = %d" % (g.logical_screen.image_height))
