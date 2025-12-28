#!/usr/bin/env python3
def selection_sort(array):
    for position in range(len(array)):
        min_index = array.index(min(array[position:]), position)
        if min_index != position and array[position] != array[min_index]:
            array[position], array[min_index] = (
                    array[min_index],
                    array[position]
            )
    return array


def main():
    print(selection_sort([33, 1, 89, 2, 67, 245]))
    print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
    print(selection_sort(
             [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123,
              43, 2, 55, 1, 234, 92]
          ))
    print(selection_sort([]))
    print(selection_sort([1]))
    print(selection_sort([1, 1, 1, 1]))
    my_list = [5, 16, 99, 12, 567, 23, 15, 72, 3]
    print(my_list)
    selection_sort(my_list)
    print(my_list)


if __name__ == '__main__':
    main()
