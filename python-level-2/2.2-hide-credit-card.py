# 1. Create an array with 16 random numbers, each ranging from 0-9
# 2. Function to print the credit card and creditcard number
#    The function needs to replace all the numbers shown with asterisks "****1234"
#    Ask the user if they want to show the full credit card number, if yes then display it
#    Else just keep it as is

import random
import sys

args = sys.argv

numbers = []
min_number = 0
max_number = 9
name = str(args[1])

def get_credit_card_number():
    string_numbers = ''
    for iteration in range(4):      

        for number in range(4):     
            random_number = random.randint(min_number, max_number)
            numbers.append(str(random_number))

        if iteration == 3:
            continue

        numbers.append("-")
            
    for item in numbers:
        string_numbers += item

    result_string = (len(numbers) - 3) * "*" + string_numbers[-4:]

    return string_numbers, result_string
    

def show_credit_card(name, card_number):
    for top in range(2):
        print("|" + 40 * "-" + "|")        
        if top == 1:
            break

        for i in range(4):
            print("|" + (40 * " ") + "|")
             
            if top == 0 and i == 1:
                print(f"Name: {name}")
                print(f"Card number: {card_number}")

credit_card_info = get_credit_card_number()
credit_card_masked = show_credit_card(name, credit_card_info[1])

print("Show card number?")
answer = input('y/n: ')

if answer == "y":
    credit_card_unmasked = show_credit_card(name, credit_card_info[0])

