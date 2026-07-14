Placeholder = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as names_file:
    letter = names_file.read()
    print(letter)

for name in names:
    name = name.strip()
    newletter = letter.replace(Placeholder, name)
    print(newletter)
    with open(
        f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w"
    ) as completed_letter:
        completed_letter.write(newletter)
