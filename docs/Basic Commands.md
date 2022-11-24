# Basic commands
Here are basic commands (not including movement commands)
for `CNCPy.GcodeCursor`.

## Heating bed (GcodeCursor.heat_bed)
Docstring:
```
(self, temp: int, halt=True, end="\n") -> None:
Heats extruder to `temp` degrees.
`halt`: whether or not to halt all other actions during heat
default: True
```
In Python:
```python
cursor.heat_bed(60)
...
```

## Heating extruder (GcodeCursor.heat_extruder)
Docstring:
```
(self, temp: int, halt=True, end="\n") -> None:
Heats extruder to `temp` degrees Celsius.
`halt`: whether or not to halt all other actions during heat
default: True
```

In Python:
```python
cursor.heat_extruder(200)
...
```

## Comments (GcodeCursor.comment)
Docstring:
```
(self, comment, end="\n") -> None:
Adds comment to file.
```

In Python:
```python
cursor.comment("This will be a comment in the output file.")
...
```

## Home Extruder (GcodeCursor.home)
Docstring:
```
(self, end="\n") -> None:
Takes extruder to (0,0,0).
```

In Python:
```python
cursor.home()
# extruder is now at (0,0,0)
...
```

## Getting X, Y, and Z (GcodeCursor.get_x, get_y, get_z)
Simply returns coordinate of current extruder location in the GCODE.

In Python:
```python
cursor.home()
cursor.move(move_x=2, move_z=3)# don't need to understand this

print(cursor.get_x())# prints `2`
print(cursor.get_y())# prints `0`
print(cursor.get_z())# prints `3`
...
```

## Blank Line (GcodeCursor.newln)
Puts a blank line in the output file

## Center Extruder (GcodeCursor.center)
Centers extruder within the bounds of the bed.

In Python:
```python
cursor.center()
print(cursor.get_x == cursor.bed_x/2)# prints `True`
```

## Pause (GcodeCursor.pause)
Docstring:
```
(self, sec: int) -> None:
Creates GCODE that pauses actions for `sec` seconds.
```

In Python:
```python
cursor.pause(3)
# doesnt actually pause, but puts pause code in output file.
```

## Close (GcodeCursor.close)
Docstring:
```
(self) -> None:
Closes file.
Writing functions will now throw errors.
```

In Python:
```python
import CNCPy
cursor = CNCPy.GcodeCursor("out.gcode")
...
cursor.close()
```
Please be sure to run this function in every script.

## Append (GcodeCursor.append)
Docstring:
```
(self, *line) -> None:
Adds unedited line to file.
```

In Python:
```python
cursor.comment("Normal Way to put a comment in the output file")
cursor.append("; Unusual and not recommended way to put comment in output file")
```
