def read_file(file_name):
    words_list = []

    with open(file_name, "r") as file:
        num = file.readline()
        words_num = int(num)

        for word in file:
            words_list.append(word.strip())

    return words_num, words_list

