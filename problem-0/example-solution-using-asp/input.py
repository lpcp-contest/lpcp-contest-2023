#!/usr/bin/python

import sys


def process_cell(row, col, word):
    print("input(" + str(row) + "," + str(col) + "," + str(word) + ").")


row = 1
for line in sys.stdin:
    col = 1
    for word in line.split():
        process_cell(row, col, word)
        col += 1
    row += 1
