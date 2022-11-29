# -*- coding:utf-8 -*-
__doc__ = '''
Simple script for unit conversion between metric and imperial units.
'''

def mm_to_in(mm: int) -> float:
    return mm * 0.0393

def cm_to_in(cm: int) -> float:
    return cm * 0.393

def in_to_mm(inch: int) -> float:
    return inch * 0.254

def in_to_cm(inch: int) -> float:
    return inch * 2.54

def farenheit_to_celsius(temp: int) -> float:
    return (temp - 32) * 5/9

def celsius_to_farenheit(temp: int) -> float:
    return temp * 9/5 + 32

if __name__ == "__main__":
    print("1mm to inch:", mm_to_in(1))
    print("2mm to inch:", mm_to_in(2))
    print("1cm to inch:", cm_to_in(1))
    print("2cm to inch:", cm_to_in(2))
    print("1in to mm:", in_to_mm(1))
    print("2in to mm:", in_to_mm(2))
    print("1in to cm:", in_to_cm(1))
    print("2in to cm:", in_to_cm(2))
    print("72 Farenheit to Celsius:", farenheit_to_celsius(72))
    print("22 Celsius to Farenheit;", celsius_to_farenheit(22))

