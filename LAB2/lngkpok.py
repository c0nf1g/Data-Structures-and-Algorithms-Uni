def find_sequence(array):
    array = sorted(array)
    joker = array.count(0)
    jokers = joker
    counter = 1
    max_length = 0
    missed = 0

    if jokers == len(array):
        return jokers

    j = 0

    while j < len(array):
        if array[j] == 0:
            array.remove(array[j])
            j -= 1
        j += 1

    i = 1

    while i < len(array):
        if array[i] - array[i - 1] == 1:
            counter += 1
        if array[i] - array[i - 1] > 1:
            if jokers >= array[i] - array[i - 1] - 1:
                jokers -= array[i] - array[i - 1] - 1
                counter += array[i] - array[i - 1]
                if missed == 0:
                    missed = i
            else:
                counter += jokers
                jokers = joker
                if counter >= max_length:
                    max_length = counter
                if missed != 0:
                    i = missed
                counter = 1
                missed = 0

        i += 1

    if jokers != 0:
        counter += jokers
    if counter > max_length:
        max_length = counter

    return max_length
