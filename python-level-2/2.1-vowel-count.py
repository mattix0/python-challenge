# 1. From a input - count the vowels 'a', 'e', 'i', 'o', 'u'
# 2. Print the vowels count to the user
# 3. Print the consonant count to the user

VOWELS = ['a', 'e', 'i', 'o', 'u']
input_string_vowels    = []
input_string_consonants = []


print(f"Please input a sentence or word to get the vowel count.")

input_string = input("Write: ")

if input_string != "":
    input_string_list = list(input_string)

    for space in input_string_list:
        if space == " ":
            input_string_list.remove(space)

    for letter in input_string_list:
        print(f"[DEBUG] {letter}")
        if letter in VOWELS:
            input_string_vowels.append(letter)        

        else:
            input_string_consonants.append(letter)

    print(f'"{input_string}" contains')
    print(f"{len(input_string_vowels)} vowels and {len(input_string_consonants)} consonants.")
