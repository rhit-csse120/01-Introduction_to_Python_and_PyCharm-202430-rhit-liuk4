"""
An exercise that summarizes what you have learned in this Session.

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
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:
#  _
#    - Constructs a SimpleTurtle with a  "blue"  Pen.
#    - Makes the SimpleTurtle:
#        1. Go straight UP 200 pixels.
#        2. Lift its pen UP
#             (so that the next movements do NOT leave a "trail").
#             HINT: Use the "dot trick" to figure out how to do this.
#        3. Go to the Point at (100, -40).
#             HINT: Use the "dot trick" to figure out how to do this.
#        4. Put its pen DOWN
#             (so that the next movements will return to leaving a "trail").
#        5. Have color "green" and thickness 10.
#        6. Go 150 pixels straight DOWN.
#  _
#   Don't forget to:
#     - Import rosegraphics
#     - Construct a TurtleWindow
#            [remember the required PARENTHESES for constructing an object!]
#         at the BEGINNING of your code.
#     - Ask your  TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.  (Again, parentheses needed!)
#   See the beginning and end of   m5e_loopy_turtles   for an example.
#  _
#   As always, test by running the module.
###############################################################################

bluePen = rg.SimpleTurtle("turtle")
bluePen.pen = rg.Pen("blue", 1)
bluePen.speed = 20

bluePen.left(90)
bluePen.forward(200)

bluePen.pen_up()
bluePen.backward(240)
bluePen.right(90)
bluePen.forward(100)

bluePen.pen_down()
bluePen.pen = rg.Pen("green", 10)
bluePen.left(90)
bluePen.backward(150)

###############################################################################
# DONE: 3. After you have successfully written and tested code per the above
#   (get help as needed!), be sure that you understand how to:
#     -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
#     -- Make an object   ** DO **   something by using a METHOD.
#     -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.
#  _
#   If those concepts are not clear to you, ASK FOR HELP.
#   Once you understand those concepts, change the above _TODO_ to DONE.
#  _
#   As always, COMMIT-and-PUSH when you are done with this module.
###############################################################################

# -----------------------------------------------------------------------------
# The next line keeps the window open until the user clicks in the window.
# Whenever you are doing TurtleGraphics code, this  close_on_mouse_click   line
# should be the LAST line in the module.  DO NOT ADD CODE BELOW THIS LINE!
# -----------------------------------------------------------------------------
window.close_on_mouse_click()
