def save_to_file(number, filename):
    with open(filename, "w") as file:
        file.write(str(number))
