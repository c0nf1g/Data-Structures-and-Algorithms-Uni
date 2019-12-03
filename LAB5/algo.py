from write_to_file import save_to_file
from read_file import read_file


def find_max(array, paths, out_file, word_num):
    array = sorted(array, key=len)
    max_len_arr = []

    paths[array[0]] = 1
    for i in range(1, word_num):
        max_len = 0
        for j in range(len(array[i])):
            combination = array[i][:j] + array[i][j + 1:]
            if combination not in paths:
                continue
            comb_path = paths[combination]
            if comb_path > max_len:
                max_len = comb_path
        max_len += 1
        paths[array[i]] = max_len
        max_len_arr.append(max_len)

    save_to_file(max(max_len_arr), out_file)

    return max(max_len_arr)


if __name__ == "__main__":
    paths = {}
    out_file = 'D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\out\\out1'
    words = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data1')[1]
    word_num = read_file('D:\\Projects\\Data-Structures-and-Algorithms-Uni\\LAB5\\data\\data1')[0]

    print(find_max(words, paths, out_file, word_num))
