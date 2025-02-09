# Write a, simple, program, to simulate
# the operation of the `grep` command,
# on Unix.

# Ask the user to enter a regular expression,
# and count the number of lines that matched
# the regular expression.

import re

fhand = open('mbox.txt')

regex = input('Enter a regular expression: ')

counter = 0

for line in fhand:
    if re.search(regex, line):
        counter = counter + 1

print('mbox.txt had', counter, 'lines that matched', regex)
