# 1. Function for converting celcius (grader) to fahrenheit
# 2. Function for converting fahrenheit to celcius
# -- 1 celcius is 33.8 fahrenheit --
import sys

args = sys.argv

celcius_to_convert = float(args[1])
fahrenheit_to_convert = float(args[2])

def celcius_to_fahrenheit(celcius):
    math = (celcius * 1.8) + 32
    print(f"{celcius} celcius in fahrenheit is {math}")

    return math

def fahrenheit_to_celcius(fahrenheit):
    math = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} fahrenheit in celcius is {math}")

    return math

