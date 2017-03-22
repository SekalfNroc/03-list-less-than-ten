#!/usr/bin/env python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less_than = []
for number in numbers:
    if number < 5:
        less_than.append(str(number))

print("The numbers in the list less than 5 are %s" % ", ".join(less_than))

