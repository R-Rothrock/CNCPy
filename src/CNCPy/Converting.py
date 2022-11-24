# -*- coding:utf-8 -*-
__doc__ = '''
Simple script for unit conversion between metric and imperial units.
'''

def mm_to_in(mm: int) -> int:
    return mm * 0.0393

def cm_to_in(cm: int) -> int:
    return cm * 0.393

def in_to_mm(inch: int) -> int:
    return inch * 0.254

def in_to_cm(inch: int) -> int:
    return inch * 2.54

def farenheit_to_celsius(temp: int) -> int:
    return int((temp - 32) * 5/9)

def celsius_to_farenheit(temp: int) -> int:
    return int(temp * 9/5 + 32)

if __name__ == "__main__":
    print("1mm to inch:", mm_to_in(1), sep=" ")
    print("2mm to inch:", mm_to_in(2), sep=" ")
    print("1cm to inch:", cm_to_in(1), sep=" ")
    print("2cm to inch:", cm_to_in(2), sep=" ")
    print("1in to mm:", in_to_mm(1), sep=" ")
    print("2in to mm:", in_to_mm(2), sep=" ")
    print("1in to cm:", in_to_cm(1), sep=" ")
    print("2in to cm:", in_to_cm(2), sep=" ")

    print("72 Farenheit to Celsius:", farenheit_to_celsius(72), sep=" ")
    print("22 Celsius to Farenheit;", celsius_to_farenheit(22), sep=" ")

    #print("deubg:", farenheit_to_celsius(celsius_to_farenheit(5)), "=", float(5), sep=" ")
