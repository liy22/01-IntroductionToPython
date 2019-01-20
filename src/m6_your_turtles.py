"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Yiqing Li.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.SimpleTurtle()

pink_turtle = rg.SimpleTurtle('turtle')
pink_turtle.pen = rg.Pen('pink',2)
pink_turtle.speed = 30
size = 200

for k in range(10):
    pink_turtle.draw_circle(size)

    pink_turtle.pen_up()
    pink_turtle.left(100)

    pink_turtle.pen_down()
    size = size - 10


purple_turtle = rg.SimpleTurtle()
purple_turtle.pen = rg.Pen('purple',3)
purple_turtle.speed = 40
length = 80


for k in range(12):
    purple_turtle.draw_regular_polygon(6,length)

    purple_turtle.pen_up()
    purple_turtle.left(150)

    purple_turtle.pen_down()
    length = length - 5