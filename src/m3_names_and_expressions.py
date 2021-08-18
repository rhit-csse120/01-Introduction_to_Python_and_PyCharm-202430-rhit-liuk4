answer = 2 ** 5
print(answer * 100)

###############################################################################
# TODO: 1.
#   Read the 2 lines of code ABOVE this _TODO_.
#   When the Python INTERPRETER runs, that is, when this program runs,
#   it does the following with that code:
#     1. It runs line 1, that is, it:
#          a. Evaluates (runs, computes) 2 raised to the 5th power,
#             yielding the object that is the integer 32.
#          b. Makes the name   answer   refer to that object.
#                Note that the RIGHT-hand-side of an assignment statement
#                is evaluated BEFORE the NAME on the LEFT-hand-side
#                gets ASSIGNED the result.
#     2. It runs line 2, that is, it:
#          a. Looks up the object to which the name   answer  refers (i.e., 32).
#          b. Multiplies that object (32) by 100
#               (hence computing the object that is the integer 3,200).
#          c. Prints (that is, displays on the Console/Run window)
#             the newly-computed object.  (It prints WITHOUT the comma.)
#  _
#   Make sure that you understand that those two lines accomplish the above,
#     ** ASKING QUESTIONS AS NEEDED. **
#   Once you completely understand the above, run this module,
#   confirming that it prints 3200.  Then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 2.
#   Immediately below this _TODO_, write code that:
#     a. Computes 77 plus the cosine of 2.75.
#         HINT: You will need to import the   math  module by putting:
#             import math
#         at the top of this module, then using   math.cos(2.75)  in the code.
#           Doing so tells the Python interpreter to use the function
#           named  cos  that is defined in the built-in module named math.
#     b. Stores that computed value using a name of your own choosing.
#     c. Prints the square root of that computed value.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 3.
#   Immediately below this _TODO_, write code that computes and prints:
#      the square root of ((41 * 88) + (4 * the cosine of 2))
#   Use as few or as many intermediate names as you feel appropriate.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 4.
#   Immediately below this _TODO_,
#   write code that computes the square root of 2 in two ways:
#     1. By using the   math.sqrt   function.
#     2. By raising 2 to the 0.5 power (using   **   for exponentiation).
#   Print both of the expressions that you write.
#   Run your code (fix errors as needed), then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# TODO: 5.
#   Sometimes we provide so-called   COMMENTED-OUT   lines of code
#   so that you can READ the code, then (if the exercise asks you to)
#   UN-comment the code and RUN it, to see what the code prints/does.
#      For example, just below this _TODO_, we have put 18 lines of code
#      that print something that you might find interesting.
#  _
#   To UN-comment lines of code, select the lines, hold down the CONTROL (ctrl)
#     key, and press the  /  key (it is beneath the ? on your keyboard).
#     The  #  (hash) symbol at the beginning of each line will go away.
#   To COMMENT-OUT lines of code, do the same thing, and notice that it puts
#     back the   #  (hash) symbols at the beginning of each line.
#  _
#   Highlight the 18 commented-out lines of code below this _TODO_,
#   then UN-comment them, then COMMENT-OUT them, then UN-comment them.
#   Then run the program to see the interesting thing that it prints.
#  _
#   Do NOT try to understand the lines of code; just be sure that you understand
#   how to UN-comment (and COMMENT-OUT) lines of code.  Ask for help as needed.
#   Once you understand how to UN-comment and COMMENT-OUT lines of code,
#   change the above _TODO_ to DONE.
###############################################################################

# def sierpinski(n, matrix, row, column):
#     if n == 0:
#         matrix[row][column] = "*"
#     else:
#         power = 2 ** (n - 1)
#         sierpinski(n-1, matrix, row, column)
#         sierpinski(n-1, matrix, row + power, column - power)
#         sierpinski(n-1, matrix, row + power, column + power)
# def make_matrix(n):
#     rows = 2 ** n
#     columns = (2 ** (n + 1)) - 1
#     return [[" " for _ in range(columns)] for _ in range(rows)]
# n = 5
# matrix = make_matrix(n)
# sierpinski(n, matrix, 0, (2 ** n) - 1)
# for row in matrix:
#     for column in row:
#         print(column, end="")
#     print()

###############################################################################
# TODO: 6.
#   Every object has a TYPE and a VALUE.  For example,
#   for the object that is computed by  math.sqrt(2):
#      Its TYPE is float  (which is shorthand for "floating point number").
#      Its VALUE is (approximately) 1.4142135623730951.
#  _
#   The TYPE of an object is important because it determines:
#      -- what the object KNOWS, and
#      -- what the object can DO.
#  _
#   The   type   function returns the TYPE of its argument.  For example,
#       type(3.14)    returns the CLASS (synonym for TYPE) 'float'
#   and so the code:
#       x = type(3.14)
#   will print     <class 'float'>
#   Try it now!  That is, write
#       print(type(3.14))
#   below this _TODO_ and run the program.
###############################################################################

###############################################################################
# TODO: 7.
#   Now go through each of the commented-out statements below this _TODO_,
#     ** ONE AT A TIME. **  For each:
#      1. Try to GUESS the TYPE of the expression whose type
#           is being printed.  For example, the first commented-out expression
#           belows asks you to GUESS the type of the expression "hello".
#      2. Then UN-comment the statement, RUN the code, and see what gets printed
#           to LEARN the TYPE of the expression whose type is being printed.
#   Do these ONE STATEMENT AT A TIME, so that you can learn as you go.
#  _
#   After learning (and hopefully remembering!) the types of the expressions
#   in the statements below, change the above _TODO_ to DONE.
###############################################################################
print(type("hello"))
print(type('hello'))

###############################################################################
# TODO: 7.
#   Ensure that no blue bars on the scrollbar-thing to the right remain.
#   Run one more time to be sure that all is still OK.
#  _
#   Then COMMIT-and-PUSH your work as before:
#     1. Select    VCS     from the menu bar (above).
#     2. Choose   Commit   from the pull-down menu that appears.
#     3. In the   Commit Changes   window that pops up,
#        press the   Commit and Push   button.
#           (Note: If you see only a Commit button:
#              - HOVER over the  Commit  button
#                (in the lower-right corner of the window)
#              - CLICK on  Commit and Push.)
#           (Note: If it asks you to type a message for the Commit, do so,
#                using   Done   or something like that for the message.)
#  _
#   You can COMMIT-and-PUSH as often as you like.
#   DO IT FREQUENTLY; AT LEAST once per module.
###############################################################################
