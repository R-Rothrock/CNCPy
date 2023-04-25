# test_advanced.py
# tests for new implementations in CNCPy 1.3.0

from context import CNCPy
from CNCPy import premades

def test_lattice():
    """
    Test for `CNCPy.premades.lattice`
    """
    c = CNCPy.GcodeCursor("lattice_test")
    # five layers of lattice in the center of the bed
    premades.lattice(c, 100, 150, 100, 150, 5)

if __name__ == "__main__":
    test_lattice()
