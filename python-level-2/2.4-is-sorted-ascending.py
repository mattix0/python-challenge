# 1. Make a function with an algorithm to check if a list of numbers are sorted
# 2. Make a list that are sorted and a list that aren't.
# 3. Return True or False depending on 
# Optionally make the function take params to either ascending or decending

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="List to check. Example: python 2.4-is-sorted-ascending.py -l '1 5 3 2 1'")
parser.add_argument("-st", "--sort-type", help="Check if a list is sorted Ascending or Descending. Example: python 2.4-is-sorted-ascending.py -l '1 5 3 2 1' -st ascending")

args = parser.parse_args()

user_list_str  = args.list
user_list = user_list_str.split()

sort_list_type = args.sort_type

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

def is_sorted(list, sort_type):
    if sort_type == "ascending":
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                return {
                    sort_type: False,
                    "list": list,
                    }
        return {
                sort_type: True,
                "list": list,
                }
        
    if sort_type == "descending":
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                return {
                        sort_type: False,
                        "list": list,
                        }

        return {
                sort_type: True,
                "list": list,
                }


result = is_sorted(user_list, sort_list_type)
print(result['list'], sort_list_type.upper(), result[sort_list_type])
