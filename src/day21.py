#!/snap/bin/pypy3

from aoc import repres

part2 = True

def transforms(pat):
	if len(pat) == 5:
		return transforms2(pat)
	A,B,C,D,E,F,G,H,I = pat[0], pat[1], pat[2], pat[4], pat[5], pat[6], pat[8], pat[9], pat[10]
	r = []
	r.append(A+B+C+'/'+D+E+F+'/'+G+H+I)
	r.append(G+D+A+'/'+H+E+B+'/'+I+F+C)
	r.append(I+H+G+'/'+F+E+D+'/'+C+B+A)
	r.append(C+F+I+'/'+B+E+H+'/'+A+D+G)
	r.append(C+B+A+'/'+F+E+D+'/'+I+H+G)
	r.append(A+D+G+'/'+B+E+H+'/'+C+F+I)
	r.append(G+H+I+'/'+D+E+F+'/'+A+B+C)
	r.append(I+F+C+'/'+H+E+B+'/'+G+D+A)
	return set(r)

def transforms2(pat):
	A,B,C,D = pat[0], pat[1], pat[3], pat[4]
	return set([A+B+'/'+C+D, C+A+'/'+D+B, D+C+'/'+B+A, B+D+'/'+A+C, B+A+'/'+D+C, A+C+'/'+B+D, C+D+'/'+A+B, D+B+'/'+C+A])

patterns = {}

with open("../data/day21.txt", "rt") as file:
	for x in file.read().strip().split('\n'):
		[p, o] = x.split(' => ')
		for px in transforms(p):
			patterns[px] = o

picture = [['.','#','.'], ['.','.','#'], ['#','#','#']]

for _ in range(18 if part2 else 5):
	size = len(picture)
	if size % 2 == 0:
		step = 2
	else:
		step = 3
	new_size = (size // step) * (step+1)
	new_picture = [[' ']*new_size for x in range(new_size)]
	for i in range(size // step):
		for j in range(size // step):
			pat = ""
			for y in range(step):
				for x in range(step):
					pat += picture[j*step+y][i*step+x]
				pat += '/'
			pat = patterns[pat[0:-1]]
			oi = 0
			for y in range(step+1):
				for x in range(step+1):
					new_picture[j*(step+1)+y][i*(step+1)+x] = pat[oi]
					oi += 1
				oi += 1
	picture = new_picture

r = 0

size = len(picture)

for x in range(size):
	for y in range(size):
		if picture[y][x] == '#':
			r += 1

repres(r, part2)
