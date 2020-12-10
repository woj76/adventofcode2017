#!/usr/bin/python3

from aoc import repres

file = open("../data/day05.txt", "rt")
data = [int(x) for x in file.read().strip().split('\n')]
file.close()

part2 = True
r = 0
i = 0
l = len(data)

while i < l:
	offset = data[i]
	data[i] += -1 if part2 and offset >= 3 else 1 
	i += offset
	r += 1


repres(r, part2)
