# -*- coding: utf-8 -*-
__doc__ = '''
CNCPy is a Python framework designed to write `.gcode` files for 3D printers
Author: Roan Rothrock
License: GNU General Public License
'''

import contextlib
import os

from CNCPy.Exceptions import (
    bed_heating_error,
    extruder_heating_error,
    GcodeCoordinateError,
    GcodeValueError,
    x_subceed_side_error,
    x_superceed_side_error,
    y_subceed_side_error,
    y_superceed_side_error
)

class GcodeCursor:
    '''
    Creates and accesses pointer to a `.gcode` output file.
    `out_file`: file to create and access.
    `bed_x`: x dimension of the bed.
    `bed_y`: y dimension of the bed.
    `initial_comment`: comment put at top of output file.
    `extrusion_ratio`: the rate of extrusion (for example, 1 cm/in of
    plastic for 1 cm/in of movement.)
    `unsafe`: if true, disables all exceptions.
    '''
    
    def __init__(self, out_file, bed_x=235, bed_y=235, *,
                 initial_comment='Made with CNCPy', metric=True,
                 extrusion_ratio=1, unsafe=False):
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

        # necessary comments
        self.comment("FLAVOR:Marlin")# identify the gcode as printer gcode.
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

        self.__unsafe = unsafe

        self.__extrude_amount = 0
        self.__extrusion_ratio = extrusion_ratio

        self.__bed_x = bed_x
        self.__bed_y = bed_y

        self.__x = 0
        self.__y = 0
        self.__z = 1

    def get_x(self) -> float:
        return float(self.__x)

    def get_y(self) -> float:
        return float(self.__y)

    def get_z(self) -> float:
        return float(self.__z)

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
            data += str(i)
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
        self.move(self.__bed_x/2, self.__bed_y/2, speed=15)

    def pause(self, sec, end="\n"):
        '''
        Halts all action for `sec` seconds.
        '''
        self.append("G4 P", str(sec*1000), end)

    def heat_extruder(self, temp: int, halt=True, end="\n"):
        '''
        Heats extruder to `temp` degrees Celsius. On wood carvers, I
        believe this gets the carver to speed.
        `halt`: whether or not to halt all other actions during heat
        default: True
        '''
        if temp < 30 and self.__unsafe == True:
            raise GcodeValueError(extruder_heating_error)

        if halt:
            self.append("M109 S", str(temp), end)
        else:
            self.append("M104 S", str(temp), end)

    def heat_bed(self, temp: int, halt=True, end="\n"):
        '''
        Heats bed to `temp` degrees Celsius. On wood carvers, I really
        don't know how this is interpreted
        `halt`: whether or not to halt all other actions during heat
        default: True
        '''
        if temp < 30 and self.__unsafe == True:
            raise GcodeValueError(bed_heating_error)

        if halt:
            self.append("M190 S", str(temp), end)
        else:
            self.append("M140 S", str(temp), end)

    def __debug(self):
        '''
        Checks that extruder coordinates are within bounds.
        Throws `CNCPy.Exceptions.GcodeCoordinateError` if they are.
        '''
        if self.__unsafe:
            return
        if self.__x < 0:
            raise GcodeCoordinateError(x_subceed_side_error)
        elif self.__x > self.__bed_x:
            raise GcodeCoordinateError(x_superceed_side_error)
        if self.__y < 0:
            raise GcodeCoordinateError(y_subceed_side_error)
        elif self.__y > self.__bed_y:
            raise GcodeCoordinateError(y_superceed_side_error)
        
        return 0

    def set_extrusion_ratio(self, new: int):
        """
        Sets extrusion ratio. If `new < 0` new ratio isn't set.
        """
        if not new < 0:
            self.__extrusion_ratio = new

    def move(self, x: int=0, y: int=0, z: int=0, *, extrusion: int=0,
             speed: int=5, end: str="\n"):
        '''
        Moves extruder relative to coordinates.
        `x`: movement of x
        `y`: movement of y
        `z`: movement of z
        `extrusion`: how much filament to extrude (only if more than 0)
        `speed`: speed of movement (default: 5)
        '''
        
        # update location variables
        self.__x += x
        self.__y += y
        self.__z += z

        # keep extruder location within bounds
        self.__debug()

        # writing to file
        if extrusion == 0:
            self.append("G0 X", float(self.__x), " Y",
                        str(float(self.__y)), " Z", float(self.__z),
                        " F", speed*1000, end)
        else:
            extrusion *= self.__extrusion_ratio
            self.__extrude_amount += extrusion
            self.append("G1 X", float(self.__x), " Y",
                        float(self.__y), " Z", float(self.__z),
                        " E", float(self.__extrude_amount),
                        " F", speed*1000, end)
    
    def move_to(self, x: int, y: int, z: int, *, extrusion: int=0,
                speed: int=5, end: str="\n"):
        '''
        Moves extruder _not_ relative to coordinates.
        `move_x`: new location of x
        `move_y`: new location of y
        `move_z`: new location of z
        `extrusion`: how much filament to extrude (only if more than 0)
        `speed`: speed of movement (default: 5)
        '''

        # keep extruder location within bounds
        self.__debug()

        # writing to file
        if extrusion == 0:
            self.append("G0 X", float(self.__x), " Y",
                        float(self.__y), " Z", float(self.__z),
                        " F", speed*1000, end)
        else:
            extrusion *= self.__extrusion_ratio
            self.__extrude_amount += extrusion
            self.append("G1 X", float(self.__x), " Y",
                        float(self.__y), " Z", float(self.__z),
                        " E", float(self.__extrude_amount),
                        " F", speed*1000, end)

    def clockwise_arc(self, *, x: int, y: int, arc_x: int,
                      arc_y: int, extrusion: int = 0, speed: int=5, end="\n"):
        '''
        Creates clockwise arc with `move_x` and `move_y` as locations
        proportional to the current x and y and `arc_x` and `arc_y` as
        the arc's center.
        `extrusion`: how much filament to extrude (0 by default)
        `speed`: speed of movement (default 5)
        Note: movement is relative to current location.
        '''
        if not self.__unsafe:
            if arc_x < 0 or arc_x > self.__bed_x or arc_y < 0 or arc_y > self.__bed_y:
                raise GcodeCoordinateError("Arc center found off bed.")
        
        # update coords
        self.__x += x
        self.__y += y

        # keep coordinates within bed
        self.__debug()

        # handle extrusion and write
        extrusion *= self.__extrusion_ratio
        self.__extrude_amount += extrusion
        self.append("G2 X", float(self.__x + x), " Y",
                    float(self.__y + y), " I", float(arc_x), " J",
                    float(arc_y), " E", float(self.extrude_amount),
                    " F", speed*1000, end)

    def counter_clockwise_arc(self, *, x: int, y: int,
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
        if not self.__unsafe:
            if arc_x < 0 or arc_x > self.__bed_x or arc_y < 0 or arc_y > self.__bed_y:
                raise GcodeCoordinateError("Arc center found off bed.")

        # update coords
        self.__x += x
        self.__y += y

        #keep coordinates within bed
        self.__debug()

        # handle extrusion and write
        extrusion *= self.__extrusion_ratio
        self.extrude_amount += extrusion
        self.append("G3 X", float(self.__x + x), " Y",
                    float(self.__y + y), " I", float(arc_x), " J",
                    float(arc_y), " E", float(self.extrude_amount),
                    " F", speed*1000, end)

    def close(self):
        '''
        Closes file.
        Writing functions will now throw errors.
        '''
        self.__file.close()
