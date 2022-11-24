# Getting started
Please note: I _highly_ recommend that this documentation is approached
with at least a basic understanding of GCODE and nested loops.
Also note: The compiled GCODE from this program is intended for 3D
printers, and it is not specifically intended for other CNC machines (millers, etc.).
Specifically, this is designed to be compatible with my _Creality Ender3_

## Installation
`CNCPy` can be installed with the pip command.
```bash
python -m pip install CNCPy
```

## Initial usage
To use `CNCpy`, you need to access `CNCPy.GcodeCursor()`,
with `out_file` being the name of the file you want to be created for
GCODE output.
```
(out_file: Any, bed_x: int = 235, bed_y: int = 235, initial_comment: str = 'Made with PyGcode', metric: bool = True) -> None
Creates and accesses pointer to a `.gcode` output file.
`out_file`: file to create and access.
`bed_x`: x dimension of the bed. Default: 235mm (the size of my 3D printer)
`bed_y`: y dimension of the bed. Default: 235mm (the size of my 3D printer)
`initial_comment`: comment put at top of output file. Defaults to
`"Made with CNCPy"`. Preferably, don't change this.
`metric`: Whether or not you want metric measurements.
```
I **strongly** recommend that the metric variable isn't touched,
espescially because the dimensions of the bed are for metric units,
along with the tempatures for heating the bed and extruder.

if you really
want to, though, be sure to redefine bed measurements with the unit converters in `CNCPy.Converting`

---
Note: if `out_file` already exists, it will be cleared before use.
```python
>>> import CNCPy
>>> cursor = CNCPy.GcodeCursor("file.gcode")
>>> cursor
<CNCPy.GcodeCursor object at [hex digits]>
...
```
Go to the `basic commands` for next steps.
