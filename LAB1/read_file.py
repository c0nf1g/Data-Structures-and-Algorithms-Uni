from classes.Clip import Clip
import csv


def read_file(name):
    array = []

    with open(name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            array.append(Clip(row[0], row[1], int(row[2]), int(row[3])))

    return array
