# shapes.py
# https://github.com/R-Rothrock/CNCPy
"""
Contains premade 2d shapes
"""
from math import sqrt

def abs(val: int):
    return sqrt(val ** 2)

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
    Writes a square with `CNCPy.GcodeCursor`.
    To prevent extrusion, set the extrusion ratio to 0.
     - `c`: instance of `CNCPy.GcodeCursor`
     - `x`: X of top-left corner
     - `y`: Y of top-left corner
     - `width`: width right of the top-left corner
     - `height`: height down from the top-left corner
    """
    c.comment("Square premake")
    c.move_to(x, y, c.get_z())
    c.comment(abs(-10))
    c.move(0, width, extrusion=abs(width))
    c.move(-height, 0, extrusion=abs(height))
    c.move(0, -width, extrusion=abs(width))
    c.move(height, 0, extrusion=abs(height))

def triangle(c, x1, y1, x2, y2, x3, y3):
    """
    Writes a triangle with `CNCPy.GcodeCursor`
     - `c`: instance of `CNCPy.GcodeCursor`
     - `x1` and `y1`: cords for point 1 of the triangle
     - `x2` and `y2`: cords for point 2 of the triangle
     etc. etc.
    """

def quad(c, x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Writes a quadrilateral with `CNCPy.GcodeCursor`
    - `c`: instance of `CNCPy.GcodeCursor`
    - `x1` and `y1`: cords for point 1 of the quad
    - `x2` and `y2`: cords for point 2 of the quad
    etc. etc.
    """
