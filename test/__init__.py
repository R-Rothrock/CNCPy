# -*- coding:utf-8 -*-
# dumb little script for support for like, figurines or something.
# run this and see how much GCODE I made in just 50 and some lines.

import CNCPy

# cursor for Gcode
c = CNCPy.GcodeCursor("sample_support.gcode")

# initializing Gcode
c.newln()
c.comment("Preparing bed")
c.heat_extruder(200, halt=False)
c.heat_bed(60, halt=False)
c.heat_extruder(200, halt=True)
c.heat_bed(60, halt=True)
c.newln()

# creating support layers
support_layers = 5 # <=== this many
c.comment("Support layer")
# the reason this library is better than raw gcode:
# the 14 lines of code below results in over 500 lines of Gcode
i = 0
c.comment("LAYER:1")
while i < support_layers:
    c.move_to(move_x=c.bed_x/2, move_y=c.bed_y/2)
    c.move(move_x=40)
    c.newln()
    while c.get_x() > c.bed_x/2-25:
        c.move(move_y=50, extrusion=25)
        c.move(move_x=-2, extrusion=1)
        c.move(move_y=-50, extrusion=25)
        c.move(move_x=-2, extrusion=1)
        c.newln()
    c.comment("LAYER:"+str(i+2))
    c.move(move_z=1, end=' ')
    c.comment("update Z")
    i += 1
# layers = i

c.move_to(move_x=c.bed_x/2+40, move_y=c.bed_y/2+50)
c.newln()

while c.get_y() >= c.bed_y/2:
    c.move(move_x=-68, extrusion=25)
    c.move(move_y=-1.5)
    c.move(move_x=68, extrusion=25)
    c.move(move_y=-1.5)
    c.newln()
c.comment("More code goes here")

#...
c.close()
