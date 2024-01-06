NOTE
---

01/06/24

After taking some time to develop and improve this project, I've
decided this project is no longer worth developing and maintaining.
1.0.2 will stay on PyPI, and this project will be archived.

# CNCPy

Efficient GCODE writer for 3D printers and CNC wood carvers.

## Installation

```shell
python3 -m pip install CNCPy
```

## Setup

Run the following code to initialize the cursor.

```python
import CNCPy
c = CNCPy.GcodeCursor("outputfile.gcode")
```

There's documentation for further instructions, but please note that
the current state of this project is much different from what the docs
say that it is. The code is commented, hopefully that's enough.

## Contribution

I don't work on this project often, so anybody that wants to help, feel
free. Open an issue or email me if you're curious about anything. I
know as a fact there are many bugs that need to be resolved.
