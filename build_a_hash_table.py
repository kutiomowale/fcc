#!/usr/bin/env python3


class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        if not isinstance(string, str):
            raise TypeError("Must be a string")
        result = sum([ord(char) for char in string])
        return result

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        else:
            self.collection[hash_value] = {key: value}

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            del self.collection[hash_value][key]

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]
        return None


def main():
    my_hash_table = HashTable()
    print(my_hash_table.collection)
    print(my_hash_table.lookup('golf'))
    print(my_hash_table.hash('golf'))
    my_hash_table.add('golf', 'sport')
    print(my_hash_table.collection)
    print(my_hash_table.lookup('golf'))
    my_hash_table.add('dear', 'friend')
    my_hash_table.add('read', 'book')
    my_hash_table.add('rose', 'flower')
    my_hash_table.add('fcc', 'coding')
    my_hash_table.add('cfc', 'chemical')
    print(my_hash_table.collection)
    my_hash_table.remove('golf')
    my_hash_table.remove('dear')
    my_hash_table.remove('omowale')
    print(my_hash_table.collection)
    try:
        my_hash_table.add(34, 'hello')
    except TypeError as e:
        print(f"TypeError: {e}")


if __name__ == '__main__':
    main()
