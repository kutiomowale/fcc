#!/usr/bin/env python3
def verify_card_number(string_of_digits):
    new_digits = ""
    for digit in string_of_digits:
        if digit.isdigit():
            new_digits += digit
    check_digit = new_digits[-1]
    new_digits = new_digits[:-1][::-1]
    doubled_digits = ""
    for index, digit in enumerate(new_digits):
        if index % 2 == 0:
            digit = int(digit)
            digit *= 2
            if digit > 9:
                digit -= 9
        doubled_digits += str(digit)

    doubled_digits = doubled_digits[::-1]
    doubled_digits += check_digit
    sum_of_doubled_digits = 0
    for digit in doubled_digits:
        sum_of_doubled_digits += int(digit)

    if sum_of_doubled_digits % 10 == 0:
        return "VALID!"
    return "INVALID!"


def main():
    print(verify_card_number('453914881'))
    print(verify_card_number('453914889'))
    print(verify_card_number('4111-1111-1111-1111'))
    print(verify_card_number('453914881'))
    print(verify_card_number('1234 5678 9012 3456'))


if __name__ == '__main__':
    main()
