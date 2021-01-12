#!/snap/bin/pypy3

from aoc import repres

part2 = True

input = 316

lst = [0]
p = 0
ln = 1

for i in range(0, 50000000 if part2 else 2017):
	i += 1
	p = (p + input) % ln
	p = p + 1
	if part2:
		if p == 1:
			r = i
	else:
		lst.insert(p, i)
	ln += 1

if not part2:
	r = lst[(p+1) % ln]

repres(r, part2)
