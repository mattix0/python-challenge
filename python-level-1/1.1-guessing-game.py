# 1. Generate a random number (random_number)
# 2. Have the user guess that number
# 3. Provide hints to the user. Is it higher or lower.

import random

MIN_NUMBER = 0
MAX_NUMBER = 100
attempts = 0

print(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}")
random_number = random.randint(MIN_NUMBER, MAX_NUMBER)

while True: 
    answer = input("Number: ")
    attempts += 1

    if int(answer) == random_number:
        print(f"CORRECT! The number was {random_number}!")
        print(f"This took {attempts} attempts!")

        break
    else:
        if int(answer) < random_number:
            print(f"INCORRECT! Number is greater than {answer}")
        else:
            print(f"INCORRECT! Number is less than {answer}") 
    
    print(f"Attempts {attempts}")

