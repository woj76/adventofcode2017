#!/usr/bin/python3

from aoc import repres

file = open("../data/day09.txt", "rt")
data = [x for x in file.read().strip()]
file.close()

part2 = True
r = 0

while '<' in data:
	i = data.index('<')
	j = i
	while True:
		j += 1
		if part2:
			r += 1
		if data[j] == '!':
			j += 1
			if part2:
				r -= 1
		elif data[j] == '>':
			if part2:
				r -= 1
			break
	del data[i:j+1]

if not part2:
	s = "".join(data).replace(',','')
	level = 1
	for c in s:
		if c == '{':
			level += 1
		elif c == '}':
			level -= 1
			r += level

repres(r, part2)
