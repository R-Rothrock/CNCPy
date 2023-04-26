# lattice.py
"""
Contains the `lattice` premade function
"""

def lattice(cursor, x1: int, x2: int, y1: int, y2: int):
    """
    Creates a lattice used for spacing the figure from the bed.
    `cursor`: instance of `CNCPy.GcodeCursor`
    `x1`: minimum X for lattice
    `x2`: maximum X for lattice
    `y1`: minimum Y for lattice
    `y2`: maximum Y for lattice
    `layers`: number of layers to print.
    """

    x_difference = x2 - x1

    cursor.newln()
    cursor.move_to(x1, y1, cursor.get_z())
 
    while cursor.get_y() < y2:
        cursor.move(x_difference, extrusion=x_difference)
        cursor.move(0, 3, extrusion=3)
        cursor.move(-x_difference, extrusion=x_difference)
        cursor.move(0, 3, extrusion=3)
    cursor.home()
