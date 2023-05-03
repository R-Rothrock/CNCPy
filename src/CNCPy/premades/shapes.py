# shapes.py
# https://github.com/R-Rothrock/CNCPy
"""
Contains premade 2d shapes
"""

def circle(c, x1, y1, x2, y2):
    """
    Writes a circle with `CNCPy.GcodeCursor`
     - `c`: instance of `CNCPy.GcodeCursor`
     - `x1`: X of the left side of circle
     - `y1`: Y of the left side of circle
     - `x2`: X of the right side of circle
     - `y2`: Y of the right side of circle
    """

def square(c, x, y, width, height):
    """
    Writes a square with `CNCPy.GcodeCursor`
     - `c`: instance of `CNCPy.GcodeCursor`
     - `x`: X of top-left corner
     - `y`: Y of top-left corner
     - `width`: width right of the top-left corner
     - `height`: height down from the top-left corner
    """

def triangle(c, x1, y1, x2, y2, x3, y3):
    """
    Writes a triangle with `CNCPy.GcodeCursor`
     - `c`: instance of `CNCPy.GcodeCursor`
     - `x1` and `y1`: cords for point 1 of the triangle
     - `x2` and `y2`: I think you get the point
    """