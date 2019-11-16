compare_operations = 0
swap_operations = 0


def quick_sort(array, p, q):
    global compare_operations
    global swap_operations

    if p >= q:
        return

    pivot = array[int((p + q) / 2)].view
    i = p - 1
    j = q + 1

    while i < j:
        while True:
            i += 1
            if array[i].view >= pivot:
                compare_operations += 1
                break
        while True:
            j -= 1
            if array[j].view <= pivot:
                compare_operations += 1
                break
        if i < j:
            array[j], array[i] = array[i], array[j]
            swap_operations += 1

    quick_sort(array, p, j)
    quick_sort(array, j + 1, q)

    return "Compare operations: {} \n" \
           "Swap opeations: {} \n" \
           "Result: \n {}".format(compare_operations,
                                  swap_operations,
                                  array)
