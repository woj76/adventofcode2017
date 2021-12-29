#!/usr/bin/python3

from aoc import repres

b = 81
b *= 100
b += 100000
c = b + 17000

r = 0

for n in range(b, c+1, 17):
	for d in range(2,n//2):
		if n % d == 0:
			r += 1
			break

repres(r, True)
