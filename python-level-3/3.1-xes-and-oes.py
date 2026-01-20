# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. 
# The string can contain any char.
#
# EXAMPLE: 
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string", help="String to check X's and O's.")
args = parser.parse_args()

XO_STRING = args.string
compare_string = XO_STRING.replace(" ", "")

def compare_x_and_o(compare_string):
    splitted_string = list(compare_string)
    x_counter = 0
    o_counter = 0

    for char in splitted_string:
        if char == 'x' or char == 'X':
            x_counter += 1

        if char == 'o' or char == 'O':
            o_counter += 1
    
    if x_counter == o_counter:
        return True
    else:
        return False

print(compare_x_and_o(compare_string))
