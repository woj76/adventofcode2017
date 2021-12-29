#!/snap/bin/pypy3

from aoc import repres

file = open("../data/day23.txt", "rt")
data = [x for x in file.read().strip().split('\n') if x != '']
file.close()

r = 0

ip = 0
multiply = 0
regs = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0}

while ip < len(data):
	d = data[ip].split(' ')
	if d[2] in regs:
		v2 = regs[d[2]]
	else:
		v2 = int(d[2])
	if d[0] == 'set':
		regs[d[1]] = v2
		ip += 1
	elif d[0] == 'sub':
		regs[d[1]] -= v2
		ip += 1
	elif d[0] == 'mul':
		multiply += 1
		regs[d[1]] *= v2
		ip += 1
	else:
		assert d[0] == 'jnz'
		if d[1] in regs:
			v1 = regs[d[1]]
		else:
			v1 = int(d[1])
		if v1 != 0:
			ip += v2
		else:
			ip += 1

repres(multiply, False)
