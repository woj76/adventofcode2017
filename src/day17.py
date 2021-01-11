#!/snap/bin/pypy3

from aoc import repres

part2 = True

input = 316

lst = [0]
p = 0
ln = 1

for i in range(0, 50000000 if part2 else 2017):
	p = (p + input + 1) % ln
	if part2:
		if p == 0:
			r = i+1
	else:
		lst.insert(p, i+1)
	ln += 1

if not part2:
	r = lst[(p+1) % ln]

repres(r, part2)
