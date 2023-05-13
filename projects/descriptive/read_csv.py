import csv

def get_file(filename: str):
    return csv.reader(open(filename))

def get_formated_data(file):
    counter = 0
    ages = []
    for line in file:
        if counter == 0:
            counter += 1
        else:
            ages.append(int(line[0]))
    return ages