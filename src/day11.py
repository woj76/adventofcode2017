#!/snap/bin/pypy3

from aoc import repres

file = open("../data/day11.txt", "rt")
data = [x for x in file.read().strip().split(',')]
file.close()

part2 = True

def calc_steps(x, y):
	x, y = abs(x), abs(y)
	steps = 2 * min(x // 2, y)
	x -= steps
	y -= steps // 2
	return steps + x + y

x = y = 0
r = float('-inf')

for d in data:
	if d == 'n':
		y -= 1
	elif d == 's':
		y += 1
	elif d == 'nw':
		if x % 2 == 0:
			y -= 1
		x -= 1
	elif d == 'ne':
		if x % 2 == 0:
			y -= 1
		x += 1
	elif d == 'sw':
		if x % 2 == 1:
			y += 1
		x -= 1
	elif d == 'se':
		if x % 2 == 1:
			y += 1
		x += 1
	if part2:
		r = max(r, calc_steps(x,y))

if not part2:
	r = calc_steps(x, y)

repres(r, part2)
