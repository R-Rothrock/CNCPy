# -*- coding:utf-8 -*-

class GcodeValueError(Exception):
    '''
    Exception for when numeric values superceed proper execution.
    EXAMPLES
    --------
    cursor.heat_bed(-10)
    cursor.heat_extruder(-10)
    '''

class GcodeCoordinateError(Exception):
    '''
    Exception for if coordinate values extent past size barriers.
    EXAMPLES
    --------
    cursor.move(move_x=cursor.bed_x+1)
    '''

# Most error messages used.
extruder_heating_error = "Extruder cannot be heated below 30 degrees."
bed_heating_error      = "Bed cannot be heated below 30 degrees."
x_subceed_side_error   = "X has subceeded bed size."
x_superceed_side_error = "X has superceeded bed size."
y_subceed_side_error   = "Y has subceeded bed size."
y_superceed_side_error = "Y has superceede bed size."
