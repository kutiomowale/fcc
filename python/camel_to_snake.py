#!/usr/bin/env python3
def to_snake(text):
    result = ''
    for char in text:
        if char.isupper():
            char = '_' + char.lower()
        result += char
    return result


def main():
    print(to_snake("iLovePython"))
    print(to_snake("lovePython"))
    print(to_snake("lovePythonAndJavascript"))


if __name__ == '__main__':
    main()
