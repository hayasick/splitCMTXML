#!/usr/bin/env python
import sys

footer = '</conference>'
header1 = sys.stdin.readline().strip()
header2 = sys.stdin.readline().strip()

print header1 + header2

for line in sys.stdin:

    if line.find(footer) > -1:
        continue
   
    if line.find(header1) > -1:
        continue

    if line.find(header2) > -1:
        continue

    print line,

print footer,
