# 1. Take in a random string from input()
# 2. Make it spongecase and print it to the user
# NOTE: I took this and just made it so every other character was uppercase.
#       Could have made the randomness, i didn't as i initially thought spongecase was like that..
#       It seems like that is called Alternating Case .. -.- 
#       Maybe I'll visit this project again. For now I am leaving it as is.

new_string = ""
print("Please provide a string to convert to sPoNgE cAsE:")

string = input()
splitted_string = string.split()
    
for word in splitted_string:
    for char in range(len(word)):
        if char % 2 == 0:
            sponge_case = word[char].lower()
            new_string += sponge_case

        else:
            sponge_case = word[char].upper()
            new_string += sponge_case

    new_string += " "

new_string.strip()
print(new_string)
