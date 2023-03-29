# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/Letters/starting_letter.txt") as letter_file:
    let = letter_file.read()

with open("input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()
# open('hi.txt', "w")

for name in names:
    name = name.strip("\n")
    txt = f"./Output/ReadyToSend/letter_to_{name}.txt"
    with open(txt, "w") as final:
        final.write(let.replace("[name]", f"{name}"))
    # print(txt)
