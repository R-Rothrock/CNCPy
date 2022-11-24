# -*- coding:utf-8 -*-
__doc__ = '''
CNCPy is a package designed to write `.gcode` files for 3D printers,
specifically, my Creality Ender3.
Author: Roan Rothrock
License: GNU General Public License
'''

import contextlib
import os

from CNCPy.Exceptions import *

class GcodeCursor:
    '''
    Creates and accesses pointer to a `.gcode` output file.
    `out_file`: file to create and access.
    `bed_x`: x dimension of the bed.
    `bed_y`: y dimension of the bed.
    `initial_comment`: comment put at top of output file. Please don't touch.
    '''
    
    def __init__(self, out_file, bed_x=235, bed_y=235,
                 initial_comment='Made with CNCPy', metric=True):
        '''
        Creates `out_file`, writes some basic Gcode into the file,
        and initializes variables for keeping track of extruder location.
        Notes:
        If `out_file` exists, it will be wiped before use.
        By default, the Z coordinate will be raised 1mm.
        '''
        with contextlib.suppress(FileNotFoundError):
            os.remove(out_file)

        # adding ".gcode" prefix to out_file
        if not out_file.endswith(".gcode"):
            out_file += ".gcode"

        self.file_name = out_file
        self.__file = open(self.file_name, "w")

        # helps viewers recognize what the GCODE is for
        self.comment("FLAVOR:Marlin")
        self.comment(self.file_name)
        self.comment(initial_comment)

        # necessary gcode at the beginning of the file
        self.append("G90\n")# absolute positioning
        self.append("G29\n")# auto bed leveling
        self.append("G0 Z1.0 F2000\n")#move Z up 1mm/in

        if metric:
            self.append("G21\n")# indicates SI measurements
        else:
            self.append("G20\n")# indicates imperial measurements

        self.home()

        self.extrude_amount = 0
        self.bed_x = bed_x
        self.bed_y = bed_y

        self._x = 0
        self._y = 0
        self._z = 1

    def get_x(self) -> int:
        return float(self._x)

    def get_y(self) -> int:
        return float(self._y)

    def get_z(self) -> int:
        return float(self._z)

    def comment(self, comment, end="\n"):
        '''
        Adds comment to file.
        '''
        self.append("; ", comment, end)

    def append(self, *line):
        '''
        Adds unedited line to file.
        '''
        data = str()
        for i in line:
            data += i
        self.__file.write(data)

    def newln(self):
        self.append("\n")

    def home(self, end="\n"):
        '''
        Takes extruder to (0,0,0).
        '''
        self.append("G28", end)

    def center(self):
        '''
        Centers extruder within the bounds of the bed.
        '''
        self.move(move_x=self.bed_x/2, move_y=self.bed_y/2, speed=15)

    def pause(self, sec, end="\n"):
        '''
        Halts all action for `sec` seconds.
        '''
        self.append("G4 P", str(sec*1000), end)

    def heat_extruder(self, temp: int, halt=True, end="\n"):
        '''
        Heats extruder to `temp` degrees Celsius.
        `halt`: whether or not to halt all other actions during heat
        default: True
        '''
        if temp < 30:
            raise GcodeValueError(extruder_heating_error)

        if halt:
            self.append("M109 S", str(temp), end)
        else:
            self.append("M104 S", str(temp), end)

    def heat_bed(self, temp: int, halt=True, end="\n"):
        '''
        Heats bed to `temp` degrees Celsius.
        `halt`: whether or not to halt all other actions during heat
        default: True
        '''
        if temp < 30:
            raise GcodeValueError(bed_heating_error)

        if halt:
            self.append("M190 S", str(temp), end)
        else:
            self.append("M140 S", str(temp), end)

    def debug(self):
        '''
        Checks that extruder coordinates are within bounds.
        Throws `PyGcode.Exceptions.GcodeCoordinateError` if they are.
        '''
        if self._x < 0:
            raise GcodeCoordinateError(x_subceed_side_error)
        elif self._x > self.bed_x:
            raise GcodeCoordinateError(x_superceed_side_error)
        if self._y < 0:
            raise GcodeCoordinateError(y_subceed_side_error)
        elif self._y > self.bed_y:
            raise GcodeCoordinateError(y_superceed_side_error)
        
        return 0

    def move(self, *, extrusion: int=0, move_x: int=0, move_y: int=0,
             move_z: int=0, speed: int=5, end: str="\n"):
        '''
        Moves extruder relative to coordinates.
        `move_x`: movement of x
        `move_y`: movement of y
        `move_z`: movement of z
        `extrusion`: how much filament to extrude (only if more than 0)
        `speed`: speed of movement (default: 5)
        '''
        
        # update location variables
        self._x += move_x
        self._y += move_y
        self._z += move_z

        # keep extruder location within bounds
        self.debug()

        # writing to file
        if extrusion == 0:
            self.append("G0 X", str(float(self._x)), " Y",
                        str(float(self._y)), " Z", str(float(self._z)),
                        " F", str(speed*1000), end)
        else:
            self.extrude_amount += extrusion
            self.append("G1 X", str(float(self._x)), " Y",
                        str(float(self._y)), " Z", str(float(self._z)),
                        " E", str(float(self.extrude_amount)),
                        " F", str(speed*1000), end)
    
    def move_to(self, *, extrusion: int=0, move_x: int=0, move_y: int=0,
                      move_z: int=0, speed: int=5, end: str="\n"):
        '''
        Moves extruder _not_ relative to coordinates.
        `move_x`: new location of x
        `move_y`: new location of y
        `move_z`: new location of z
        `extrusion`: how much filament to extrude (only if more than 0)
        `speed`: speed of movement (default: 5)
        '''
        
        # update location variables
        if move_x != 0:
            self._x = move_x
        if move_y != 0:
            self._y = move_y
        if move_z != 0:
            self._z = move_z

        # keep extruder location within bounds
        self.debug()

        # writing to file
        if extrusion == 0:
            self.append("G0 X", str(float(self._x)), " Y",
                        str(float(self._y)), " Z", str(float(self._z)),
                        " F", str(speed*1000), end)
        else:
            self.extrude_amount += extrusion
            self.append("G1 X", str(float(self._x)), " Y",
                        str(float(self._y)), " Z", str(float(self._z)),
                        " E", str(float(self.extrude_amount)),
                        " F", str(speed*1000), end)

    def clockwise_arc(self, *, move_x: int, move_y: int, arc_x: int,
                      arc_y: int, extrusion: int = 0, speed: int=5, end="\n"):
        '''
        Creates clockwise arc with `move_x` and `move_y` as locations
        proportional to the current x and y and `arc_x` and `arc_y` as
        the arc's center.
        `extrusion`: how much filament to extrude (0 by default)
        `speed`: speed of movement (default 5)
        Note: movement is relative to current location.
        '''
        if arc_x < 0 or arc_x > self.bed_x or arc_y < 0 or arc_y > self.bed_y:
            raise GcodeCoordinateError("Arc center found off bed.")
        
        # update coords
        self._x += move_x
        self._y += move_y

        # keep coordinates within bed
        self.debug()

        # handle extrusion and write
        self.extrude_amount += extrusion
        self.append("G2 X", str(float(self._x + move_x)), " Y",
                    str(float(self._y + move_y)), " I", str(float(arc_x)), " J",
                    str(float(arc_y)), " E", str(float(self.extrude_amount)),
                    " F", str(speed*1000), end)

    def counter_clockwise_arc(self, *, move_x: int, move_y: int,
                              arc_x: int, arc_y: int, extrusion: int = 0,
                              speed: int=5, end="\n"):
        '''
        Creates counter clockwise arc with `move_x` and `move_y` as locations
        proportional to the current x and y and `arc_x` and `arc_y` as
        the arc's center.
        `extrusion`: how much filament to extrude (0 by default)
        `speed`: speed of movement (default 5)
        Note: movement is relative to current location.
        '''
        if arc_x < 0 or arc_x > self.bed_x or arc_y < 0 or arc_y > self.bed_y:
            raise GcodeCoordinateError("Arc center found off bed.")

        # update coords
        self._x += move_x
        self._y += move_y

        #keep coordinates within bed
        self.debug()

        # handled extrusion and writes
        self.extrude_amount += extrusion
        self.append("G3 X", str(float(self._x + move_x)), " Y",
                    str(float(self._y + move_y)), " I", str(float(arc_x)), " J",
                    str(float(arc_y)), " E", str(float(self.extrude_amount)),
                    " F", str(speed*1000), end)

    def close(self):
        '''
        Closes file.
        Writing functions will now throw errors.
        '''
        self.__file.close()
