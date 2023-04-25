# lattice.py
"""
Contains the `lattice` premade function
"""

def lattice(cursor, x1: int, x2: int, y1: int, y2: int, layers: int):
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

    for i in range(layers):
        cursor.newln()
        cursor.move_to(move_x=x1, move_y=y1, move_z=cursor.get_z())
        cursor.comment(f"Lattice layer {i+1}")

        while cursor.get_y() < y2:
            cursor.move(move_x=x_difference, extrusion=x_difference)
            cursor.move(move_y=3, extrusion=3)
            cursor.move(move_x=-x_difference, extrusion=x_difference)
            cursor.move(move_y=3, extrusion=3)

        cursor.move(move_z=1)
