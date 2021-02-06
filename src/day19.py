#!/snap/bin/pypy3

from aoc import repres

with open("../data/day19.txt", "rt") as file:
	data = [list(x) for x in file.read().split('\n')]

part2 = True

x, y = 1, 0

dir = 'd'
r = 0 if part2 else ''

while True:
	if dir == 'd':
		y += 1
	elif dir == 'u':
		y -= 1
	elif dir == 'l':
		x -= 1
	elif dir == 'r':
		x += 1
	if part2:
		r += 1
	n = data[y][x]
	if n == ' ':
		break
	if n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		if not part2:
			r += n
	elif n == '+':
		for od,nx,ny,nd in [('r',x-1,y,'l'), ('d',x,y-1,'u'), ('l',x+1, y,'r'), ('u',x,y+1,'d')]:
			if od != dir and data[ny][nx] != ' ':
				dir = nd
				break

repres(r, part2)
