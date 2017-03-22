#!/usr/bin/env python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

try:
    divider = int(input("Enter a number: "))
except:
    print("That's silly")
    exit()

less_than = []
for number in numbers:
    if number < divider:
        less_than.append(str(number))

print("The numbers in the list less than %d are %s" % (divider, ", ".join(less_than)))

