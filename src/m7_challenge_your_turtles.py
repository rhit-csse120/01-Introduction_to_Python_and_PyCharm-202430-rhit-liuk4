"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         Kevin Liu.
"""

import rosegraphics as rg

window = rg.TurtleWindow()
###############################################################################
# DONE: 1.
#   On Line 7 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#  _
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2  rg.SimpleTurtle  objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#  _
#   Don't forget that you need to import rosegraphics, construct a TurtleWindow
#   and have it close_on_mouse_click, just as in all previous modules.
#  _
#   In this CHALLENGE problem, be creative!
#   Strive for way-cool pictures!  Abstract pictures rule!
#  _
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#  _
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

redPen = rg.SimpleTurtle("turtle")
redPen.pen = rg.Pen("red", 5)
redPen.speed = 100

for k in range(10):
    for i in range(8):
        redPen.pen_down()
        redPen.right(90)
        redPen.forward(i*5)
    redPen.pen_up()
    redPen.left(45)
    redPen.forward(5)
    redPen.right(45)

greenPen = rg.SimpleTurtle("turtle")
greenPen.pen = rg.Pen("green", 15)
greenPen.speed = 20

for k in range(50):
    greenPen.left(35)
    greenPen.forward(k*5)

window.close_on_mouse_click()