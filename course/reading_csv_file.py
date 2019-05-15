"""

Reading CSV file

CSV -> Comma Separated Values

# Can be Comma Separated
Ex: 1, 2, 3, 4


# Can be Semicolon Separated
Ex: 1; 2; 3;  4

# Can be Space Separated
Ex: 1 2 3 4

"""

from csv import reader, DictReader


# Form 1 - Not recommended
with open('fighters.csv') as file:
    data_set = file.read()
    # print(type(data_set))
    print(data_set.split(','))

print('--------------------------------------------------------')

# Reader -> from cvs import reader
with open('fighters.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)  # Jump the first line
    for line in csv_reader:
        # Each line is a list
        print(f"Fighter: {line[0]}; Born in: {line[1]}; Height(cm): {line[2]}")

print('--------------------------------------------------------')

# DictReader -> from cvs import DictReader
with open('fighters.csv') as file:
    csv_reader = DictReader(file)
    # print(list(csv_reader))
    for line in csv_reader:
        # Each line is a OrderedDict
        print(f"Fighter: {line['Name']}; Born in: {line['Country']}; Height(cm): {line['Height (in cm)']}")

print('--------------------------------------------------------')
