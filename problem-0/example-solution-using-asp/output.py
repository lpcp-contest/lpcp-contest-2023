#!/usr/bin/python

import sys
import re

exp = re.compile("output\(([1-9][0-9]*),([1-9][0-9]*),([0-9]+)\)")
res = re.findall(exp, sys.stdin.read())
res = [(int(r), int(c), w) for (r, c, w) in res]
res.sort()

row = 1
for (r, c, w) in res:
    if row < r:
        row += 1
        print()
    if 1 < c: print(" ", end="")
    print(w, end="")
print()
