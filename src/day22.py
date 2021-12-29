#!/usr/bin/python3

from aoc import repres

file = open("../data/day22.txt", "rt")
data = [x for x in file.read().strip().split('\n') if x != '']
file.close()

part2 = True

nodes = {}

y = 0
for d in data:
	x = 0
	for c in d:
		if c == '#':
			nodes[(x,y)] = 2
		x += 1
	y += 1

curr_x = x // 2
curr_y = y // 2

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
curr_dir = 0

infections = 0

for _ in range(10000000 if part2 else 10000):
	node_val = nodes[(curr_x,curr_y)] if (curr_x,curr_y) in nodes else 0
	if part2:
		if node_val == 0:
			curr_dir -= 1
		elif node_val == 2:
			curr_dir += 1
		elif node_val == 3:
			curr_dir += 2
	else:
		if node_val == 2:
			curr_dir += 1
		else:
			curr_dir -= 1
	curr_dir %= len(dirs)
	if part2:
		if node_val == 1:
			infections += 1
		nodes[(curr_x,curr_y)] = (node_val + 1) % 4
	else:
		if node_val == 0:
			nodes[(curr_x,curr_y)] = 2
			infections += 1
		else:
			nodes[(curr_x,curr_y)] = 0
	curr_x += dirs[curr_dir][0]
	curr_y += dirs[curr_dir][1]

repres(infections, part2)
