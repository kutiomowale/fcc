#!/usr/bin/env python3

# Here is your challenge:** Write a function `product` which accepts a
# number, and returns a function accepting a number. The inner function
# should return the product of the two numbers.

# **Examples:**
# ```js
# const myProduct = product(3);
# myProduct(4); // 12
# myProduct(7); // 21

def product(n):
    def helper_func(y):
        return n * y
    return helper_func
