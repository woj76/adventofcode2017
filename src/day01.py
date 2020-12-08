#!/usr/bin/python3

from aoc import repres

file = open("../data/day01.txt", "rt")
data = [int(x) for x in file.readline().strip()]
file.close()

part2 = True

l = len(data)
r = 0

step = l // 2 if part2 else 1

for i in range(l):
	if data[i] == data[(i+step) % l]:
		r += data[i]

repres(r, part2)
