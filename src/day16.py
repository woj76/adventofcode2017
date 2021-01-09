#!/snap/bin/pypy3

from aoc import repres

with open("../data/day16.txt", "rt") as file:
	data = file.read().strip().split(',')

dance = list("abcdefghijklmnop")

def do_dance(dn):
	for d in data:
		if d[0] == 's':
			n = int(d[1:])
			dn = dn[-n:] + dn[:-n]
		elif d[0] == 'x':
			[n1, n2] = d[1:].split('/')
			n1, n2 = int(n1), int(n2)
			dn[n1], dn[n2] = dn[n2], dn[n1]
		elif d[0] == 'p':
			n1 = dn.index(d[1])
			n2 = dn.index(d[3])
			dn[n1], dn[n2] = dn[n2], dn[n1]
	return dn

init_dance = dance[:]

r = "".join(do_dance(dance))

repres(r, False)

dance = init_dance[:]

for k in range(1000000000):
	dance = do_dance(dance)
	if dance == init_dance:
		break

for _ in range(1000000000 % (k+1)):
	dance = do_dance(dance)

r = "".join(dance)

repres(r, True)
