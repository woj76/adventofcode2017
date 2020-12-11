#!/usr/bin/python3

from aoc import repres

file = open("../data/day06.txt", "rt")
data = [int(x) for x in file.read().strip().split('\t')]
file.close()

part2 = True
r = 0
seen = []

while True:
	m = max(data)
	i = data.index(m)
	data[i] = 0
	for j in range(0, m):
		i = (i + 1) % 16
		data[i] += 1
	r += 1
	if data in seen:
		if part2:
			r -= seen.index(data) + 1
		break
	seen.append(data.copy())

repres(r, part2)
