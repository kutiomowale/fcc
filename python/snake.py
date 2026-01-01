#!/usr/bin/env python3
"""Takes a sentence from the terminal
prints out a word formed by joining the lowercase words of the sentence using
an underscore.
Example: running the program then typing "How Are You" will print
"how_are_you".

Output can be copied and used to name a file.
"""


def main():
    text = input()
    words_lower = (word.lower() for word in text.split())
    result = '_'.join(words_lower)
    print(result)


if __name__ == '__main__':
    main()
