#!/usr/bin/env python3
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    less = [number for number in numbers if number < numbers[0]]
    equal = [number for number in numbers if number == numbers[0]]
    greater = [number for number in numbers if number > numbers[0]]

    return quick_sort(less) + equal + quick_sort(greater)


def main():
    print(quick_sort([]))
    my_list = [20, 3, 14, 1, 5]
    print(my_list)
    print(quick_sort(my_list))
    print(my_list)
    print(quick_sort([83, 4, 24, 2]))
    print(quick_sort([4, 42, 16, 23, 15, 8]))
    print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))


if __name__ == '__main__':
    main()
