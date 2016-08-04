#!/usr/bin/env python
import cairo, sys

file = open(sys.argv[1],mode="r")
dna = file.read()
length = int(len(dna) * 1 + 20)
s = cairo.PDFSurface(sys.argv[2],length,30)
c = cairo.Context(s)
c.set_antialias(cairo.ANTIALIAS_NONE)


def draw_base(base, j):
    base = base.upper()
    color = (0,0,0)
    if base == "A":
        color = (51,0,102)
    elif base == "T":
        color = (255,255,0)
    elif base == "G":
        color = (0,102,51)
    elif base == "C":
        color = (255,0,0)

    c.set_source_rgb(color[0], color[1], color[2])
    c.rectangle(10+1*j, 10, 1, 10)
    c.fill()
    if j % 50 == 0:
        # draw ticks
        c.set_source_rgb(0,0,0)
        c. rectangle(10+1*j,5,0.5,3)
        c.fill()
        # draw numbers
        c.set_font_size(3)
        c.move_to(10+1*j, 4)
        c.show_text(str(j))

j=0
for i in dna:
    print(i)
    draw_base(i, j)
    j += 1
