# Movement

## Straight Line Movement (GcodeCursor.move)

Docstring:
```
(*, extrusion: int = 0, move_x: int = 0, move_y: int = 0, move_z: int = 0, speed: int = 5, end: str = "\n") -> None
Moves extruder relative to coordinates.
move_x: movement of x
move_y: movement of y
move_z: movement of z
extrusion: how much filament to extrude (only if more than 0)
speed: speed of movement (default: 5)
```

In Python:
```python
cursor.home()
cursor.move(move_x=5, move_y=25, extrusion=32)
# moves extruder to (5,25,0) and extrudes 32mm
cursor.move(move_x=7, move_z=1)
# moves extruder to (12,25,1) and doesn't extrude
...
```

## Clockwise Arc Movement (GcodeCursor.clockwise_arc)
Docstring:
```
(*, move_x: int, move_y: int, arc_x: int, arc_y: int, extrusion: int = 0, speed: int = 5, end: str = "\n") -> None
Creates clockwise arc with move_x and move_y as locations proportional to the current x and y and arc_x and arc_y as the arc's center.
extrusion: how much filament to extrude (0 by default)
speed: speed of movement (default 5)
```

In Python:
```python
cursor.home()
cursor.clockwise_arc(move_x=10, move_y=10, arc_x=5, arc_y=5)
# The extruder will move in a half cricle around (x+5,y+5) and update x and y.
```

## Counter Clockwise Arc Movement (GcodeCursor.counter_clockwise_arc)
Docstring:
```
(*, move_x: int, move_y: int, arc_x: int, arc_y: int, extrusion: int = 0, speed: int = 5, end: str = "\n") -> None
Creates counter clockwise arc with move_x and move_y as locations proportional to the current x and y and arc_x and arc_y as the arc's center.
extrusion: how much filament to extrude (0 by default)
speed: speed of movement (default 5)
```

In Python
```python
cursor.home()
cursor.counter_clockwise_arc(move_x=10, move_y=10, arc_x=5, arc_y=5)
# The extruder will move in a half circle around (x+5,y+5) and update x and y.
```

## Move to (GcodeCursor.move_to)
Docstring:
```
(*, extrusion: int = 0, move_x: int = 0, move_y: int = 0, move_z: int = 0, speed: int = 5, end: str = "\n") -> None
Moves extruder _not_ relative to coordinates.
move_x: new location of x
move_y: new location of y
move_z: new location of z
extrusion: how much filament to extrude (only if more than 0) speed: speed of movement (default: 5)
```

In Python:
```python
cursor.move(move_x=15)
cursor.move_to(move_x=50, move_y=45)
print(cursor.get_x())# prints `50`
```
