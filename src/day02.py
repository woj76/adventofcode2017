#!/usr/bin/python3

from aoc import repres

file = open("../data/day02.txt", "rt")
data = [[int(y) for y in x.split('\t')] for x in file.read().strip().split('\n')]
file.close()

part2 = True
r = 0

for row in data:
	if part2:
		r += [ x // y for x in row for y in row if x != y and x % y == 0][0]
	else:
		r += max(row) - min(row)

repres(r, part2)
