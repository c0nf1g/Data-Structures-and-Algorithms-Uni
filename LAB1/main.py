from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort
import timeit
from read_file import read_file


def main():
    clip_array = read_file("resources/data.csv")

    print("\n!------ Bubble sort ------!\n")
    start = timeit.default_timer()
    bubble_sort(clip_array.copy())
    print("time:", timeit.default_timer() - start, '\n')
    print(bubble_sort(clip_array))

    print("\n!------ Quick sort ------!\n")
    start = timeit.default_timer()
    quick_sort(clip_array.copy(), 0, len(clip_array.copy()) - 1)
    print("time:", timeit.default_timer() - start, '\n')
    print(quick_sort(clip_array, 0, len(clip_array) - 1))


if __name__ == "__main__":
    main()
