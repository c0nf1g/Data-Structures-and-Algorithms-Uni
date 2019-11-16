def bubble_sort(array):
    compare_operations = 0
    swap_operations = 0

    for iteration in range(len(array)):
        for clip in range(0, len(array) - 1):
            if array[clip].duration < array[clip + 1].duration:
                array[clip], array[clip + 1] = array[clip + 1], array[clip]
                swap_operations += 1
            compare_operations += 1

    return "Compare operations: {} \n" \
           "Swap opeations: {} \n" \
           "Result: \n {}".format(compare_operations,
                                  swap_operations,
                                  array)
