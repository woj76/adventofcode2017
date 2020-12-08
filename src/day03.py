#!/usr/bin/python3

from aoc import repres

input = 325489

part2 = True
r = 0

dirs = [ (0, -1), (1, 0), (0,1), (-1,0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

x = y = 0
positions = {}
dir = 0
value = 0

for i in range(0, input):
	if part2:
		s = 0
		for (dx, dy) in dirs:
			s += positions[(x+dx,y+dy)] if (x+dx,y+dy) in positions.keys() else 0
		value = s if s > 0 else 1
	else:
		value += 1
	positions[(x,y)] = value
	if part2:
		if value > input:
			r = value
			break;
	else:
		if value == input:
			r = abs(x) + abs(y)
			break
	(dx, dy) = dirs[(dir + 1) % 4]
	if not (x+dx, y+dy) in positions.keys():
		dir = (dir + 1) % 4
	(dx, dy) = dirs[dir]
	x += dx
	y += dy

repres(r, part2)
