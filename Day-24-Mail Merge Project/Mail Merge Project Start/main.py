with open('./Input/Names/invited_names.txt') as names:
    names_list = names.readlines()
    print(names_list)

with open('./Input/Letters/starting_letter.txt') as letter:
    letter = letter.read()

for name in names_list:
    new_name = name.strip()
    new_letter = letter.replace('[name]', new_name)
    with open(f'./Output/ReadyToSend/letter_for_{new_name}.docx', mode='w') as letter_file:
        letter_file.write(new_letter)
